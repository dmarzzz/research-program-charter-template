#!/usr/bin/env python3
"""Render a filled-in charter directory to one self-contained HTML file.

Usage:  python3 render.py path/to/charter_dir [-o index.html]

Needs pandoc. Diagrams are rendered to inline SVG at build time when Playwright
is available (set PLAYWRIGHT_NODE_MODULES to its node_modules folder); otherwise
the page loads mermaid from a CDN when opened, and shows the source if offline.
"""
import html, os, pathlib, re, subprocess, sys, datetime, yaml

HERE = pathlib.Path(__file__).resolve().parent
ORDER = [("one_pager", "One page"), ("space", "Space"), ("thesis", "Thesis"),
         ("open_problems", "Open problems"), ("roadmap", "Roadmap"), ("terms", "Terms")]

def pandoc(md):
    return subprocess.run(["pandoc", "-f", "gfm+hard_line_breaks", "-t", "html", "--no-highlight"],
                          input=md, capture_output=True, text=True, check=True).stdout

def mermaid_svg(src):
    nm = os.environ.get("PLAYWRIGHT_NODE_MODULES")
    if not nm and not (HERE / "node_modules" / "playwright").exists():
        return None
    try:
        r = subprocess.run(["node", str(HERE / "render_mermaid.mjs")], input=src, capture_output=True,
                           text=True, timeout=120, env={**os.environ, **({"PLAYWRIGHT_NODE_MODULES": nm} if nm else {})})
        return r.stdout if r.returncode == 0 and r.stdout.lstrip().startswith("<svg") else None
    except Exception:
        return None

def chip(value):
    v = str(value)
    cls = re.sub(r"[^a-z]+", "-", v.lower()).strip("-")
    return f'<span class="chip chip-{cls}">{html.escape(v.replace("_", " "))}</span>'

def card(block):
    try:
        d = yaml.safe_load(block)
    except yaml.YAMLError:
        return None
    if not isinstance(d, dict):
        return None
    head = d.get("id") or d.get("name") or ""
    title = d.get("question") or d.get("statement") if d.get("id") else ""
    chips = "".join(chip(d[k]) for k in ("status", "stage") if d.get(k))
    rows = ""
    for k, v in d.items():
        if k in ("id", "name", "status", "stage") or (k == "question"):
            continue
        rows += f"<dt>{html.escape(k.replace('_', ' '))}</dt><dd>{html.escape(str(v))}</dd>"
    anchor = f' id="{html.escape(str(d["id"]))}"' if d.get("id") else ""
    q = f'<p class="card-q">{html.escape(str(d["question"]))}</p>' if d.get("question") else ""
    return f'<div class="card"{anchor}><div class="card-head"><span class="card-id">{html.escape(str(head))}</span>{chips}</div>{q}<dl>{rows}</dl></div>'

def transform(fragment, state):
    def code(m):
        lang, body = m.group(1), html.unescape(m.group(2))
        if lang == "mermaid":
            svg = mermaid_svg(body)
            if svg:
                svg = re.sub(r'(<svg[^>]*?)\swidth="100%"', r'\1', svg, count=1)      # keep natural size; the figure scrolls
                svg = re.sub(r'(<svg[^>]*?style=")max-width:\s*([0-9.]+)px;', r'\1width:\2px;', svg, count=1)
                return f'<figure class="tree">{svg}</figure>'
            state["needs_mermaid"] = True
            return f'<figure class="tree"><pre class="mermaid">{html.escape(body)}</pre></figure>'
        if lang == "yaml":
            return card(body) or m.group(0)
        return m.group(0)
    fragment = re.sub(r'<pre class="(\w+)"><code>(.*?)</code></pre>', code, fragment, flags=re.S)
    # link question and premise ids in running text to their cards
    return fragment

CSS = """
:root{--bg:#f6f4ef;--fg:#1c1b19;--mute:#6d6a63;--line:#d9d5cb;--card:#fffdf8;--accent:#8a3b12;--chip:#ece8de}
@media (prefers-color-scheme:dark){:root{--bg:#141413;--fg:#e9e6df;--mute:#9a968d;--line:#2e2d2a;--card:#1b1b19;--accent:#e0915f;--chip:#262522}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 Georgia,'Iowan Old Style','Times New Roman',serif}
.wrap{display:grid;grid-template-columns:15rem minmax(0,46rem);gap:3rem;max-width:66rem;margin:0 auto;padding:2.5rem 1.25rem 6rem}
nav{position:sticky;top:2rem;align-self:start;font:13px/1.5 ui-monospace,SFMono-Regular,Menlo,monospace}
nav .prog{color:var(--fg);font-weight:600;margin-bottom:.25rem}nav .ver{color:var(--mute);margin-bottom:1.25rem}
nav a{display:block;color:var(--mute);text-decoration:none;padding:.2rem 0;border-left:2px solid transparent;padding-left:.75rem;margin-left:-.75rem}
nav a:hover{color:var(--fg);border-left-color:var(--accent)}
section{padding-top:1rem;margin-bottom:4rem;border-top:1px solid var(--line)}section:first-of-type{border-top:0;padding-top:0}
h1{font-size:1.9rem;line-height:1.2;margin:.5rem 0 1rem;font-weight:600;letter-spacing:-.01em}
h2{font:600 .8rem/1.4 ui-monospace,SFMono-Regular,Menlo,monospace;text-transform:uppercase;letter-spacing:.08em;color:var(--accent);margin:2.5rem 0 .75rem}
h3{font-size:1.05rem;margin:1.5rem 0 .5rem}
p,li{max-width:42rem}a{color:var(--accent)}strong{font-weight:600}
code{font:.85em ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--chip);padding:.1em .35em;border-radius:3px}
pre{background:var(--card);border:1px solid var(--line);padding:1rem;overflow-x:auto;border-radius:4px;font:13px/1.5 ui-monospace,Menlo,monospace}pre code{background:none;padding:0}
table{border-collapse:collapse;width:100%;font-size:.92rem;margin:1rem 0}th,td{border-bottom:1px solid var(--line);padding:.5rem .6rem;text-align:left;vertical-align:top}
th{font:600 .72rem/1.4 ui-monospace,Menlo,monospace;text-transform:uppercase;letter-spacing:.06em;color:var(--mute)}
blockquote{margin:1rem 0;padding-left:1rem;border-left:2px solid var(--line);color:var(--mute)}
.card{background:var(--card);border:1px solid var(--line);border-radius:4px;padding:.9rem 1rem;margin:.75rem 0;scroll-margin-top:1rem}
.card-head{display:flex;gap:.5rem;align-items:center;flex-wrap:wrap}
.card-id{font:600 .85rem ui-monospace,Menlo,monospace;color:var(--accent)}
.card-q{margin:.4rem 0 .6rem;font-size:1.02rem}
.card dl{display:grid;grid-template-columns:9.5rem 1fr;gap:.25rem .75rem;margin:0;font-size:.88rem}
.card dt{font:.74rem/1.7 ui-monospace,Menlo,monospace;color:var(--mute);text-transform:lowercase}.card dd{margin:0}
.chip{font:.68rem/1 ui-monospace,Menlo,monospace;background:var(--chip);color:var(--mute);padding:.3rem .45rem;border-radius:3px;text-transform:uppercase;letter-spacing:.05em}
.chip-being-worked,.chip-proof-of-concept{color:var(--accent)}
.tree{position:relative;z-index:2;margin:1.25rem 0;background:#fff;border:1px solid var(--line);border-radius:4px;padding:.75rem;overflow-x:auto;width:min(63.5rem,calc(100vw - 2.5rem));left:-18rem}.tree svg{width:100%!important;max-width:100%;height:auto;display:block}
footer{color:var(--mute);font:12px ui-monospace,Menlo,monospace;margin-top:3rem}
@media (max-width:1080px){.tree{left:0;width:100%}.tree svg{width:auto!important;max-width:none}}
@media (max-width:860px){.wrap{grid-template-columns:1fr;gap:1rem}nav{position:static;display:flex;flex-wrap:wrap;gap:.25rem 1rem}nav .prog,nav .ver{width:100%;margin:0}nav a{border:0;margin:0;padding:0}.card dl{grid-template-columns:1fr}}
@media print{nav{display:none}.wrap{display:block}section{break-before:page}body{background:#fff;color:#000}}
"""

def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    charter = pathlib.Path(argv[1])
    out = pathlib.Path(argv[argv.index("-o") + 1]) if "-o" in argv else charter.parent / "index.html"
    state, sections, nav = {"needs_mermaid": False}, "", ""
    program, version = "Research program", ""
    for doc, label in ORDER:
        path = charter / f"{doc}.md"
        if not path.exists():
            continue
        md = path.read_text()
        if doc == "one_pager":
            m = re.search(r"^# (.+?)(?:: one page)?$", md, flags=re.M)
            if m: program = m.group(1)
            v = re.search(r"\| Version \| (.+?) \|", md)
            if v: version = v.group(1)
        sections += f'<section id="{doc}">{transform(pandoc(md), state)}</section>\n'
        nav += f'<a href="#{doc}">{label}</a>'
    script = ('<script type="module">import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";'
              'mermaid.initialize({startOnLoad:true,theme:"neutral"});</script>') if state["needs_mermaid"] else ""
    built = datetime.date.today().isoformat()
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(program)}: charter</title>
<style>{CSS}</style></head><body><div class="wrap">
<nav><div class="prog">{html.escape(program)}</div><div class="ver">charter {html.escape(version)}</div>{nav}</nav>
<main>{sections}<footer>Built {built} from the markdown in {html.escape(charter.name)}/ with the Research Program Charter format. Edit the markdown, not this file.</footer></main>
</div>{script}</body></html>"""
    out.write_text(page)
    print(f"wrote {out} ({len(page)//1024} KB; diagrams {'inline SVG' if not state['needs_mermaid'] else 'via CDN at view time'})")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
