# Architecture

## Goal

The purpose of this memory style is not to store everything. The purpose is to make later recall cleaner.

Many agents fail not because they forget too much, but because retrieval treats all text as equally important. Raw scratch notes, temporary plans, settled conclusions, preferences, and intimate observations all get flattened into one search pool. The result is noisy recall.

This architecture fixes that by separating memory into rooms.

## Design principles

### 1. Preserve raw process without letting it dominate

Drafts are useful. They show how the agent got somewhere. But they should not automatically become the main material returned during normal recall.

### 2. Curated memory should be easier to find than raw memory

If the agent wrote a final reflection after a long exploration, later retrieval should prefer that reflection over the exploration trace.

### 3. Different kinds of durable memory deserve different homes

Preferences, relationships, reflections, and unresolved questions behave differently. Putting them in different rooms makes later recall more legible.

### 4. Higher-level systems should ingest clean sources

Dreaming, memory-palace, or wiki compilation layers are most helpful when they read curated rooms first. If they ingest noisy drafts indiscriminately, they can become a more organized version of the same clutter.

## Retrieval policy

Recommended default policy:

1. Search curated rooms first.
2. Search draft rooms only on explicit request, or when curated recall is empty.
3. Keep relationship and preference notes small, concrete, and append-friendly.
4. Keep open questions visible, but do not rewrite them as if they were settled facts.

## What to avoid

- Dumping every transcript into durable recall.
- Treating daily logs as equivalent to reflections.
- Letting palace/wiki layers auto-ingest every folder by default.
- Replacing an active memory system without first documenting what already works.
