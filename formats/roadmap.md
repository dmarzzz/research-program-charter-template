# Research Roadmap: <program name>

> Research Program Charter format `roadmap` (spec: `spec/roadmap.yaml`). Reader: the team, the sponsor, close partners. Updated: at every review.
> Delete these guidance lines as you fill the sections in.

## 1. Path

> Our route through the tree: which nodes, in what order, and why this order.


## 2. Horizons

> This quarter, this year, longer: what we expect to be true at each.


## 3. Next 90 days  *(required in the charter)*

> Table of commitments: what, owner, traced to, test, date.


## 4. Go / no-go  *(required in the charter)*

> Dated criteria written before results exist, and the decision each one unlocks.


## 5. Untraced work

> Register: what, why, share of envelope used, number of reviews survived.


## 6. Risks and dependencies  *(required in the charter)*

> Top risks. Dependencies on teams the program does not control.


## 7. Parking lot

> What we are deliberately not doing now, so nobody has to ask.


### Commitment card (copy per item)

```yaml
id:    # short
statement:    # By DATE we will see Y, measured by M against baseline B.
owner:    # exactly one
traced_to:    # a question id, or 'untraced'
test:    # the check that decides it
judged_by:    # continuation (research) | kill rule (product, arena)
status:    # proposed | active | passed | stopped
heavier_form:    # an optional fuller bet card, not yet specified
```

---

Checks before it goes out:

- [ ] every commitment has one owner, a date, and a test
- [ ] every commitment cites a question id or is tagged untraced
- [ ] untraced work is within its share of the envelope
