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

## License

MIT. See [LICENSE](LICENSE).
