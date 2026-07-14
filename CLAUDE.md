# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Bowling Game Kata implementation in Python. The codebase currently has no source files yet — only a `.venv`, PyCharm project metadata (`.idea/`), and a leftover pytest cache referencing a `test_game.py` that is not present in the working tree. Treat this as a from-scratch implementation.

### Requirements (Bowling Game Kata)

Implement a `Game` class with:
- `roll(pins: int) -> None` — called once per ball thrown; `pins` is the number of pins knocked down.
- `score() -> int` — returns the total score for the game.

Scope is intentionally reduced (this is a kata):
- Do not validate that individual rolls are legal.
- Do not validate that the number of rolls/frames is correct.
- Do not expose intermediate/per-frame scores — only the final total via `score()`.

Scoring rules to implement:
- **Open frame**: sum of the two rolls.
- **Spare** (two rolls in a frame total 10): frame score = 10 + pins knocked down on the *next* roll.
- **Strike** (10 pins on the first roll of a frame): frame score = 10 + pins knocked down on the *next two* rolls; the frame ends after one roll.
- **10th frame**: if it's a spare or strike, the player gets extra roll(s) to complete the frame (up to 3 rolls total in the 10th frame), and those extra rolls count only toward the 10th frame's bonus, not as new frames.

## Environment & Commands

Python 3.14, managed via a local virtualenv at `.venv` (already created). Test runner is `pytest` (already installed in `.venv`; also `pluggy`, `iniconfig`, `packaging`, `colorama`, `pygments` as pytest's own dependencies — no other third-party packages are installed yet).

```powershell
# Activate the virtualenv (PowerShell)
.venv\Scripts\Activate.ps1

# Run the full test suite
.venv\Scripts\pytest.exe

# Run a single test file
.venv\Scripts\pytest.exe test_game.py

# Run a single test by name
.venv\Scripts\pytest.exe test_game.py::test_perfect_game -v
```

There is no build step, lint config, or `requirements.txt`/`pyproject.toml` in the repo yet — if you add dependencies beyond pytest, add them explicitly and record them in a requirements/pyproject file.

## TDD Workflow

This repo uses the `agentic-test-driven-development` skill (`.claude/skills/agentic-test-driven-development/SKILL.md`) for all implementation work, adapted to this Python/pytest project rather than the C++/GoogleTest examples it documents. Key points specific to this repo's flow:

- Before writing any test, write/update a `Plan.md` describing the behavior to be tested next, and get it reviewed/discussed with the user before writing the failing test.
- After making a test pass with minimal code, get the implementation reviewed/discussed with the user before refactoring or moving to the next test.
- Test file naming follows pytest convention: `test_*.py`, with test functions named `test_<behavior_description>` (snake_case, describing the scenario — e.g. `test_all_spares_scores_150`, `test_strike_in_tenth_frame_gets_two_bonus_rolls`).
