# Research Roadmap: <program name>

> Research Program Charter format `roadmap` (spec: `spec/roadmap.yaml`). Reader: the team, the sponsor, close partners, and anyone trying to find where their work fits. Updated: at every review, and immediately when something changes stage.
> Goal: One place where anyone can see, in thirty seconds, what the program is working on, what stage each thing is in, how the pieces connect, and when each will next be decided. If it exists, is roughly right, and people can find it, it is doing its job.
> Delete these guidance lines as you fill the sections in.

## 1. The map  *(required in the charter)*

> The tree with each node marked by stage. The thirty-second overview; look here first. Our path through it: which nodes, in what order, and why this order.


## 2. Stages and gates

> The stages items move through and what it takes to pass each gate. Use the default ladder below or define your own.


## 3. Items  *(required in the charter)*

> Table of what is being worked on: name, stage, traced to, appetite, decision date, accountable person, last updated.


## 4. Decisions due  *(required in the charter)*

> The decision dates coming up, the criteria written in advance, and the default if they are not met.


## 5. Horizons

> This quarter, this year, longer: what we expect to be true at each.


## 6. Untraced work

> Register: what, why, share of envelope used, number of reviews survived.


## 7. Risks and dependencies  *(required in the charter)*

> Top risks. Dependencies on teams the program does not control.


## 8. Parking lot

> What we are deliberately not doing now, so nobody has to ask.


## 9. Naming registry

> The canonical name for each thing, so teammates and partners hear the same words for the same things.


## 10. Stage log

> When things moved stage, and why.


### Default stage ladder (copy per item)

```yaml
research:    # problem identified, no concrete solution. No owner required, no commitment. Gate out: a concrete hypothesis and an experiment plan with success and failure criteria and a review date.
proof_of_concept:    # short, fixed appetite. One accountable person, an experiment plan, success criteria, a decision date. Gate out: a working demonstration validated against the criteria, and a description written down.
transitioning:    # being handed to whoever will use it. Appetite defined, a name registered, the receiving party named. Gate out: in use by at least one outside party.
in_use:    # serving real users. Measures defined, an owner maintains the entry.
maintenance:    # no active development. Within a fixed window: assign an owner, hand over, or sunset.
```

### Item (copy per item)

```yaml
name:    # canonical, from the naming registry
stage:    # one of the program's stages
traced_to:    # a question id, or 'untraced'
statement:    # By DATE we will see Y, measured by M against baseline B.
appetite:    # time and resource we are willing to spend at this stage
decision_date:    # when it is judged
default_if_missed:    # dropped, returned to research, or re-scoped
success_criteria:    # written before the work starts
accountable:    # exactly one person, from proof of concept on
judged_by:    # continuation (research) | kill rule (product, arena)
last_updated:    # date
```

---

Checks before it goes out:

- [ ] someone new can find where their work sits on the map in thirty seconds
- [ ] every item past research has one accountable person, an appetite, a decision date, and criteria written in advance
- [ ] every item cites a question id or is tagged untraced
- [ ] nothing is older than the staleness window
