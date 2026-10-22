"""Genera index.html autónomo (JS, CSS y logos incrustados). Uso: python3 build.py"""
import base64, io, pathlib
from PIL import Image
R = pathlib.Path(__file__).parent
def uri(name, w):
    im = Image.open(R / 'assets' / name).convert('RGB'); im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    b = io.BytesIO(); im.convert('P', palette=Image.ADAPTIVE, colors=64).save(b, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
h = (R / 'src/template.html').read_text()
for n, w in [('icono-claro.png', 160), ('icono-oscuro.png', 440), ('logo-horizontal-oscuro.png', 520), ('favicon.png', 64)]:
    h = h.replace('assets/' + n, uri(n, w))
for s in ['engine', 'fx', 'app']:
    h = h.replace(f'<script src="{s}.js"></script>', '<script>\n' + (R / f'src/{s}.js').read_text() + '\n</script>')
h = h.replace('initial-scale=1"', 'initial-scale=1, viewport-fit=cover"').replace('</style>', ':root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}\n</style>', 1)
(R / 'index.html').write_text(h); print(len(h) // 1024, 'KB')
