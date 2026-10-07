# Aasish FX — AI Automation Engine

**Provider-neutral reference architecture for reliable AI workflow automation.**

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) [![Tests](https://img.shields.io/badge/Tests-Pytest-0A9EDC?style=for-the-badge)](#testing) [![Status](https://img.shields.io/badge/Status-Prototype-8B5CF6?style=for-the-badge)](#project-status)

## Why this exists

An LLM by itself is not an automation system. A useful system needs **control, validation, tools, state, observability and evaluation** around the model.

This project demonstrates that boundary without requiring a specific model provider or API key.

## Architecture

```
USER / EVENT
     |
     v
  VALIDATOR
     |
     v
 ORCHESTRATOR
   /       \
 MODEL     TOOLS
 ADAPTER    |
   \       /
    \     /
   VALIDATOR
       |
       v
 EVIDENCE / TELEMETRY
```

> **Probabilistic reasoning should not silently own irreversible authority.**

The model can propose. Deterministic application code validates and controls what happens next.

## Design principles

- **Provider neutral** — the core does not depend on one AI vendor.
- **Deterministic control** — validation, policy, schemas and state transitions live in application code.
- **Evidence first** — executions should leave enough information to reconstruct what happened.
- **Human approval boundaries** — destructive, financial, security-sensitive or production-impacting actions need explicit gates.
- **Evaluation before scale** — small reproducible tests beat large unmeasured demos.

## Repository structure

```
src/
  core/
    models.py
    policy.py
    orchestrator.py
  adapters/
    model.py
  tools/
    calculator.py
  telemetry/
    events.py

tests/
examples/
docs/
.github/workflows/ci.yml
```

## Quick start

```bash
git clone https://github.com/aasishchoudhary/aasish.git
cd aasish
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
python examples/basic_run.py
```

No API key is required for the deterministic demo and tests.

## Testing

The first evaluation layer checks:

| Area | Question |
|---|---|
| Policy | Can unsafe actions be rejected? |
| Tools | Are inputs validated? |
| Orchestration | Are state transitions predictable? |
| Telemetry | Can an execution be reconstructed? |
| Regression | Do changes preserve expected behaviour? |

Actual performance metrics will only be published after reproducible measurements exist.

## Security

**Never commit API keys, tokens, passwords or private client data.**

See [docs/SECURITY.md](docs/SECURITY.md).

The architecture separates model reasoning, deterministic policy, tool execution and evidence to reduce the blast radius of model mistakes.

## Project status

**L2 — Prototype / Engineering Foundation**

This repository demonstrates architecture and deterministic execution controls. It does **not** claim production readiness, autonomous general intelligence or guaranteed model accuracy.

## Roadmap

- [x] Provider-neutral model boundary
- [x] Policy layer
- [x] Safe deterministic tool
- [x] Structured telemetry
- [x] Unit tests
- [x] CI
- [ ] Pluggable real model adapter
- [ ] Persistent execution store
- [ ] Evaluation dataset
- [ ] Failure replay
- [ ] Web/API interface
- [ ] Deployment example

## Engineering philosophy

```
CLAIM
  |
IMPLEMENT
  |
TEST
  |
MEASURE
  |
DOCUMENT LIMITATIONS
  |
ITERATE
```

**Build it. Instrument it. Test it. Understand it.**

— **Aasish FX**
