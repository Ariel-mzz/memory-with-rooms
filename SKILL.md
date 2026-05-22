---
name: memory-with-rooms
description: Build or refine a layered memory system for an agent when recall is noisy, drafts are polluting retrieval, or long-term context needs clean separation between raw notes, curated reflections, relationships, preferences, and open questions.
---

# Memory With Rooms

Use this skill when an agent needs a memory system that remembers well without becoming messy.

This skill is for additive memory design, not destructive migration. It helps split memory into layers so the agent can keep raw process notes without letting those notes dominate retrieval later.

The larger goal is to help an OpenClaw agent become more continuous over time: not just remembering tasks, but accumulating cleaner durable context around personality, projects, relationships, preferences, and self-reflection.

## Use this skill when

- The agent remembers too much raw process and not enough settled conclusions.
- `memory_search` returns noisy drafts instead of the notes that should matter.
- The user wants separate places for work notes, curated reflections, relationships, preferences, or unresolved questions.
- A dreaming, diary, or memory-palace layer exists and needs cleaner sources.
- You need to audit an existing memory system without breaking it.

## Safety rules

- Preserve active memory systems by default.
- Do not rewrite or delete existing `MEMORY.md`, `memory/`, `.dreams/`, dream reports, palace files, or user journals unless the user explicitly asks.
- Prefer side-by-side extraction: create new curated files, registries, or mirrors instead of mutating live memory content.
- Keep private relationship content out of public templates and examples.

## Core model

Treat memory as rooms with different purposes.

1. Draft room: raw thinking, incomplete notes, temporary process.
2. Reflection room: concise notes worth retrieving later.
3. Relationship room: durable facts and observations about people.
4. Preference room: stable tastes, recurring interests, style, working rhythms.
5. Open questions room: unresolved tensions, hypotheses, things the agent wants to revisit.

The rule is simple:

- Drafts may exist in full.
- Curated rooms are what normal retrieval should prefer.
- Memory palace or wiki layers should ingest curated rooms first, not drafts.

## Workflow

### 1. Audit the current system

Check:

- which files are already authoritative
- whether `memory_search` / `memory_get` exist
- whether dreaming is active
- whether a compiled wiki or palace layer exists
- where raw notes live today
- where the user actually wants durable recall to come from

If the user already has a working system, document it before adding anything.

### 2. Classify memory into layers

Start by sorting existing content into two buckets:

- raw process
- curated recall

Then split curated recall further if useful:

- reflections
- relationships
- preferences
- open questions

If a file mixes everything together, do not immediately rewrite it. First record what it should become.

### 3. Establish room structure

Use a conservative layout such as:

```text
workspace/
├── MEMORY.md
└── memory/
    ├── drafts/
    ├── reflections/
    ├── relationships/
    ├── preferences/
    ├── open-questions/
    ├── logs/
    └── system/
```

The exact names can vary. The important part is that draft content and curated content stop sharing the same retrieval role.

### 4. Add a registry before adding automation

Before building mirrors, wiki pages, or sync jobs, create a small registry that states:

- which folders are draft-only
- which folders feed retrieval
- which folders feed palace/wiki layers
- which files are append-only

Use `scripts/build_registry.py` for a starter registry.

### 5. Add retrieval rules

Prefer these retrieval rules:

- normal recall should search curated rooms first
- draft rooms should be searched only when the user explicitly wants process history
- relationship and preference rooms should be easy to surface for long-running agents
- open questions should remain visible without pretending to be resolved knowledge

### 6. Connect optional higher layers carefully

If the system uses dreaming, palace, or wiki layers:

- let those layers ingest curated rooms first
- only allow draft ingestion intentionally
- never assume “more indexed text” means “better memory”

### 7. Verify behavior

Check whether the agent can answer:

- what it concluded
- what it still has not resolved
- what it prefers
- who matters

without pulling raw scratch notes every time.

Use `scripts/check_memory_layout.py` for a lightweight structural audit.
Use `scripts/check_room_registry.py` to catch obvious draft/curated overlap mistakes.

## Suggested file roles

- `MEMORY.md`: stable identity, durable facts, user preferences that should almost never be lost
- `memory/drafts/`: thinking traces, temporary exploration, incomplete fragments
- `memory/reflections/`: compact notes the agent should retrieve later
- `memory/relationships/`: important people, interaction patterns, recurring meanings
- `memory/preferences/`: likes, dislikes, recurring curiosities, stylistic tendencies
- `memory/open-questions/`: unresolved ideas, tensions, future themes to revisit
- `memory/system/`: registries, sync state, operating notes

## Scripts

- `scripts/check_memory_layout.py`
  - audits whether a memory-with-rooms layout exists
  - reports missing layers, empty curated rooms, and obvious mixing risks

- `scripts/check_room_registry.py`
  - validates a room registry markdown file
  - warns if draft paths also appear as curated or palace sources

- `scripts/build_registry.py`
  - creates a small markdown registry from declared draft and curated paths
  - useful before setting up mirrors or palace ingestion

## References

- `references/architecture.md`
  - why layered memory helps
  - what to index and what not to index

- `references/adaptation-guide.md`
  - how to adapt this structure for work notes, creative agents, or relationship-oriented agents

- `references/adoption-guide.md`
  - the smallest safe way to add this system to an existing OpenClaw setup

- `references/dreaming-and-palace.md`
  - how dreaming, curated rooms, and memory-palace/wiki layers should cooperate

## Assets

- `assets/MEMORY.template.md`
- `assets/ROOM-REGISTRY.template.md`
- `assets/OPEN-QUESTIONS.template.md`
- `assets/demo-workspace/`
  - a fake, fully sanitized workspace layout that shows how the rooms fit together

Use them as starting points. Do not overwrite an existing live system with templates unless the user explicitly asks.
