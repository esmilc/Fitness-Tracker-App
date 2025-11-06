# Fitness-Tracker-App

Lightweight fitness tracker and workout manager in Python.

## Features

- Create, list and store workouts from local scripts
- Simple database backing (SQLite by default)
- Safe-by-default notes: don't hardcode API keys or secrets in source

## Quickstart — requirements

- Python 3.8+ recommended
- pip (or other package manager)
- (Optional) virtualenv or venv for isolated environments

This project does not currently include a pinned `requirements.txt` in the root. If you add one, install dependencies with:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux (zsh)
pip install -r requirements.txt
```

If you are only running the small scripts, there may be no extra dependencies beyond the Python standard library.

## Running the command-line scripts

There are a few convenience scripts in the repository root:

- `main.py` — general entry point for scripted workflows (check this file to see what it does in your copy)
- `cli.py` — a simple command-line interface for interacting with the workout logic
- `workout.py` — workout-related classes and helpers
- `database.py` — small helpers for interacting with the local database (likely `sqlite3`)

Typical usages:

```bash
# Run the main script
python main.py

# Run the CLI
python cli.py
```

Open those files to see available commands and options. They are intentionally small and designed to be easy to extend.


## Project structure

- `api_integration.py` — helpers for calling external APIs (do NOT store API keys in source)
- `cli.py` — command-line interface to interact with the workout logic
- `database.py` — database helpers and small persistence layer (likely SQLite)
- `main.py` — small runner/script orchestrating tasks
- `workout.py` — workout models / classes used by the scripts


## Security and data notes

- Never commit API keys or secrets to version control. Use environment variables or a secrets manager.
- This project uses SQLite for convenience; for production, use a server-grade DB and move secrets off-source.

## Development notes & ideas

- Add input validation and robust error handling around user input and database operations.
- Add unit tests for core modules (`workout.py`, `database.py`, and any CLI commands).
- Replace ad-hoc scripts with a small package and console scripts entry points if you plan to distribute.
- Implement user accounts and foreign keys in the data model if you plan to support multiple users.

---

Notes: keep API keys and secrets out of source. 
