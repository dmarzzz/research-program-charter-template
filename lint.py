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
    """Body with guidance blockquotes, code fences, headings, rules and table markup removed."""
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    keep = []
    for l in body.splitlines():
        if l.lstrip().startswith((">", "#")) or l.strip() in ("---", "") or re.match(r"^\s*\|?[\s:|-]+\|?\s*$", l):
            continue
        keep.append(l.replace("|", " ").replace("*", ""))
    return "\n".join(keep)

UNDECIDED = re.compile(r"\b(TBD|TODO|not yet (written|decided|defined|set)|not set|to confirm|none committed)\b", re.I)

def cards(md):
    """YAML cards found in fenced blocks."""
    out = []
    for block in re.findall(r"```yaml\n(.*?)```", md, flags=re.S):
        try:
            d = yaml.safe_load(block)
        except yaml.YAMLError:
            continue
        if isinstance(d, dict): out.append(d)
    return out

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
            filled = [l for l in body.splitlines() if l.strip() and not l.lstrip().startswith(">") and l.strip() not in ("---", "```", "```yaml")]
            if not filled:                                  # cards in code blocks count as content
                errors.append(f"{doc}.md: \"{s['title']}\" is empty")
            limit = WORD_LIMITS.get((doc, s["id"]))
            if limit and len(text.split()) > limit:
                warnings.append(f"{doc}.md: \"{s['title']}\" is {len(text.split())} words (limit {limit})")
        n_undecided = len(UNDECIDED.findall(md))
        if n_undecided:
            warnings.append(f"{doc}.md: {n_undecided} undecided marker(s) (TBD, not yet written, not set, to confirm)")

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

    # items past research must carry an appetite, a decision date and one accountable person
    if "roadmap" in texts:
        for c in cards(texts["roadmap"]):
            stage = str(c.get("stage", "")).strip()
            if not stage or stage == "research": continue
            for field in ("appetite", "decision_date", "accountable"):
                v = str(c.get(field, "") or "")
                if not v.strip() or UNDECIDED.search(v):
                    errors.append(f"roadmap.md: item \"{c.get('name', '?')}\" is at {stage} without a usable {field}")

    # premises and questions point at each other
    if "thesis" in texts and "open_problems" in texts:
        premises = set(re.findall(r"\*\*(P\d+)\.", texts["thesis"]))
        served = set()
        for c in cards(texts["open_problems"]):
            for ref in re.findall(r"\bP\d+\b", str(c.get("serves", ""))):
                served.add(ref)
                if premises and ref not in premises:
                    errors.append(f"open_problems.md: {c.get('id', '?')} serves {ref}, which is not a premise in thesis.md")
        for p in sorted(premises - served):
            warnings.append(f"thesis.md: premise {p} has no open problem serving it")

    # the space is written about the world
    if "space" in texts:
        for title, body in sections_of(texts["space"]).items():
            if "shared asset" in title or "steward" in title: continue
            hits = re.findall(r"\b(we|our|us)\b", prose(body), flags=re.I)
            if hits:
                warnings.append(f"space.md: \"{title}\" uses first person ({len(hits)}x); the space is written about the world")

    for w in warnings: print(f"warning  {w}")
    for e in errors:   print(f"error    {e}")
    failed = bool(errors) or (strict and bool(warnings))
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s): {'FAIL' if failed else 'ok'}")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
