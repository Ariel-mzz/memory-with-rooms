# Memory With Rooms

A layered memory system for OpenClaw agents that separates raw drafts from curated recall.

This project is for agents that need to remember well **without** letting every scratch note, planning trace, or unfinished thought dominate later retrieval.

## Why this exists

Many agent memory setups become noisy over time:

- raw process notes pollute normal recall
- long-term conclusions get buried under drafts
- relationships, preferences, and open questions end up mixed together
- dreaming or palace/wiki layers ingest too much raw material

Memory With Rooms solves that by splitting memory into distinct rooms with different roles.

## Core idea

Treat memory as rooms, not one undifferentiated archive.

- **Draft room**: raw thinking, unfinished notes, temporary process
- **Reflection room**: concise notes worth retrieving later
- **Relationship room**: durable observations about people and collaboration
- **Preference room**: recurring tastes, curiosities, and working style
- **Open questions room**: unresolved tensions and themes worth revisiting

The goal is not to store less. The goal is to make later recall cleaner.

## What this project includes

- A reusable skill: [SKILL.md](./SKILL.md)
- Reference docs for architecture and adoption
- Small utility scripts for auditing and registry generation
- Templates for durable memory files
- A fully sanitized demo workspace

## Directory structure

```text
memory-with-rooms/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── MEMORY.template.md
│   ├── OPEN-QUESTIONS.template.md
│   ├── ROOM-REGISTRY.template.md
│   └── demo-workspace/
├── references/
│   ├── architecture.md
│   ├── adaptation-guide.md
│   ├── adoption-guide.md
│   └── dreaming-and-palace.md
└── scripts/
    ├── build_registry.py
    ├── check_memory_layout.py
    ├── check_room_registry.py
    └── smoke_test.py
```

## Quick start

### 1. Read the skill

Start with [SKILL.md](./SKILL.md) for the workflow and operating rules.

### 2. Inspect the demo

Look at [assets/demo-workspace](./assets/demo-workspace) to see a minimal layered memory layout:

- `memory/drafts/`
- `memory/reflections/`
- `memory/relationships/`
- `memory/preferences/`
- `memory/open-questions/`
- `memory/system/`

### 3. Run the smoke test

```powershell
py -3 .\scripts\smoke_test.py
```

This checks the demo workspace with the included audit scripts.

### 4. Adapt to your own workspace

For an existing OpenClaw workspace, read:

- [references/adoption-guide.md](./references/adoption-guide.md)
- [references/dreaming-and-palace.md](./references/dreaming-and-palace.md)

## Scripts

### `check_memory_layout.py`

Audit whether a workspace has the expected room structure and whether curated rooms are empty.

```powershell
py -3 .\scripts\check_memory_layout.py C:\path\to\workspace
```

### `check_room_registry.py`

Validate a room registry and warn if draft paths also appear as curated or palace sources.

```powershell
py -3 .\scripts\check_room_registry.py C:\path\to\room-registry.md
```

### `build_registry.py`

Generate a simple markdown registry describing draft, curated, and palace source paths.

```powershell
py -3 .\scripts\build_registry.py `
  --workspace C:\path\to\workspace `
  --draft memory/drafts/ `
  --curated memory/reflections/ `
  --curated memory/relationships/ `
  --curated memory/preferences/ `
  --curated memory/open-questions/ `
  --palace memory/reflections/ `
  --palace memory/relationships/ `
  --palace memory/preferences/ `
  --palace memory/open-questions/
```

## Recommended adoption path

If you already have a working OpenClaw memory setup, do **not** migrate everything at once.

Start small:

1. keep the current system
2. add `memory/drafts/`
3. add `memory/reflections/`
4. create a room registry
5. let normal retrieval gradually prefer curated rooms

This project is designed for additive adoption, not destructive replacement.

## Dreaming and palace guidance

Memory With Rooms works best when:

- raw drafts are preserved but not preferred for normal recall
- curated rooms feed higher-level memory layers first
- dreaming is treated as an auxiliary summarization process
- palace/wiki layers organize cleaned memory instead of ingesting every raw trace

See [references/dreaming-and-palace.md](./references/dreaming-and-palace.md).

## Status

This repository is currently an **early public version**.

The structure, templates, and scripts are usable now, but the project is still intended to evolve through real-world OpenClaw use.

## Privacy note

This repository was extracted from a real layered agent memory workflow, but all personal content, private relationship material, tokens, and live memory data were intentionally removed or sanitized before publication.
