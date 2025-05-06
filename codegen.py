# vibe/codegen.py

def generate_html(ast):
    page = ast['Page']
    html = [f"<html>\n<head><title>{page['title']}</title></head>\n<body>"]
    for section in page['sections']:
        html.append(f'  <section class="{section["title"].lower()}">')
        for k, v in section['content'].items():
            if isinstance(v, dict):
                html.append(f'    <a href="{v["link"]}">{v["label"]}</a>')
            elif isinstance(v, list):
                html.append('    <ul>')
                for item in v:
                    html.append(f'      <li>{item}</li>')
                html.append('    </ul>')
            else:
                html.append(f'    <h1>{v}</h1>')
        html.append('  </section>')
    html.append('</body>\n</html>')
    return '\n'.join(html)
