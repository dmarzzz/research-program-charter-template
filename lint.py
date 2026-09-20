#!/usr/bin/env python3
"""Lint a filled-in Research Program Charter against the specs in spec/.

Usage:  python3 lint.py path/to/charter_dir [--strict]

The charter directory holds the filled-in copies of formats/*.md, keeping the
file names (one_pager.md, space.md, thesis.md, open_problems.md, roadmap.md,
terms.md). Errors fail the run; warnings do not, unless --strict is given.
Structural checks only. Judgement belongs to the review skill.
"""
import pathlib, re, sys, yaml

HERE = pathlib.Path(__file__).resolve().parent
REQUIRED_FILES = ["one_pager", "space", "thesis", "open_problems", "roadmap", "terms"]
WORD_LIMITS = {("thesis", "simply"): 200}      # (doc id, section id): max words
ONE_PAGER_WORDS = 600

def norm(s): return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()

def sections_of(md):
    """Map normalised '## heading' -> body text, ignoring numbering and the required tag."""
    out, cur = {}, None
    for line in md.splitlines():
        m = re.match(r"^##\s+(?:\d+\.\s*)?(.*?)(?:\s*\*\(required in the charter\)\*)?\s*$", line)
        if m and not line.startswith("###"):
            cur = norm(m.group(1)); out[cur] = []
        elif cur is not None:
            out[cur].append(line)
    return {k: "\n".join(v) for k, v in out.items()}

def prose(body):
    """Body with guidance blockquotes, code fences and rules removed."""
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    keep = [l for l in body.splitlines() if not l.lstrip().startswith(">") and l.strip() not in ("---", "")]
    return "\n".join(keep)

def main(argv):
    if len(argv) < 2:
        print(__doc__); return 2
    charter = pathlib.Path(argv[1]); strict = "--strict" in argv
    errors, warnings = [], []
    specs = {}
    for f in (HERE / "spec").glob("*.yaml"):
        d = yaml.safe_load(f.read_text())
        if "sections" in d: specs[d["id"]] = d

    texts = {}
    for doc in REQUIRED_FILES:
        path = charter / f"{doc}.md"
        if not path.exists():
            errors.append(f"{doc}.md: missing (required)"); continue
        texts[doc] = path.read_text()

    for doc, md in texts.items():
        spec, found = specs[doc], sections_of(md)
        for s in spec["sections"]:
            is_part = "question" in spec                    # parts carry required flags; supporting docs require all
            if is_part and not s.get("required"): continue
            body = found.get(norm(s["title"]))
            if body is None:
                errors.append(f"{doc}.md: required section missing: \"{s['title']}\""); continue
            if s["prompt"] in body:
                errors.append(f"{doc}.md: \"{s['title']}\" still contains the template guidance")
            text = prose(body)
            if not text.strip():
                errors.append(f"{doc}.md: \"{s['title']}\" is empty")
            limit = WORD_LIMITS.get((doc, s["id"]))
            if limit and len(text.split()) > limit:
                warnings.append(f"{doc}.md: \"{s['title']}\" is {len(text.split())} words (limit {limit})")
        if re.search(r"\b(TBD|TODO|lorem ipsum)\b", md, flags=re.I):
            warnings.append(f"{doc}.md: contains TBD/TODO placeholders")

    if "one_pager" in texts:
        n = len(prose(texts["one_pager"]).split())
        if n > ONE_PAGER_WORDS:
            warnings.append(f"one_pager.md: {n} words; a one-pager should stay near {ONE_PAGER_WORDS}")

    # question ids: unique, and every roadmap trace resolves
    ids = []
    if "open_problems" in texts:
        ids = re.findall(r"^\s*id:\s*[\"']?(Q\d+)\b", texts["open_problems"], flags=re.M)
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        if dupes: errors.append(f"open_problems.md: duplicate question ids: {', '.join(dupes)}")
        if len(set(ids)) < 5: warnings.append(f"open_problems.md: {len(set(ids))} question ids found; the format expects at least 5")
    if "roadmap" in texts:
        traces = re.findall(r"^\s*traced_to:\s*[\"']?([A-Za-z0-9, ]+)", texts["roadmap"], flags=re.M)
        if not traces: warnings.append("roadmap.md: no items with a traced_to field")
        for t in traces:
            for ref in [x.strip() for x in t.split(",") if x.strip()]:
                if ref.lower() != "untraced" and ref not in ids:
                    errors.append(f"roadmap.md: traced_to \"{ref}\" is not a question id in open_problems.md")

    for w in warnings: print(f"warning  {w}")
    for e in errors:   print(f"error    {e}")
    failed = bool(errors) or (strict and bool(warnings))
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s): {'FAIL' if failed else 'ok'}")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
