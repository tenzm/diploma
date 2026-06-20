#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FINAL_DIR="$SCRIPT_DIR/final"
IMAGE_NAME="diploma-latex"
CONTAINER_NAME="diploma-build"

usage() {
  echo "Usage: $0 [--rebuild] [--clean]"
  echo ""
  echo "  --rebuild   Force rebuild of the Docker image"
  echo "  --clean     Run latexmk -C (full clean) instead of building"
  exit 1
}

REBUILD=0
CLEAN=0

for arg in "$@"; do
  case "$arg" in
    --rebuild) REBUILD=1 ;;
    --clean)   CLEAN=1 ;;
    --help|-h) usage ;;
    *) echo "Unknown option: $arg"; usage ;;
  esac
done

# Build image if missing or --rebuild requested
if [[ "$REBUILD" -eq 1 ]] || ! docker image inspect "$IMAGE_NAME" &>/dev/null; then
  echo "==> Building Docker image '$IMAGE_NAME'..."
  docker build -t "$IMAGE_NAME" "$FINAL_DIR"
else
  echo "==> Docker image '$IMAGE_NAME' already exists (use --rebuild to refresh)"
fi

# Choose latexmk command
if [[ "$CLEAN" -eq 1 ]]; then
  LATEX_CMD="latexmk -C"
  echo "==> Cleaning build artifacts..."
else
  LATEX_CMD="latexmk -xelatex -pdf -interaction=nonstopmode main.tex"
  echo "==> Compiling diploma..."
fi

# Run container
docker run --rm \
  --name "$CONTAINER_NAME" \
  -v "$FINAL_DIR:/doc" \
  -w /doc \
  "$IMAGE_NAME" \
  bash -c "$LATEX_CMD"

if [[ "$CLEAN" -eq 0 ]]; then
  PDF="$FINAL_DIR/main.pdf"
  if [[ -f "$PDF" ]]; then
    SIZE=$(du -h "$PDF" | cut -f1)
    echo ""
    echo "==> Done: $PDF ($SIZE)"
  else
    echo "==> Build finished but main.pdf not found — check logs above"
    exit 1
  fi
fi
