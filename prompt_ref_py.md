Act as a senior Python reviewer. Patch-only.

Attached files:
- instructions.md (guidelines & best practices)
- module_a.py
- module_b.py

Goals:
1) Apply all rules in instructions.md across both Python files.
2) Fix naming (snake_case for functions/vars, CapWords for classes, UPPER_CASE for constants).
3) Resolve or minimize circular imports; reorder imports (stdlib → third-party → internal); remove wildcard imports.
4) Remove duplicate logic; extract repeated literals → constants. If cross-file → propose a new `constants.py`.
5) Secure SQL: parameterized queries (no string concat).
6) Replace print with logging; add minimal docstrings & meaningful comments (**why**, not what).
7) Enforce Black + isort + Flake8 (+ pep8-naming). 88 cols, 4 spaces.
8) Return **patch-only diffs** for module_a.py and module_b.py, plus new constants.py if introduced.
9) Add a short note explaining how you addressed the circular import.
