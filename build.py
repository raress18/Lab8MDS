import json
import os

def build():
    with open("data.json") as f:
        items = json.load(f)

    os.makedirs("site", exist_ok=True)

    # Pagina 1: Lista de cărți
    index_lines = ["<html><body>", "<h1>Lista mea SF</h1>", "<p><a href='about.html'>Despre proiect</a></p>", "<ul>"]
    for item in items:
        index_lines.append(f"  <li><strong>{item['title']}</strong>: {item['description']}</li>")
    index_lines.append("</ul></body></html>")

    with open("site/index.html", "w") as f:
        f.write("\n".join(index_lines))

    # Pagina 2 (NOUĂ): Pagina About
    about_lines = [
        "<html><body>",
        "<h1>Despre</h1>",
        "<p>Acest site are două pagini și este generat automat cu GitHub Actions CD!</p>",
        "<p><a href='index.html'>Înapoi la listă</a></p>",
        "</body></html>"
    ]
    with open("site/about.html", "w") as f:
        f.write("\n".join(about_lines))

if __name__ == "__main__":
    build()