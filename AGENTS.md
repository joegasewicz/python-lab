# Agent Instructions

This repository is read-only for AI agents by default.

Agents must not modify files, create commits, rewrite history, delete files, install dependencies, run formatters that write changes, or push to any remote unless the user explicitly gives permission in the current conversation.

Allowed by default:
- Read files and inspect repository state.
- Run non-mutating commands that only print information.
- Explain findings, propose patches, or describe commands for the user to run.

Requires explicit user approval first:
- Editing, creating, moving, or deleting files.
- Staging, committing, rebasing, resetting, or pushing Git changes.
- Running tests or tools that write caches, generated files, lockfiles, snapshots, or build output.
- Installing, upgrading, or removing dependencies.

If a task appears to require writes, stop and ask for permission before making changes.
