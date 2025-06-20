index.html: index.template.html render_template.py
	uv run --script render_template.py > index.html

.PHONY: serve clean format
serve:
	python3 -m http.server 8000

clean:
	rm -f index.html

format:
	uv run --with ruff ruff format .
