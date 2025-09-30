# Copilot Review & Refactor Guidelines

This document defines the rules and best practices for using GitHub Copilot to review and refactor code in our project (Python, SQL, YAML).
The purpose is to ensure maintainability, readability, and long-term scalability across the entire codebase.

---

## 1. General Principles
- **Clarity over cleverness**: prefer readable, explicit code over obscure one-liners.
- **Consistency first**: follow project conventions (naming, imports, indentation).
- **Automate style**: rely on linters/formatters (Black, Flake8, isort, Prettier for YAML).
- **No dead code**: remove unused imports, variables, functions, and comments.
- **Document intent**: minimal but clear docstrings for all public functions and classes.

---

## 2. Python Code Rules

### 2.1 Naming (Methods & Variables)
- Use **snake_case** for functions/methods/variables, **CapWords** for classes, **UPPER_CASE** for constants.
- Names must be **meaningful and specific**:
  - Prefer `fetch_user_by_id()` over `getData()`; `retry_count` over `x`.
  - Avoid unclear abbreviations. If you must abbreviate, use well-known forms (`id`, `db`, `cfg`).
- **Boolean names** start with `is_`, `has_`, `should_`, `can_` (e.g., `is_active`, `has_error`).
- **Verb-first for functions**, **noun for classes/objects**.
- Avoid single-letter names except for trivial indices in short scopes (`i`, `j` in small loops).
- Private/internal helpers: prefix with `_` (e.g., `_normalize_email`).
- Do not encode types in names (no Hungarian notation).
- Keep parameter names consistent across layers (API → service → repo). If you rename a concept, rename it **everywhere**.
- Enforce via **pep8-naming** (flake8-naming) in CI.

### 2.2 Constants
- Any literal used **2 or more times** → extract as a constant (UPPER_CASE).
- Store constants in a dedicated module (e.g., `constants.py`).

### 2.3 Functions & Methods
- Avoid duplicate code: factor shared logic into helper functions.
- No hard-coded values inside methods; use config, environment, or constants.
- Limit function length: prefer <50 lines; split responsibilities if needed.

### 2.4 Commenting
- Use comments to explain **why**, not **what** (the code itself should show *what* it does).
- Avoid redundant comments like `i += 1  # increment i`.
- Use `# TODO:` for planned work and ensure they are tracked (issue/ticket).
- Keep comments updated when refactoring; stale comments must be removed.

### 2.5 Docstrings
- All public functions and classes must have docstrings (PEP 257 style).
- Follow project’s docstring style (NumPy or Google). Example:
  ```python
  def fetch_user(user_id: int) -> User:
      """Fetch a user from the database.

      Args:
          user_id (int): The unique ID of the user.

      Returns:
          User | None: User instance if found, else None.
      """
  ```

### 2.6 Formatting
- Enforce [PEP 8] style.
- Use **Black** for auto-formatting, **isort** for imports, **Flake8** (+ **pep8-naming**) for lint checks.
- Maximum line length: 88 chars (Black default).
- Indentation: 4 spaces (no tabs).
- One blank line between functions; two blank lines between top-level classes/functions.
- Break long parameter lists, dict/JSON literals, and comprehensions across lines when needed.

### 2.7 Imports
- **Explicit imports only**; **do not use** `from x import *`.
- **Order imports**: stdlib → third-party → internal. Enforce with **isort**.
- **One module per import line** unless grouping is clearer and passes linting.
- **Remove unused imports** automatically:
  - Prefer **ruff** (`F401`, `F403`) with `--fix`, or **autoflake** (`--remove-all-unused-imports`) in pre-commit.
  - CI must fail on unused imports (ruff/flake8 config).
- Avoid circular imports; if unavoidable, move imports to function scope or refactor modules to break cycles.

### 2.8 Dependencies Hygiene
- Keep `requirements.txt` / `pyproject.toml` minimal; **remove unused libraries**.
- Detect unused/undeclared dependencies with tools like **deptry** (unused/obsolete/missing), verify with **pipdeptree**.
- When removing a dependency:
  1) Ensure no runtime usage (search + tests pass).  
  2) Remove from dependency files and lock files.  
  3) Run the full test suite and smoke tests.
- Periodically run **pip-audit** (or equivalent) to surface known vulnerabilities (fix separately from feature PRs).

### 2.9 Testing
- Ensure Copilot-generated tests follow Pytest conventions.
- Provide meaningful test names (`test_should_fail_when_input_invalid`).
- Use fixtures for shared setup.
- Use `pytest.mark.parametrize` to avoid duplicated tests.
- Aim for >80% coverage on new/modified code.

---

## 3. SQL Rules

### 3.1 Readability
- Use uppercase for SQL keywords (`SELECT`, `WHERE`).
- Keep queries multiline for readability.

### 3.2 Parameters
- Always use parameterized queries; never concatenate raw strings.

### 3.3 Consistency
- Prefer CTEs (`WITH ...`) over deeply nested subqueries.
- Avoid `SELECT *`; specify columns explicitly.

### 3.4 Naming
- Use **snake_case** for table and column names (unless existing schema dictates otherwise).
- Table names should be consistent (all singular or all plural per project convention).
- Aliases should be short **but meaningful**: `usr`/`ord` acceptable; avoid ambiguous single letters unless the query is tiny.
- Name derived columns with intent (`total_revenue`, `user_count`), not generic `value1`.

### 3.5 Performance
- Ensure proper indexes exist for filtering/joining columns.
- Avoid N+1 queries; batch when possible.

---

## 4. YAML Rules

### 4.1 Anchors & Aliases
Use YAML anchors (`&`) and aliases (`*`) to avoid duplication.
```yaml
default: &default
  retries: 3
  timeout: 60

job1:
  <<: *default
  script: run_job1.sh
```

### 4.2 Formatting
- Indent with 2 spaces.
- Quote strings only when necessary.
- No trailing spaces or unused keys.

### 4.3 Naming
- Use **snake_case** for keys unless the target tool requires another case (then be consistent).
- Keep key names descriptive (`retry_count`, `max_timeout_seconds`), avoid `cfg1`, `misc`.

### 4.4 Validation
- All configs must pass schema validation (e.g., JSON Schema or PyYAML checks).

---

## 5. Copilot Usage Rules

### 5.1 When to Use Prompts
- For **new code generation**: describe role, scope, output format.
- For **refactor tasks**: specify “patch-only” or “optimize this method.”
- For **constants scan**: ask Copilot to auto-detect repeated literals.

### 5.2 Prompt Style (Patterns)
```markdown
Act as a Python reviewer.
Refactor this function:
- Remove duplicate logic
- Replace literals with constants
- Follow PEP8
```
```markdown
Patch-only: propose minimal diffs (no full-file rewrites).
Explain each change in bullets.
```
```markdown
Scan these files for repeated literals and suggest constants:
- src/a.py
- src/b.py
Return a diff and a constants module proposal.
```
```markdown
Scan and remove unused imports and unused dependencies.
- Apply ruff/autoflake for imports
- Propose dependency removals with justification (deptry report summary)
- Return diffs for code and dependency files
```

### 5.3 Copilot Limitations
- Validate AI output with linters, tests, and human code reviews.
- Copilot should never auto-commit; always review manually.
- Do not trust correctness blindly → run tests/benchmarks before merge.

---

## 6. Quick Start
1. Open the target file(s) (Python/SQL/YAML).
2. Trigger Copilot inline suggestions.
3. If results are weak → open **Copilot Chat** with a structured prompt.
4. For **multi-file refactor**: feed this `.md` guideline + the list of files into Copilot Chat.
5. Apply linter/formatter and cleanup: `ruff --fix` or `autoflake --remove-all-unused-imports`, then `isort`.
6. Run tests to confirm no regression; if dependencies changed, run deptry/pipdeptree and smoke tests.

---

## 7. Anti-Patterns to Reject
- Hard-coded values scattered in code.
- Duplicate SQL queries across files.
- YAML repetition without anchors.
- Comments explaining obvious code (e.g., `i += 1  # increment i`).
- Overuse of “magic numbers” or string literals.
- Vague names (`data`, `tmp`, `processStuff`) for core logic.
- Wildcard imports and **unused imports/dependencies**.

---

## 8. Final Checklist for Refactor
- [ ] No duplicate code.
- [ ] Clear, meaningful names (methods, variables, aliases).
- [ ] Constants extracted.
- [ ] **No unused imports** (ruff/flake8 clean) and **no unused dependencies** (deptry clean).
- [ ] SQL injection prevented.
- [ ] YAML anchors used.
- [ ] Tests updated and passing.
- [ ] Coverage threshold met.
- [ ] Style/format validated.

---

✅ Following these rules ensures that GitHub Copilot becomes a **scalable assistant**, not a liability.
