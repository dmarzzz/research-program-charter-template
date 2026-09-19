#!/usr/bin/env python3
"""Generate the blank templates in formats/ from the specs in spec/.
Run from anywhere: python3 build.py"""
import pathlib, yaml
here = pathlib.Path(__file__).resolve().parent
out = here / "formats"; out.mkdir(exist_ok=True)
n = 0
for f in sorted((here / "spec").glob("*.yaml")):
    d = yaml.safe_load(f.read_text())
    if "sections" not in d:            # charter.yaml is structure only
        continue
    t = f"# {d['title']}\n\n"
    t += f"> Research Program Charter format `{d['id']}` (spec: `spec/{f.name}`). Reader: {d['reader']}. Updated: {d['updated']}.\n"
    t += "> Delete these guidance lines as you fill the sections in.\n\n"
    for i, s in enumerate(d["sections"], 1):
        tag = "  *(required in the charter)*" if s.get("required") else ""
        t += f"## {i}. {s['title']}{tag}\n\n> {s['prompt']}\n\n\n"
    for name, fields in d.get("sub_formats", {}).items():
        t += f"### {name.replace('_', ' ').capitalize()} (copy per item)\n\n```yaml\n"
        t += "".join(f"{k}:    # {v}\n" for k, v in fields.items()) + "```\n\n"
    t += "---\n\nChecks before it goes out:\n\n" + "".join(f"- [ ] {c}\n" for c in d["checks"])
    (out / f"{d['id']}.md").write_text(t); n += 1
print(f"wrote {n} templates to formats/")
