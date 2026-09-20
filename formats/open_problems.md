# Open Problems in <space>

> Research Program Charter format `open_problems` (spec: `spec/open-problems.yaml`). Reader: outside researchers and builders. Updated: at every review; ids are never renumbered or reused.
> Delete these guidance lines as you fill the sections in.

## 1. How to use this document

> What is on offer, how to claim a question, who to contact.


## 2. The map

> The tree as a figure: questions and capabilities as nodes, requires as edges, status and who is on each node.


## 3. Areas

> One paragraph each: the input, the output, which premise it serves, or that it is cross-cutting.


## 4. Questions  *(required in the charter)*

> One card per question, grouped by area. Format below.


## 5. Hazards

> Questions that should be sequenced defensively or not accelerated, and why.


## 6. Contributing and credit

> How an answer is submitted, how the list changes in response, how credit is given.


## 7. Change log

> Questions added, answered, retired. Dates.


### Question card (copy per item)

```yaml
id:    # Q<number>, for example Q7. Stable: never renumbered, never reused.
question:    # one sentence
serves:    # the premise or area it belongs to
answer_looks_like:    # what would count as an answer
first_step:    # the smallest useful contribution
status:    # open | being worked | answered | retired
prior_work:    # links
skill_to_start:    # what someone needs to know
who_is_on_it:    # names, may include outsiders
contact:    # optional
hazard:    # optional
```

### Tree (copy per item)

```yaml
maintainer:    # a named person
built_by:    # backcasting from the end state with outside experts
nodes:    # {id, kind: question | capability | external, label, area, status, who}
edges:    # {from, to, kind: requires}
reviewed:    # date
```

---

Checks before it goes out:

- [ ] an outsider can pick a question and know the first step without talking to us
- [ ] every question says what an answer looks like
- [ ] the tree names its maintainer and its last review date
