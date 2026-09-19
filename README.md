# Research Program Charter

A format for describing a research program: where it is working, what it claims, what is unknown, what it is doing, and on what terms. Domain-neutral. Draft 0.3.

## Structure

A charter is a masthead plus five parts. The parts run from the most stable to the most volatile. Each answers one question and must not answer the others.

| Part | Question it answers | Spec | Template |
|---|---|---|---|
| **Space** | Where? What territory, why it matters, why now | [spec/space.yaml](spec/space.yaml) | [formats/space.md](formats/space.md) |
| **Thesis** | What do we claim can be made true here, and why us | [spec/thesis.yaml](spec/thesis.yaml) | [formats/thesis.md](formats/thesis.md) |
| **Open problems** | What would have to be true, and what do we not know | [spec/open-problems.yaml](spec/open-problems.yaml) | [formats/open_problems.md](formats/open_problems.md) |
| **Roadmap** | In what order, by when, what are we doing now | [spec/roadmap.yaml](spec/roadmap.yaml) | [formats/roadmap.md](formats/roadmap.md) |
| **Terms** | Under what authority, with whom, for how long, how it ends | [spec/terms.yaml](spec/terms.yaml) | [formats/terms.md](formats/terms.md) |

The masthead, the order of the parts, the rules, and the lifecycle are in [spec/charter.yaml](spec/charter.yaml).

Each part can be written at summary depth inside the charter, or as its own document. Sections marked `required: true` in a part's spec must exist inside the charter either way.

## Supporting documents

| Document | When | Spec | Template |
|---|---|---|---|
| **One-pager** | always; the primary artifact | [spec/one-pager.yaml](spec/one-pager.yaml) | [formats/one_pager.md](formats/one_pager.md) |
| **Review note** | at every review | [spec/review-note.yaml](spec/review-note.yaml) | [formats/review_note.md](formats/review_note.md) |
| **Discovery summary** | optional; once, before the first charter | [spec/discovery-summary.yaml](spec/discovery-summary.yaml) | [formats/discovery_summary.md](formats/discovery_summary.md) |
| **Closing report** | at the end of the term | [spec/closing-report.yaml](spec/closing-report.yaml) | [formats/closing_report.md](formats/closing_report.md) |

## How the parts relate

```
Space            the territory: shared beliefs, cruxes, landscape, shared assets
  └─ Thesis      our side of each crux; premises, each with the result that would make us drop it
      └─ Open problems   what is unknown; stable question ids; the tree as the public map
          └─ Roadmap     our path through the tree; commitments with owners, dates and tests
Terms            sponsor and authority, people, envelope, openness, endings, stewardship
```

A program ends. A space does not. The space lives inside the charter until a second program shares it.

## Using it

1. Copy the templates you need from `formats/` into your program's repo and fill them in. Start with the one-pager.
2. Hold one review cadence. Write a review note each time, and ask whether anything learned changes a part above the roadmap.
3. Read [GUIDANCE.md](GUIDANCE.md) for how much to write and how to tell whether the format is working.

The specs in `spec/` are the source. `python3 build.py` regenerates the templates in `formats/`.

## History

[reviews/2026-09-19-panel.md](reviews/2026-09-19-panel.md) records the review that shaped the current version.
