# Program Charter: the documents and their formats

Generated from `documents.spec.yaml` by `build.py`. Each part of the charter can be written at summary depth inside the charter, or as its own document in the format below. Only the one-pager, the charter itself, and the review note are always required. Everything else is written when a named reader asks for it.

| Document | Reader | Length | Updated |
|---|---|---|---|
| **<Program name>: one page** | anyone; the primary artifact | 1 page | at every review |
| **Opportunity Space: <name>** | the field, including competitors | 3 to 5 pages | when the landscape or a crux moves |
| **Program Thesis: <program name>** | funders, peers, prospective collaborators | 3 to 4 pages | on a version bump; a falsified premise forces one |
| **Open Problems in <space>** | outside researchers and builders | as long as the list needs; one paragraph per area, one card per question | at every review; ids are never renumbered or reused |
| **Research Roadmap: <program name>** | the team, the sponsor, close partners | 2 to 3 pages plus cards | at every review |
| **Terms: <program name>** | the sponsor and the team | 1 to 2 pages | rarely; by the amendment rule it contains |
| **Review note: <date>** | the team and the sponsor | 1 page | never; it is a record |
| **Discovery summary: <space>** | whoever will draft the thesis | 2 pages | never |
| **Closing report: <program name>** | the sponsor, the steward, the field | 3 pages | never |

## <Program name>: one page

Part: all. Required: always

| # | Section | What goes in it |
|---|---|---|
| 1 | Masthead | Box. Lead, sponsor, people with time fractions, envelope, end, next review, what is on offer, version. |
| 2 | Goal | The goal sentence, in plain words. |
| 3 | The space in three lines | Name. What is inside and outside. Why now. |
| 4 | Where we stand | Our side of each crux, one line each. |
| 5 | What has to be true | Three to five premises, one line each, each ending with the result that would make us drop it. |
| 6 | What exists at the end | What will exist that does not exist now, next to the baseline it has to beat. |
| 7 | Next 90 days | Three commitments with an owner and a date. |
| 8 | The ask and the offer | What we need from the reader. What the reader can get from us. |

**Checks before it goes out**

- a stranger can say back the goal and one premise after two minutes
- no adjective without a number or a source
- fits on one page without shrinking the type

**How it usually goes wrong**

- a mission statement where the goal sentence should be
- premises that could not be false

Blank template: `formats/one_pager.md`

## Opportunity Space: <name>

Part: space. Required: inside the charter as one page. Standalone only when a second program or an outside organisation shares the space.

| # | Section | What goes in it |
|---|---|---|
| 1 | Name and boundary | The name. What is inside, what is outside, which neighbouring spaces it touches. |
| 2 | Why it matters | Who gains or loses what if this space develops well or badly. Magnitudes with sources. |
| 3 | Why now | Three trends at most. Each with the evidence that it is real. |
| 4 | Shared beliefs | Short list of claims most of the field accepts. Keep it short; these orient nobody on their own. |
| 5 | Cruxes | Two to five contested claims, stated neutrally. For each: the claim, the strongest case for, the strongest case against, and what evidence would move it. |
| 6 | Landscape | Table: who is here, what they cover, what they left open, how their work and ours connect. |
| 7 | Shared assets | What others can use today: an arena, a benchmark, a dataset, a convening, money. How to get access. |
| 8 | Seeds | Questions in the space that sit outside any program. Small, exploratory, unowned. |
| 9 | Steward and citation | Who maintains this document, how to cite it, version. |

**Checks before it goes out**

- no "we" outside the shared assets and steward sections
- each crux names someone who holds each side, or cites them
- a competitor could publish it under their own name changing only the steward

**How it usually goes wrong**

- beliefs everyone accepts presented as insight
- our thesis smuggled in as a fact about the world
- a landscape that lists nobody doing better work than us

Blank template: `formats/space.md`

## Program Thesis: <program name>

Part: thesis. Required: inside the charter at summary depth. Standalone when a funder or peer reviewer asks.

| # | Section | What goes in it |
|---|---|---|
| 1 | Simply stated | 200 words, no jargon. Ends with what is not in scope. |
| 2 | Worked example | One concrete case, carried through the rest of the document and the open problems. |
| 3 | Positions | Our side of each crux in the space, and why. |
| 4 | Premises | For the goal to be true, these have to be true. For each: the statement, why we believe it, the result that would make us drop it, and the area of open problems it generates. |
| 5 | Success at the end | What exists at the end of the term that does not exist now, and how anyone would check. |
| 6 | Baseline | How this is done today, by whom, and the thing we have to beat. |
| 7 | Why us | Evidence, not adjectives. |
| 8 | Not in scope | What a reader might assume we are doing and we are not. |
| 9 | Transition | Who receives the result, and what they would need to see to accept it. |
| 10 | What we are still trying to figure out | The questions about the program itself we would most like a reader to argue with. |
| 11 | Update log | Version, date, what changed and why. |

**Checks before it goes out**

- a reasonable peer could disagree with every position
- every premise has a drop condition written before the work started
- covers the classic questions: what are you trying to do, how is it done today, what is new, who cares, what are the risks, what are the exams (cost and time live in the terms and the roadmap)

**How it usually goes wrong**

- premises that are restatements of the goal
- the why-us section made of credentials instead of results
- success at the end described as activity instead of a thing that exists

Blank template: `formats/thesis.md`

## Open Problems in <space>

Part: open_problems. Required: the question list is required inside the charter. The standalone public document is written when there is something on offer to outsiders.

| # | Section | What goes in it |
|---|---|---|
| 1 | How to use this document | What is on offer, how to claim a question, who to contact. |
| 2 | The map | The tree as a figure: questions and capabilities as nodes, requires as edges, status and who is on each node. |
| 3 | Areas | One paragraph each: the input, the output, which premise it serves, or that it is cross-cutting. |
| 4 | Questions | One card per question, grouped by area. Format below. |
| 5 | Hazards | Questions that should be sequenced defensively or not accelerated, and why. |
| 6 | Contributing and credit | How an answer is submitted, how the list changes in response, how credit is given. |
| 7 | Change log | Questions added, answered, retired. Dates. |

**Checks before it goes out**

- an outsider can pick a question and know the first step without talking to us
- every question says what an answer looks like
- the tree names its maintainer and its last review date

**How it usually goes wrong**

- questions only we could work on
- a tree with no external nodes
- renumbering after a reorganisation

**Sub-format: question card**

```yaml
question_card:
  id:                 stable, never renumbered
  question:           one sentence
  serves:             the premise or area it belongs to
  answer_looks_like:  what would count as an answer
  first_step:         the smallest useful contribution
  status:             open | being worked | answered | retired
  prior_work:         links
  skill_to_start:     what someone needs to know
  who_is_on_it:       names, may include outsiders
  contact:            optional
  hazard:             optional
```

**Sub-format: tree**

```yaml
tree:
  maintainer:  a named person
  built_by:    backcasting from the end state with outside experts
  nodes:       {id, kind: question | capability | external, label, area, status, who}
  edges:       {from, to, kind: requires}
  reviewed:    date
```

Blank template: `formats/open_problems.md`

## Research Roadmap: <program name>

Part: roadmap. Required: the next-90-days table and the go/no-go criteria are required inside the charter. The standalone document is written when the sponsor or a partner needs the sequencing argument.

| # | Section | What goes in it |
|---|---|---|
| 1 | Path | Our route through the tree: which nodes, in what order, and why this order. |
| 2 | Horizons | This quarter, this year, longer: what we expect to be true at each. |
| 3 | Next 90 days | Table of commitments: what, owner, traced to, test, date. |
| 4 | Go / no-go | Dated criteria written before results exist, and the decision each one unlocks. |
| 5 | Untraced work | Register: what, why, share of envelope used, number of reviews survived. |
| 6 | Risks and dependencies | Top risks. Dependencies on teams the program does not control. |
| 7 | Parking lot | What we are deliberately not doing now, so nobody has to ask. |

**Checks before it goes out**

- every commitment has one owner, a date, and a test
- every commitment cites a question id or is tagged untraced
- untraced work is within its share of the envelope

**How it usually goes wrong**

- a list of activities with no tests
- criteria written after the result
- a path that is just the order things were started

**Sub-format: commitment card**

```yaml
commitment_card:
  id:            short
  statement:     By DATE we will see Y, measured by M against baseline B.
  owner:         exactly one
  traced_to:     a question id, or 'untraced'
  test:          the check that decides it
  judged_by:     continuation (research) | kill rule (product, arena)
  status:        proposed | active | passed | stopped
  heavier_form:  an optional fuller bet card, not yet specified
```

Blank template: `formats/roadmap.md`

## Terms: <program name>

Part: terms. Required: always, inside the charter. Its key lines are repeated in the masthead.

| # | Section | What goes in it |
|---|---|---|
| 1 | Purpose | One sentence. Points to the thesis. |
| 2 | Sponsor and authority | Who signs, who funds, who can end it. What the program may decide on its own. Who approves a version bump. |
| 3 | People | Names, roles, time fractions. Investigators named against questions where that is real. |
| 4 | Envelope | Total resources, not line items. The share reserved for untraced work. |
| 5 | Term and review | Start, end date or end condition, the one review cadence. |
| 6 | Reporting | What the sponsor sees, and how often. |
| 7 | Openness | What is published, what is commercial, who decides, and the default when nobody has decided. |
| 8 | Judging | How research continuation is judged. How product expansion is judged. Kept separate. |
| 9 | Endings | Graduate, hand off, stop: the condition that triggers each. |
| 10 | Stewardship | Who inherits the space, the open problems, and the tree when the program ends. |
| 11 | Amendments | How the charter changes, and what forces a new version. |
| 12 | Signed | Names and date. |

**Checks before it goes out**

- someone outside the team can tell who can stop the program and on what grounds
- time fractions add up to the people actually available

**How it usually goes wrong**

- authority described as consensus
- an end condition nobody could observe

Blank template: `formats/terms.md`

## Review note: <date>

Part: all. Required: at every review

| # | Section | What goes in it |
|---|---|---|
| 1 | What we learned | Results since the last review, each with its evidence. |
| 2 | Commitments | Met, missed, changed. One line each. |
| 3 | Go / no-go decisions taken | Which criteria came due and what was decided. |
| 4 | Does anything change a part above? | Space, thesis, open problems: yes or no for each, and what. A falsified premise is recorded here. |
| 5 | Untraced work | New, resolved, and ageing. Anything at its second review gets resolved now. |
| 6 | Next | Decisions, owners, next review date, whether the version bumps. |

**Checks before it goes out**

- took under 90 minutes
- the "change a part above" question was answered explicitly for each part

**How it usually goes wrong**

- a status update with no decisions

Blank template: `formats/review_note.md`

## Discovery summary: <space>

Part: before the charter. Required: optional; written once, before charter v0.1

| # | Section | What goes in it |
|---|---|---|
| 1 | What we tried | Workshops, short projects, prototypes, conversations. |
| 2 | What exists | Artifacts with links and an honest grade for each. |
| 3 | What surprised us | The results nobody predicted. |
| 4 | Cruxes it surfaced | Disagreements that turned out to matter. These seed the space. |
| 5 | Toward a thesis | The claim the evidence now supports, and what it still does not. |

**Checks before it goes out**

- at least one surprise is recorded

**How it usually goes wrong**

- a list of events with no findings

Blank template: `formats/discovery_summary.md`

## Closing report: <program name>

Part: after the term. Required: at the end of the term

| # | Section | What goes in it |
|---|---|---|
| 1 | What exists now | Against the success-at-end statement and the baseline. |
| 2 | Premises | Held, dropped, or still open. With the evidence. |
| 3 | Questions | Answered, opened, retired. |
| 4 | Handover | What goes to whom: results, the space, the open problems, the tree. |
| 5 | Which ending | Graduate, hand off, or stop, and the condition that triggered it. |
| 6 | What we would do differently | About the work, and about this format. |

**Checks before it goes out**

- a named steward has accepted the handover

**How it usually goes wrong**

- a success story with no dropped premises

Blank template: `formats/closing_report.md`

