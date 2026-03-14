---
name: uv-run
description: Use when setting up, installing dependencies, or running the EduTrack project locally with uv (Python package manager). Covers creating or reusing a local virtual environment, syncing dependencies from uv.lock or pyproject.toml, and running app/test commands via uv.
---

# UV Run (EduTrack)

## Overview

Use uv to install and run EduTrack locally. Follow the project’s own run instructions, but translate all environment and command steps into uv-native workflows.

## Workflow

1. Locate the project root.
2. Read run instructions in the project docs.
3. Create or reuse a uv-managed virtual environment.
4. Sync or install dependencies with uv.
5. Run the requested command with `uv run`.
6. If needed, adjust dependencies or troubleshoot.

## Step 1: Locate Project Root

Use `/Users/anju/EduTrack` as the project root (it contains `pyproject.toml` and `uv.lock`). Run all uv commands from this directory unless the user specifies otherwise.

## Step 2: Read Project Instructions

Open the project’s README or setup guide and follow its run steps, but use uv for environment and dependency management. For EduTrack, the typical run sequence is: sync deps, make migrations (when models change), migrate, run server.

## Step 3: Create or Reuse a uv Environment

If `.venv` does not exist in the project root, create it with:

```bash
uv venv
```

Use the existing `.venv` if it already exists.

## Step 4: Install or Sync Dependencies

Prefer lockfile-based installs:

```bash
uv sync
```

If there is no `uv.lock`, install from the available metadata:

1. If `pyproject.toml` defines the project, run `uv pip install -e .`.
2. If a `requirements.txt` exists, run `uv pip install -r requirements.txt`.

## Step 5: Run Commands

Run all app, script, or test commands through uv:

```bash
uv run <command>
```

Examples (EduTrack):

```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
uv run python manage.py runserver
uv run pytest
```

## Step 6: Dependency Changes (If Needed)

Add or update dependencies with uv and then re-sync:

1. Run `uv add <package>` or `uv add <package>==<version>`.
2. Run `uv sync`.

## Troubleshooting

1. If the environment looks corrupt, delete `.venv` and run `uv sync` again.
2. If a command fails, re-check the project docs for required environment variables and set them before re-running `uv run`.
