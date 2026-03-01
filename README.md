# Mirror_surface

> **MirrorNode** — User-facing surface layer

![CI](https://github.com/mirrornode/Mirror_surface/actions/workflows/blank.yml/badge.svg)

---

## Overview

`Mirror_surface` is the user-facing interface layer of the **MirrorNode** distributed AI system. It serves as the outermost membrane — the point where human interaction meets the orchestration layer beneath.

MirrorNode is a distributed AI architecture consisting of:
- **Mirror_surface** (this repo) — UI layer, surface routes, agent interaction endpoints
- **Enoch** — Core reasoning agent (integration pending)
- **Osiris CLI** — Command-line orchestration tool
- **Ray cluster** — Distributed compute backbone

---

## Architecture

```
[ User / Client ]
       |
       v
[ Mirror_surface ]  <-- You are here
       |
       v
[ Enoch Agent ]  (pending integration)
       |
       v
[ Ray Cluster / MirrorNode Core ]
```

---

## Getting Started

### Prerequisites
- Python 3.11+
- pip

### Install

```bash
git clone https://github.com/mirrornode/Mirror_surface.git
cd Mirror_surface
pip install -r requirements.txt
```

### Run

```bash
# Surface layer entrypoint (coming soon)
python main.py
```

---

## CI/CD

This repo uses GitHub Actions for continuous integration:

| Job | Description |
|-----|-------------|
| `lint-and-test` | Flake8 linting + pytest on Python 3.11 |
| `health-check` | YAML validation + Enoch integration readiness check |

Workflow triggers on push and pull requests to `main` and `develop`.

---

## Enoch Integration

The Enoch agent module is currently in development. When ready, it will be wired into the surface layer via:

```
enoch/stub.py  →  enoch/agent.py  →  MirrorNode core
```

The CI pipeline already monitors for the integration stub (`enoch/stub.py`) and will report readiness automatically.

---

## Contributing

This is an active internal project. Maintained by [@mirrornode](https://github.com/mirrornode).

---

*Part of the MirrorNode distributed AI system.*
