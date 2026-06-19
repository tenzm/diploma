#!/usr/bin/env python3
"""Count visible words and characters in thesis files.

The script is intentionally dependency-free. It can be used for the future
`result/contents` directory, for the example thesis files, or for individual
`.tex` / `.md` files.

Examples:
    python3 scripts/report_stats.py result/contents
    python3 scripts/report_stats.py result/contents --by both
    python3 scripts/report_stats.py result/contents --format csv
    python3 scripts/report_stats.py example/contents/1_3.tex --by section

By default, the script uses the diploma page limits from CLAUDE.md:
    - 260 words per page
    - 2200 characters per page
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, TextIO


DEFAULT_PAGE_WORDS = 260
DEFAULT_PAGE_CHARS = 2200
SUPPORTED_EXTENSIONS = {".tex", ".md", ".markdown"}

WORD_RE = re.compile(
    r"[A-Za-zА-Яа-яЁё0-9]+(?:[._:/-][A-Za-zА-Яа-яЁё0-9]+)*",
    re.UNICODE,
)

LATEX_HEADING_RE = re.compile(
    r"\\(?P<kind>section|subsection|subsubsection)\*?\s*\{(?P<title>(?:[^{}]|\{[^{}]*\})*)\}",
    re.DOTALL,
)

MARKDOWN_HEADING_RE = re.compile(
    r"^(?P<marks>#{1,6})\s+(?P<title>.+?)\s*$",
    re.MULTILINE,
)


@dataclass
class Count:
    words: int
    chars: int
    chars_no_spaces: int


@dataclass
class ReportRow:
    scope: str
    file: str
    level: str
    title: str
    words: int
    chars: int
    chars_no_spaces: int
    pages_by_words: float
    pages_by_chars: float
    pages_estimate: float


def strip_latex_comments(text: str) -> str:
    """Remove LaTeX comments while preserving escaped percent signs."""
    cleaned_lines: list[str] = []
    for line in text.splitlines():
        cut_at = None
        for index, char in enumerate(line):
            if char != "%":
                continue
            backslashes = 0
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                backslashes += 1
                cursor -= 1
            if backslashes % 2 == 0:
                cut_at = index
                break
        cleaned_lines.append(line if cut_at is None else line[:cut_at])
    return "\n".join(cleaned_lines)


def strip_latex(text: str) -> str:
    """Approximate visible text extraction from LaTeX."""
    text = strip_latex_comments(text)

    # Remove code/listing/verbatim blocks from word counts.
    for env in ("verbatim", "lstlisting", "minted"):
        text = re.sub(
            rf"\\begin\{{{env}\}}.*?\\end\{{{env}\}}",
            " ",
            text,
            flags=re.DOTALL,
        )

    # Remove math blocks and inline math. Formulas are usually not counted as
    # prose words, while their explanation in the surrounding text is counted.
    math_envs = (
        "equation",
        "equation*",
        "align",
        "align*",
        "gather",
        "gather*",
        "multline",
        "multline*",
        "displaymath",
    )
    for env in math_envs:
        escaped_env = re.escape(env)
        text = re.sub(
            rf"\\begin\{{{escaped_env}\}}.*?\\end\{{{escaped_env}\}}",
            " ",
            text,
            flags=re.DOTALL,
        )

    text = re.sub(r"\\\[.*?\\\]", " ", text, flags=re.DOTALL)
    text = re.sub(r"\\\(.*?\\\)", " ", text, flags=re.DOTALL)
    text = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.DOTALL)
    text = re.sub(r"(?<!\\)\$.*?(?<!\\)\$", " ", text, flags=re.DOTALL)

    # Remove commands that should not contribute prose.
    text = re.sub(
        r"\\(?:cite|citep|citet|ref|eqref|label|url|href|includegraphics)"
        r"\*?(?:\[[^\]]*\])?(?:\{[^{}]*\}){1,2}",
        " ",
        text,
    )

    # Keep the visible argument of formatting/section-like commands.
    for _ in range(8):
        new_text = re.sub(
            r"\\[A-Za-zА-Яа-яЁё]+\*?(?:\[[^\]]*\])?\{([^{}]*)\}",
            r" \1 ",
            text,
        )
        if new_text == text:
            break
        text = new_text

    text = re.sub(r"\\begin\{[^{}]*\}|\\end\{[^{}]*\}", " ", text)
    text = re.sub(r"\\item(?:\[[^\]]*\])?", " ", text)
    text = re.sub(r"\\[A-Za-zА-Яа-яЁё]+\*?(?:\[[^\]]*\])?", " ", text)
    text = re.sub(r"\\([%#$&_{}])", r"\1", text)
    text = text.replace("~", " ")
    text = re.sub(r"[{}]", " ", text)

    return normalize_text(text)


def strip_markdown(text: str) -> str:
    """Approximate visible text extraction from Markdown."""
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"^#{1,6}\s+", " ", text, flags=re.MULTILINE)
    text = re.sub(r"^[>\-*+]\s+", " ", text, flags=re.MULTILINE)
    text = re.sub(r"^\d+\.\s+", " ", text, flags=re.MULTILINE)
    text = re.sub(r"[*_~]", " ", text)
    return normalize_text(text)


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def visible_text(text: str, suffix: str) -> str:
    if suffix == ".tex":
        return strip_latex(text)
    if suffix in {".md", ".markdown"}:
        return strip_markdown(text)
    return normalize_text(text)


def count_text(text: str) -> Count:
    text = normalize_text(text)
    return Count(
        words=len(WORD_RE.findall(text)),
        chars=len(text),
        chars_no_spaces=len(re.sub(r"\s+", "", text)),
    )


def make_row(
    *,
    scope: str,
    file: str,
    level: str,
    title: str,
    count: Count,
    page_words: int,
    page_chars: int,
) -> ReportRow:
    pages_by_words = count.words / page_words if page_words else 0
    pages_by_chars = count.chars / page_chars if page_chars else 0
    return ReportRow(
        scope=scope,
        file=file,
        level=level,
        title=title,
        words=count.words,
        chars=count.chars,
        chars_no_spaces=count.chars_no_spaces,
        pages_by_words=round(pages_by_words, 2),
        pages_by_chars=round(pages_by_chars, 2),
        pages_estimate=round(max(pages_by_words, pages_by_chars), 2),
    )


def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def collect_files(paths: Iterable[Path], extensions: set[str]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if not path.exists():
            raise FileNotFoundError(path)
        if path.is_file():
            if path.suffix.lower() in extensions:
                files.append(path)
            continue
        files.extend(
            candidate
            for candidate in sorted(path.rglob("*"))
            if candidate.is_file() and candidate.suffix.lower() in extensions
        )
    return sorted(dict.fromkeys(files))


def clean_title(raw_title: str, suffix: str) -> str:
    return visible_text(raw_title, suffix)


def section_rows_for_file(
    path: Path,
    *,
    page_words: int,
    page_chars: int,
    include_unnamed: bool,
    rollup: bool,
) -> list[ReportRow]:
    text = read_file(path)
    suffix = path.suffix.lower()

    if suffix == ".tex":
        return latex_section_rows(
            path,
            text,
            page_words=page_words,
            page_chars=page_chars,
            include_unnamed=include_unnamed,
            rollup=rollup,
        )
    if suffix in {".md", ".markdown"}:
        return markdown_section_rows(
            path,
            text,
            page_words=page_words,
            page_chars=page_chars,
            include_unnamed=include_unnamed,
            rollup=rollup,
        )

    return []


def latex_section_rows(
    path: Path,
    text: str,
    *,
    page_words: int,
    page_chars: int,
    include_unnamed: bool,
    rollup: bool,
) -> list[ReportRow]:
    level_by_kind = {"section": 1, "subsection": 2, "subsubsection": 3}
    matches = list(LATEX_HEADING_RE.finditer(text))
    return split_into_sections(
        path,
        text,
        matches,
        suffix=".tex",
        heading_level=lambda match: level_by_kind[match.group("kind")],
        heading_title=lambda match: match.group("title"),
        page_words=page_words,
        page_chars=page_chars,
        include_unnamed=include_unnamed,
        rollup=rollup,
    )


def markdown_section_rows(
    path: Path,
    text: str,
    *,
    page_words: int,
    page_chars: int,
    include_unnamed: bool,
    rollup: bool,
) -> list[ReportRow]:
    matches = list(MARKDOWN_HEADING_RE.finditer(text))
    return split_into_sections(
        path,
        text,
        matches,
        suffix=path.suffix.lower(),
        heading_level=lambda match: len(match.group("marks")),
        heading_title=lambda match: match.group("title"),
        page_words=page_words,
        page_chars=page_chars,
        include_unnamed=include_unnamed,
        rollup=rollup,
    )


def split_into_sections(
    path: Path,
    text: str,
    matches: list[re.Match[str]],
    *,
    suffix: str,
    heading_level,
    heading_title,
    page_words: int,
    page_chars: int,
    include_unnamed: bool,
    rollup: bool,
) -> list[ReportRow]:
    if not matches:
        if not include_unnamed:
            return []
        count = count_text(visible_text(text, suffix))
        return [
            make_row(
                scope="section",
                file=str(path),
                level="-",
                title="(без заголовка)",
                count=count,
                page_words=page_words,
                page_chars=page_chars,
            )
        ]

    section_meta: list[dict[str, object]] = []
    counts: list[Count] = []
    stack_ids_by_level: dict[int, int] = {}
    current_stack: list[int] = []
    current_id: int | None = None
    previous_end = 0

    def add_count(section_ids: list[int], raw_text: str) -> None:
        clean = visible_text(raw_text, suffix)
        count = count_text(clean)
        for section_id in section_ids:
            counts[section_id] = Count(
                words=counts[section_id].words + count.words,
                chars=counts[section_id].chars + count.chars,
                chars_no_spaces=counts[section_id].chars_no_spaces + count.chars_no_spaces,
            )

    if include_unnamed and matches[0].start() > 0:
        title = "(до первого заголовка)"
        section_meta.append({"level": "-", "title": title, "path": title})
        counts.append(Count(0, 0, 0))
        add_count([0], text[: matches[0].start()])

    for match in matches:
        if current_id is not None:
            target_ids = current_stack if rollup else [current_id]
            add_count(target_ids, text[previous_end : match.start()])

        level = int(heading_level(match))
        title = clean_title(str(heading_title(match)), suffix)

        for old_level in [item for item in stack_ids_by_level if item >= level]:
            del stack_ids_by_level[old_level]

        section_id = len(section_meta)
        parent_stack = [
            stack_ids_by_level[item]
            for item in sorted(stack_ids_by_level)
            if item < level
        ]
        current_stack = parent_stack + [section_id]
        stack_ids_by_level[level] = section_id

        path_parts = [str(section_meta[item]["title"]) for item in parent_stack]
        path_parts.append(title)
        path_title = " / ".join(path_parts)
        section_meta.append({"level": str(level), "title": title, "path": path_title})
        counts.append(Count(0, 0, 0))

        title_targets = current_stack if rollup else [section_id]
        add_count(title_targets, title)

        current_id = section_id
        previous_end = match.end()

    if current_id is not None:
        target_ids = current_stack if rollup else [current_id]
        add_count(target_ids, text[previous_end:])

    rows: list[ReportRow] = []
    for meta, count in zip(section_meta, counts):
        rows.append(
            make_row(
                scope="section",
                file=str(path),
                level=str(meta["level"]),
                title=str(meta["path"] if rollup else meta["title"]),
                count=count,
                page_words=page_words,
                page_chars=page_chars,
            )
        )

    return rows


def file_rows(
    files: Iterable[Path],
    *,
    page_words: int,
    page_chars: int,
) -> list[ReportRow]:
    rows: list[ReportRow] = []
    for path in files:
        count = count_text(visible_text(read_file(path), path.suffix.lower()))
        rows.append(
            make_row(
                scope="file",
                file=str(path),
                level="-",
                title=path.name,
                count=count,
                page_words=page_words,
                page_chars=page_chars,
            )
        )
    return rows


def total_row(rows: list[ReportRow], page_words: int, page_chars: int) -> ReportRow:
    total = Count(
        words=sum(row.words for row in rows),
        chars=sum(row.chars for row in rows),
        chars_no_spaces=sum(row.chars_no_spaces for row in rows),
    )
    return make_row(
        scope="total",
        file="-",
        level="-",
        title="Итого",
        count=total,
        page_words=page_words,
        page_chars=page_chars,
    )


def output_table(rows: list[ReportRow], stream: TextIO) -> None:
    columns = [
        ("scope", "scope"),
        ("file", "file"),
        ("level", "lvl"),
        ("words", "words"),
        ("chars", "chars"),
        ("chars_no_spaces", "chars_no_sp"),
        ("pages_estimate", "pages"),
        ("title", "title"),
    ]
    data = [
        {field: str(getattr(row, field)) for field, _ in columns}
        for row in rows
    ]
    widths = {
        field: max(len(header), *(len(item[field]) for item in data))
        for field, header in columns
    }

    header = " | ".join(header.ljust(widths[field]) for field, header in columns)
    separator = "-+-".join("-" * widths[field] for field, _ in columns)
    print(header, file=stream)
    print(separator, file=stream)
    for item in data:
        print(
            " | ".join(item[field].ljust(widths[field]) for field, _ in columns),
            file=stream,
        )


def output_csv(rows: list[ReportRow], stream: TextIO) -> None:
    writer = csv.DictWriter(stream, fieldnames=list(asdict(rows[0]).keys()))
    writer.writeheader()
    for row in rows:
        writer.writerow(asdict(row))


def output_json(rows: list[ReportRow], stream: TextIO) -> None:
    json.dump([asdict(row) for row in rows], stream, ensure_ascii=False, indent=2)
    print(file=stream)


def output_list(rows: list[ReportRow], stream: TextIO) -> None:
    visible_rows = [row for row in rows if row.scope != "total"]
    for index, row in enumerate(visible_rows, start=1):
        filename = Path(row.file).name
        print(f"{index}) {filename} - words={row.words} - chars={row.chars}", file=stream)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Count visible words and characters in thesis .tex/.md files.",
    )
    parser.add_argument(
        "paths",
        nargs="+",
        type=Path,
        help="Files or directories to analyze, for example result/contents.",
    )
    parser.add_argument(
        "--by",
        choices=("section", "file", "both"),
        default="file",
        help="Report granularity. Default: file.",
    )
    parser.add_argument(
        "--format",
        choices=("list", "table", "csv", "json"),
        default="list",
        help="Output format. Default: list.",
    )
    parser.add_argument(
        "--extensions",
        default=",".join(sorted(SUPPORTED_EXTENSIONS)),
        help="Comma-separated file extensions to include. Default: .markdown,.md,.tex.",
    )
    parser.add_argument(
        "--page-words",
        type=int,
        default=DEFAULT_PAGE_WORDS,
        help=f"Words per page limit. Default: {DEFAULT_PAGE_WORDS}.",
    )
    parser.add_argument(
        "--page-chars",
        type=int,
        default=DEFAULT_PAGE_CHARS,
        help=f"Characters per page limit. Default: {DEFAULT_PAGE_CHARS}.",
    )
    parser.add_argument(
        "--include-unnamed",
        action="store_true",
        help="Include text before the first heading and files without headings.",
    )
    parser.add_argument(
        "--rollup",
        action="store_true",
        help="For section reports, aggregate subsection text into parent sections.",
    )
    parser.add_argument(
        "--max-pages",
        type=float,
        default=None,
        help="Exit with code 1 if any reported row exceeds this page estimate.",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    extensions = {
        extension.strip().lower()
        for extension in args.extensions.split(",")
        if extension.strip()
    }
    extensions = {
        extension if extension.startswith(".") else f".{extension}"
        for extension in extensions
    }

    try:
        files = collect_files(args.paths, extensions)
    except FileNotFoundError as error:
        print(f"error: path not found: {error}", file=sys.stderr)
        return 2

    if not files:
        print("error: no supported files found", file=sys.stderr)
        return 2

    rows: list[ReportRow] = []
    if args.by in {"file", "both"}:
        file_report = file_rows(
            files,
            page_words=args.page_words,
            page_chars=args.page_chars,
        )
        rows.extend(file_report)
        rows.append(total_row(file_report, args.page_words, args.page_chars))

    if args.by in {"section", "both"}:
        section_report: list[ReportRow] = []
        for path in files:
            section_report.extend(
                section_rows_for_file(
                    path,
                    page_words=args.page_words,
                    page_chars=args.page_chars,
                    include_unnamed=args.include_unnamed,
                    rollup=args.rollup,
                )
            )
        rows.extend(section_report)
        if section_report:
            rows.append(total_row(section_report, args.page_words, args.page_chars))

    if not rows:
        print("error: no report rows produced", file=sys.stderr)
        return 2

    if args.format == "list":
        output_list(rows, sys.stdout)
    elif args.format == "table":
        output_table(rows, sys.stdout)
    elif args.format == "csv":
        output_csv(rows, sys.stdout)
    else:
        output_json(rows, sys.stdout)

    if args.max_pages is not None:
        exceeded = [
            row for row in rows
            if row.scope != "total" and row.pages_estimate > args.max_pages
        ]
        if exceeded:
            print(
                f"error: {len(exceeded)} row(s) exceed --max-pages={args.max_pages}",
                file=sys.stderr,
            )
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
