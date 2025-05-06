# vibe
“AI-Enhanced Web DSL - Build websites with simple language + AI.”

**Vibe** is a new AI-enhanced DSL (Domain-Specific Language) for fast web design with smart AI-assisted components.
A simple DSL (Domain-Specific Language) and tool to build HTML websites from readable `.vibe` files.

## Install

```bash
git clone https://github.com/acatree/vibe.git
```

## ✨ Features

- Minimal syntax to describe pages and sections.
- Converts `.vibe` files into clean HTML output.
- Easy to extend and customize.

### Install dependencies

Make sure you have Python 3.12+ and `pip` installed.

```bash
pip install -r requirements.txt
```

### Install the package (optional)

To use `vibe` as a **global CLI command:**

```bash
pip install .
```

## 🔧 How to Run

After writing your `.vibe` file (example: `mysite.vibe`), you can build the site:

### ▶️ If installed as package:

```bash
vibe mysite.vibe
```

### If running locally (without install):

```bash
python -m vibe.cli mysite.vibe
```

✅ The output will be generated at `dist/index.html`.


## View your site
(run a local server):

```bash
cd dist
python -m http.server 8000
```

Visit `http://localhost:8000` in your browser.


## Development

To contribute or customize:

- **Lexer:** `vibe/lexer.py`
- **Parser:** `vibe/parser.py`
- **Builder:** `vibe/build.py`

Modify these files to add new syntax or extend functionality.

## 🤝 Contributing

Feel free to fork, submit issues, or make pull requests.

## 📄 License

MIT License.
