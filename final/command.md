```bash
docker run --rm -v "$(pwd):/doc" diploma-latex bash -c "cd /doc && latexmk -xelatex -pdf main.tex"
```

Если образ ещё не собран:

```bash
docker build -t diploma-latex .
```
