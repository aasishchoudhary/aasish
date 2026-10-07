# Trustworthy Execution Standard

A portfolio is trustworthy when a reviewer can inspect how a claim was produced.

## Required evidence

### Level 0 — Claim
A statement about what the project is intended to do.

### Level 1 — Specification
Interfaces, assumptions, inputs, expected outputs and constraints are documented.

### Level 2 — Implementation
Runnable source code exists.

### Level 3 — Reproducible test
A fresh environment can execute tests against deterministic fixtures.

### Level 4 — Measurement
Performance, accuracy, reliability, latency, cost or other metrics are measured using a declared method.

### Level 5 — Real-world validation
The system has been used against a real workload with evidence that can be disclosed safely.

Do not label an L2 prototype as production. Do not publish numbers without a reproducible measurement method.

## Client trust checklist

Before presenting a project, verify:

- README explains the problem within seconds.
- Architecture is visible.
- Setup works from a clean environment.
- Tests cover important failure modes.
- Secrets are absent.
- Logs do not expose private data.
- Limitations are explicit.
- Evidence can be inspected.
- Claims match implementation status.

## Execution record

For meaningful runs, record:

```text
run_id
timestamp
input
expected outcome
actual outcome
tools used
validation result
failure / recovery
environment
next action
```

This makes the work auditable instead of purely promotional.
