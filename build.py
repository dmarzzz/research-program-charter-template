#!/usr/bin/env python3
"""Rebuild README.md, DOCUMENTS.md and formats/*.md from the two spec files.
Run from anywhere: python3 build.py"""
import re, pathlib, yaml
here = pathlib.Path(__file__).resolve().parent

def strip_banner(text): return re.sub(r"\A(#.*\n)+\n", "", text)
def box(s): return "```yaml\n" + s.rstrip() + "\n```\n\n"

# ---------------------------------------------------------------- README.md
src = (here / "charter.spec.yaml").read_text()
head = (here / "readme.head.md").read_text().rstrip() + "\n\n"
blocks = re.split(r"\n(?=[a-z_]+:)", strip_banner(src).strip())
titles = {"format": "Format", "profiles": "Size profiles", "primary_artifact": "Primary artifact",
          "charter": "The charter", "rules": "Rules", "lifecycle": "Lifecycle",
          "optional_steps": "Optional steps", "format_test": "Is the format working?"}
docs = yaml.safe_load((here / "documents.spec.yaml").read_text())["documents"]

out = head + "## The documents\n\nFormats for each are in `DOCUMENTS.md`; blank templates are in `formats/`.\n\n"
out += "| Document | Part | Required | Length |\n|---|---|---|---|\n"
for d in docs:
    out += f"| [{d['title']}](formats/{d['id']}.md) | {d['part']} | {d['required']} | {d['length']} |\n"
out += "\n## The spec\n\nSource: `charter.spec.yaml`. This README is rebuilt from it by `build.py`.\n\n"
for b in blocks:
    key = b.split(":", 1)[0]
    out += f"### {titles.get(key, key)}\n\n" + box(b)
(here / "README.md").write_text(out)

# ------------------------------------------------------------- DOCUMENTS.md
raw = strip_banner((here / "documents.spec.yaml").read_text())
raw_docs = re.split(r"\n(?=  - id: )", raw.split("documents:\n", 1)[1].rstrip())
md = "# Program Charter: the documents and their formats\n\n"
md += ("Generated from `documents.spec.yaml` by `build.py`. Each part of the charter can be written at summary depth "
       "inside the charter, or as its own document in the format below. Only the one-pager, the charter itself, and the "
       "review note are always required. Everything else is written when a named reader asks for it.\n\n")
md += "| Document | Reader | Length | Updated |\n|---|---|---|---|\n"
for d in docs:
    md += f"| **{d['title']}** | {d['reader']} | {d['length']} | {d['updated']} |\n"
md += "\n"
for d, r in zip(docs, raw_docs):
    md += f"## {d['title']}\n\n"
    md += f"Part: {d['part']}. Required: {d['required']}\n\n"
    md += "| # | Section | What goes in it |\n|---|---|---|\n"
    for i, s in enumerate(d["sections"], 1):
        md += f"| {i} | {s['title']} | {s['prompt']} |\n"
    md += "\n**Checks before it goes out**\n\n" + "".join(f"- {c}\n" for c in d["checks"])
    md += "\n**How it usually goes wrong**\n\n" + "".join(f"- {c}\n" for c in d["failures"]) + "\n"
    if "sub_formats" in d:
        for name, fields in d["sub_formats"].items():
            width = max(len(k) for k in fields) + 1
            body = f"{name}:\n" + "".join(f"  {(k + ':').ljust(width + 1)} {v}\n" for k, v in fields.items())
            md += f"**Sub-format: {name.replace('_', ' ')}**\n\n" + box(body)
    md += f"Blank template: `formats/{d['id']}.md`\n\n"
(here / "DOCUMENTS.md").write_text(md)

# ---------------------------------------------------------------- templates
fdir = here / "formats"; fdir.mkdir(exist_ok=True)
for d in docs:
    t = f"# {d['title']}\n\n"
    t += f"> Program Charter format `{d['id']}`. Reader: {d['reader']}. Length: {d['length']}. Updated: {d['updated']}.\n"
    t += "> Delete these guidance lines as you fill the sections in.\n\n"
    for i, s in enumerate(d["sections"], 1):
        t += f"## {i}. {s['title']}\n\n> {s['prompt']}\n\n\n"
    if "sub_formats" in d:
        for name, fields in d["sub_formats"].items():
            t += f"### {name.replace('_', ' ').capitalize()} (copy per item)\n\n```yaml\n"
            t += "".join(f"{k}:    # {v}\n" for k, v in fields.items()) + "```\n\n"
    t += "---\n\nChecks before it goes out:\n\n" + "".join(f"- [ ] {c}\n" for c in d["checks"])
    (fdir / f"{d['id']}.md").write_text(t)

print("wrote README.md, DOCUMENTS.md,", len(docs), "templates in formats/")
