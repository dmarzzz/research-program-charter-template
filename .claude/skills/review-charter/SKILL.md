---
name: review-charter
description: Review a filled-in Research Program Charter (or a pull request that changes one) against the format's specs. Use when asked to review, critique, or check a program charter, its space, thesis, open problems, roadmap, or terms.
---

# Review a Research Program Charter

You are reviewing a charter written in the Research Program Charter format. The specs are the source of truth: `spec/charter.yaml` for the structure and rules, and one file per part in `spec/`. If this skill was copied into a program's repo, find the format directory first (look for a folder containing `spec/charter.yaml`).

Review the writing, not the research. Do not rewrite the charter. Report findings the authors can act on.

## Steps

1. **Run the lint.** `python3 <format_dir>/lint.py <charter_dir>`. Report its errors first and do not repeat them later. If it fails on missing files or sections, say so and review what exists.
2. **Read the specs for the parts that changed**, including each part's `checks` and `common_failures`. For a pull request, review only the changed parts, plus anything above or below them that the change makes inconsistent.
3. **Check each part against its own question.** Each part answers one question and must not answer the others:
   - Space: about the world, no "we". A competitor could publish it under their own name changing only the steward. Cruxes are stated neutrally, with the strongest case for and against.
   - Thesis: our side of each crux. Three to five premises, each with the result that would make us drop it. Success at the end is a thing that exists, not activity. "Why us" is evidence, not adjectives.
   - Open problems: questions, with no dates and no owners. Each says what an answer looks like and gives a first step an outsider could take. Ids are stable.
   - Roadmap: every item past research has one accountable person, an appetite, a decision date, and criteria written in advance. Dates are decision dates, not delivery estimates. Every item cites a question id or is tagged untraced.
   - Terms: someone outside the team can tell who can stop the program and on what grounds. Endings name the condition that triggers each. Someone is named to inherit the space, the open problems and the tree.
4. **Check the joins between parts.**
   - Is any sentence in the space really thesis (a peer could dispute it, or it is about our approach)? Is any sentence in the thesis really a shared belief?
   - Does each premise generate at least one open problem? Is there an open problem no premise needs?
   - Does untraced work stay within its share of the envelope, and has anything untraced survived two reviews without amending the thesis?
   - If a review note records a falsified premise, did the charter version change?
   - Were any criteria written after the result they judge?
5. **Read it three more times, briefly, as three readers.**
   - A program manager: what decision does each section change? What is missing that a sponsor needs on day one?
   - A field builder: could a stranger find where they fit and start on a question without talking to the authors?
   - An operator on the team: what here will not be kept up to date, and what could be cut?

## Gaps the authors have flagged themselves

A draft may say openly that something is undecided and belongs to the sponsor. Do not list each of those as a finding. Report them once, as a count per part, and say which of them block the charter from binding anyone. Do treat as findings any undecided item the authors could have settled themselves, such as a missing decision date on their own work.

## Output

At most ten findings, most serious first. For each: the file and section, what is wrong in one sentence, and the smallest change that would fix it. Then one line per part: fine, or needs work. Then a verdict: ready to circulate, ready after the listed fixes, ready to circulate as a proposal (the writing is sound and the open decisions belong to the sponsor), or not yet a charter.

Do not praise. Do not summarise the charter back to its authors. If something is good enough, leave it alone.
