# Research Program Charter

A format for describing a research program: where it is working, what it claims, what is unknown, what it is doing, and on what terms. Domain-neutral. Draft 0.3.

## Structure

A charter is a masthead plus five parts. The parts run from the most stable to the most volatile. Each answers one question and must not answer the others.

| Part | Question it answers | Spec | Template |
|---|---|---|---|
| **Space** | Where? What territory, why it matters, why now | [spec/space.yaml](spec/space.yaml) | [formats/space.md](formats/space.md) |
| **Thesis** | What do we claim can be made true here, and why us | [spec/thesis.yaml](spec/thesis.yaml) | [formats/thesis.md](formats/thesis.md) |
| **Open problems** | What do we not know yet that stands between the premises and the goal | [spec/open-problems.yaml](spec/open-problems.yaml) | [formats/open_problems.md](formats/open_problems.md) |
| **Roadmap** | What is being worked on, at what stage, how it connects, and when each thing is next decided | [spec/roadmap.yaml](spec/roadmap.yaml) | [formats/roadmap.md](formats/roadmap.md) |
| **Terms** | Under what authority, with whom, for how long, how it ends | [spec/terms.yaml](spec/terms.yaml) | [formats/terms.md](formats/terms.md) |

The masthead, the order of the parts, the rules, and the lifecycle are in [spec/charter.yaml](spec/charter.yaml).

Each part can be written at summary depth inside the charter, or as its own document. Sections marked `required: true` in a part's spec must exist inside the charter either way.

## Checking and sharing a charter

- `python3 lint.py path/to/charter` checks structure: required files and sections, leftover template guidance, question ids, and that every roadmap item traces to a question or is tagged untraced. An example workflow for running it on pull requests is in [ci/charter-lint.example.yml](ci/charter-lint.example.yml).
- `python3 render.py path/to/charter -o index.html` builds one self-contained HTML page from the markdown: question and item cards, and the tree as inline SVG when Playwright is available at build time.
- [.claude/skills/review-charter](.claude/skills/review-charter/SKILL.md) is a Claude Code skill that reviews the writing against each part's checks and common failures.

## License

MIT. See [LICENSE](LICENSE).
