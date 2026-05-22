# Contributing

Thanks for helping improve Memory With Rooms.

This project is still early, so the most useful contributions are usually small, practical ones:

- clearer room layouts
- safer migration advice
- better registry conventions
- tighter audit scripts
- real-world examples from OpenClaw workspaces

## What makes a good contribution

Please prefer changes that keep the system:

- additive rather than destructive
- easy to adopt in an existing workspace
- clear about the boundary between drafts and curated memory
- cautious about what gets promoted into palace/wiki or dreaming inputs

## Before opening a pull request

1. Read [README.md](./README.md)
2. Read [SKILL.md](./SKILL.md)
3. Run the local smoke test:

```powershell
py -3 .\scripts\smoke_test.py
```

If you are changing registry or layout logic, please also run:

```powershell
py -3 .\scripts\check_memory_layout.py .\assets\demo-workspace
py -3 .\scripts\check_room_registry.py .\assets\demo-workspace\memory\system\room-registry.md
```

## Scope and privacy

Please do not include:

- personal chat logs
- private relationship memory
- tokens, keys, or live credentials
- raw workspace exports that were not intentionally sanitized

This repository is meant to share a memory architecture, not anyone's private memory contents.
