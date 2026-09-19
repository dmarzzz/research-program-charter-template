# Program Charter: a format for R&D programs

Draft 0.2, 2026-09-19. Domain-neutral. Meant to be pulled into a program's own repo and filled in there. Called a format, not a standard, until a second organisation uses it. Revised after a three-reviewer panel: `reviews/2026-09-19-panel.md`.

## What it is

One document that describes an R&D program of any size: where it is working, what it claims, what is unknown, what it is doing, and on what terms. The format is the same at every scale; only the size guidance changes. A small team writes six pages in two days and keeps it alive in under two hours per person per month. A large program writes each part as its own document. The one-pager is the primary artifact either way; the charter is its appendix.

Five parts. Each answers one question and must not answer the others.

| Part | Question | Writes as |
|---|---|---|
| **Space** | Where? What territory, why it matters, why now | about the world, no "we" |
| **Thesis** | What do we claim can be made true here, and why us | first person, a claim a peer could dispute |
| **Open problems** | What would have to be true, and what do we not know | questions; no dates, no owners |
| **Roadmap** | In what order, by when, what are we doing now | commitments; dates, owners, tests |
| **Terms** | Under what authority, with whom, for how long, how it ends | the only part that binds anyone |

A **masthead** box on page one carries the lines an approver has to see: lead, sponsor, people with time fractions, envelope, end, next review, what is on offer to outsiders.

## How space and thesis stay apart

The space holds **shared beliefs** (most of the field accepts them) and **cruxes** (the field splits on them, stated neutrally). The thesis states **our side of each crux**, then the premises that follow, each with the result that would make us drop it. A stranger reads the cruxes to find where they stand; they read the thesis to see where we stand.

A space is adopted for what others can use in it (an arena, a benchmark, a dataset, a convening, money), not for its name. The format asks for that shared asset and does not pretend a name is enough.

## How the parts stay honest

- The **tree** lives with the open problems, as the public map with a named maintainer. The roadmap is our path through it.
- Roadmap commitments cite a question id or are tagged **untraced**. Untraced work is allowed, budgeted at about a fifth of the envelope, and has to resolve after two reviews: it amends the thesis or leaves the program.
- A falsified premise forces a new version. The thesis is revised from below as well as from above.
- There is **one review cadence**. Parts change when a result, a budget, or a departure forces them to.
- Success at the end, the baseline to beat, drop conditions, and go/no-go criteria are written **before** results exist.
- The terms say what triggers each ending, and who inherits the space, the open problems, and the tree.

## What is parked

Rungs, bet cards, evidence grades, ledgers, and generated views are optional lower-layer machinery and are not specified yet. Nothing in this format depends on them.

## The documents

Formats for each are in `DOCUMENTS.md`; blank templates are in `formats/`.

| Document | Part | Required | Length |
|---|---|---|---|
| [<Program name>: one page](formats/one_pager.md) | all | always | 1 page |
| [Opportunity Space: <name>](formats/space.md) | space | inside the charter as one page. Standalone only when a second program or an outside organisation shares the space. | 3 to 5 pages |
| [Program Thesis: <program name>](formats/thesis.md) | thesis | inside the charter at summary depth. Standalone when a funder or peer reviewer asks. | 3 to 4 pages |
| [Open Problems in <space>](formats/open_problems.md) | open_problems | the question list is required inside the charter. The standalone public document is written when there is something on offer to outsiders. | as long as the list needs; one paragraph per area, one card per question |
| [Research Roadmap: <program name>](formats/roadmap.md) | roadmap | the next-90-days table and the go/no-go criteria are required inside the charter. The standalone document is written when the sponsor or a partner needs the sequencing argument. | 2 to 3 pages plus cards |
| [Terms: <program name>](formats/terms.md) | terms | always, inside the charter. Its key lines are repeated in the masthead. | 1 to 2 pages |
| [Review note: <date>](formats/review_note.md) | all | at every review | 1 page |
| [Discovery summary: <space>](formats/discovery_summary.md) | before the charter | optional; written once, before charter v0.1 | 2 pages |
| [Closing report: <program name>](formats/closing_report.md) | after the term | at the end of the term | 3 pages |

## The spec

Source: `charter.spec.yaml`. This README is rebuilt from it by `build.py`.

### Format

```yaml
format:
  name: Program Charter
  version: "0.2"
  status: draft
```

### Size profiles

```yaml
profiles:                   # the format is the same at any scale; only the size guidance changes
  small_team:               # roughly 3 to 8 people
    week_one: "2 to 3 pages, about two person-days: one drafts, the team red-teams for 90 minutes, half a day of edits"
    full_charter: 6 pages at most
    deeper_documents: written only when a named reader asks for one
    upkeep: under two hours per person per month
  large_program:            # many teams, outside performers, a funder running a call
    full_charter: 10 to 15 pages; each part usually also exists as its own document
    deeper_documents: space, thesis, open problems and roadmap are normally all standalone
    adds: "the optional call step, technical areas under the thesis, and a separate evaluation performer"
```

### Primary artifact

```yaml
primary_artifact: the one-pager, at any scale. The charter is its appendix, not the other way round.
```

### The charter

```yaml
charter:
  masthead:                 # a box on page one; the only part an approver must read
    - program_name
    - lead
    - sponsor               # who signs it, who funds it, who can end it
    - people                # names with time fractions; in a small team this is the budget
    - envelope              # total resources, not line items
    - end                   # end date or end condition
    - next_review
    - on_offer              # what outsiders can get: funds, arena access, data, review, co-authorship. "nothing yet" is a valid answer.
    - version

  parts:
    - id: space
      question: Where? What territory is this, why does it matter, why now?
      writes_as: about the world, no "we"
      fields:
        name:             {required: true}
        definition:       {required: true, note: "what is inside and what is outside"}
        shared_beliefs:   {required: true, note: "claims about the world most of the field accepts. Keep short; these orient nobody on their own."}
        cruxes:           {required: true, note: "2 to 5 contested claims about the space, stated neutrally. This is where a stranger locates themselves."}
        why_now:          {required: true, max_items: 3}
        landscape:        {required: true, note: "who else is here, what they cover, what they left open"}
        shared_asset:     {required: false, note: "the thing others can use: an arena, a benchmark, a dataset, a convening, money. A space is adopted for its asset, not its name."}
      notes:
        - lives inside the charter. Becomes its own document only when a second program shares the space.
        - sorting heuristic, not a requirement: if a competitor would agree with a sentence, it is a shared belief; if the field splits on it, it is a crux; our side of a crux is thesis.

    - id: thesis
      question: What do we claim can be made true here, and why us?
      writes_as: first person; a claim a reasonable peer could dispute
      fields:
        goal_sentence:    {required: true, note: "plain words, one sentence"}
        simply_stated:    {required: true, max_words: 200}
        positions:        {required: true, note: "our side of each crux"}
        premises:         {required: true, min_items: 3, max_items: 5, note: "for the goal to be true, these have to be true"}
        drop_condition:   {required: true, per: premise, note: "what result would make us drop this premise. Written before work starts."}
        success_at_end:   {required: true, note: "what exists at the end of the term that does not exist now"}
        baseline:         {required: true, note: "how this is done today, and the thing we have to beat"}
        why_us:           {required: true, note: "evidence, not adjectives"}
        not_in_scope:     {required: true}
        transition:       {required: true, note: "who receives the result, and what they would need to see to accept it"}

    - id: open_problems
      question: What would have to be true, and what do we not know yet?
      writes_as: questions; no dates, no owners
      fields:
        areas:            {note: "groupings of questions. Usually one per premise, plus cross-cutting areas such as measurement and infrastructure."}
        questions:
          required: true
          min_items: 5
          each:
            id:               "stable, never renumbered, citable by outsiders"
            question:         required
            answer_looks_like: required
            status:           "open | being worked | answered | retired"
            prior_work:       optional
            skill_to_start:   optional
            who_is_on_it:     "may include outsiders"
            contact:          optional
            hazard:           "optional. Flag questions that should be sequenced defensively or not accelerated."
        tree:             {required: false, note: "the public map: questions and capabilities as nodes, requires as edges, status and who is on each node. Built by backcasting with outside experts. Needs a named maintainer."}
        contribution_path: {required: false, note: "how to claim a question, submit an answer, how the list changes in response, how credit is given"}
      publishes_as: "Open Problems in <space>"

    - id: roadmap
      question: In what order, by when, and what are we doing now?
      writes_as: commitments; dates, owners, tests
      fields:
        next_90_days:     {required: true, note: "commitments with one owner each"}
        path:             {note: "our route through the tree. The tree is the map; this is the trip."}
        go_no_go:         {required: true, note: "dated criteria, written before the results exist"}
        traced_to:        {required: true, per: commitment, note: "a question id, or the tag 'untraced'"}
        untraced_budget:  {default: "about 20% of the envelope"}
        risks:            {required: true, note: "top risks, and dependencies on teams the program does not control"}
      detail: "bet cards, rungs, evidence grades: optional, not yet specified"

    - id: terms
      question: Under what authority, with whom, for how long, and how does it end?
      writes_as: constitutional; the only part that binds anyone
      fields:
        authority:        {required: true, note: "what the program may decide on its own; who approves a version bump"}
        reporting:        {required: true, note: "what the sponsor sees, and how often"}
        openness:         {required: true, note: "what is published, what is commercial, who decides. Settle this early."}
        judging:          {required: true, note: "research continuation and product expansion are judged separately, each by its own test"}
        ending:
          required: true
          note: "conditions, not just outcomes"
          each_of: [graduate, hand_off, stop]
          states: "the condition that triggers it"
        stewardship:      {required: true, note: "who inherits the space, the open problems, and the tree when the program ends"}
        still_figuring_out: {required: true, note: "the questions about the program itself we would most like a reader to argue with"}
```

### Rules

```yaml
rules:
  - one review cadence. At each review, update the roadmap, then ask whether anything learned changes a part above it.
  - parts change when a result, a budget, or a departure forces them to. No calendars per part.
  - traceability is a check run at review, not a gate. Untraced work is allowed and labelled.
  - untraced work that survives two reviews either amends the thesis or moves out of the program.
  - a premise that is falsified forces a new charter version. The thesis is revised from below as well as from above.
  - a fact lives in one place. No summary-plus-deeper-copy of the same content.
  - criteria are written before results. Criteria written after get fitted to the results.
```

### Lifecycle

```yaml
lifecycle: [discovery, charter, running, closing]
```

### Optional steps

```yaml
optional_steps:
  call: "publishing the open problems as an invitation. Only meaningful when on_offer is not empty."
```

### Is the format working?

```yaml
format_test:                # how to know in 90 days whether this format is working
  working:
    - the file was edited at the review without anyone chasing
    - each person can name the question their current work answers
    - it killed or reordered at least one thing
    - an outsider cited a question id
    - upkeep stayed under two hours per person per month
  failed: a slide deck has become the real plan
```

