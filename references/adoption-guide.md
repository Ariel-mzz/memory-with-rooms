# Adoption Guide

## Goal

This guide is for agents that already have a working OpenClaw workspace and need the smallest safe path toward layered memory.

## Smallest useful adoption path

1. Leave the current memory system in place.
2. Create only these new folders:
   - `memory/drafts/`
   - `memory/reflections/`
   - `memory/system/`
3. Put new raw process notes into `memory/drafts/`.
4. Put short, settled notes into `memory/reflections/`.
5. Create a registry file in `memory/system/` that states:
   - which paths are draft-only
   - which paths are curated retrieval sources
   - which paths may feed palace/wiki layers

This alone is enough to make later retrieval cleaner.

## If the workspace already has daily notes

Do not migrate everything at once.

Instead:

1. Keep the old files.
2. Start writing new raw notes into `memory/drafts/`.
3. Write concise conclusions into `memory/reflections/`.
4. Let retrieval gradually shift toward curated rooms.

## If dreaming is already enabled

Do not point dreaming or palace ingestion at draft folders first.

Prefer:

- dreaming reads existing recall artifacts as usual
- curated rooms become the preferred source for later summarization
- palace/wiki layers ingest curated rooms before any draft content

## If a memory palace or wiki layer already exists

Before changing ingestion, document the current sources.

Then move in this order:

1. reflections
2. relationships
3. preferences
4. open questions
5. drafts only if explicitly intended

## Recommended first verification

After adoption, check whether the agent can answer:

- what was concluded last week
- what is still unresolved
- what preferences have become stable

without quoting raw process notes by default.
