import json
import os
from build import build

def test_pages_are_generated():
    build() # rulăm scriptul de build
    
    # Verificăm pagina principală
    with open("site/index.html") as f:
        index_html = f.read()
    with open("data.json") as f:
        items = json.load(f)
    for item in items:
        assert item["title"] in index_html
        
    # Verificăm pagina nouă (dacă fișierul a fost creat)
    assert os.path.exists("site/about.html")