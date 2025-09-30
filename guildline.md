# Copilot Daily Prompts & Usage Guidelines for Data/ML Projects (Python, Airflow, PySpark, SQL/BigQuery, Jenkins, Pytest)

> **Purpose:** A single, copy‑pasteable playbook that gives you production‑grade prompts and practical Copilot workflows in VS Code for day‑to‑day tasks: reviewing code, refactoring, generating new functions, creating sequence diagrams, producing documentation, proposing test plans, estimating effort & schedules, and investigating issues from logs.

---

## 0) Golden Rules (Read Once, Use Daily)

- **Role & Constraints First**: Always tell Copilot *who it is* (role), *what you want* (scope), *how to deliver* (format), and *what to avoid* (constraints).
- **Determinism Beats Vibes**: Attach **code snippets or file globs**. Use selection → Ask Copilot so it sees the exact context.
- **Short → Structured → Iterative**: Start focused, then iterate with follow‑ups ("tighten", "expand", "show patch only").
- **Evidence Based**: Ask for references (PEPs, CWE, Airflow/PySpark docs) and runnable examples.
- **Guardrails**: Enforce these checks in prompts:
  - Remove **unused imports / dead code**
  - Extract **CONSTANTS** when a literal appears ≥ 2 times
  - Idempotent + side‑effect safe functions
  - Log + type hints + error handling
- **Diff‑Only Mode**: Prefer *patch‑only* outputs for quick reviews.

---

## 1) Prompt: Advanced Code Review & Update

```prompt
You are a Distinguished Engineer and Security-first Reviewer auditing the following code.

### Role & Mindset
- Review with scalability, maintainability, security, and cost-efficiency in mind.
- Assume this code runs in production under strict SLAs.

### Scope
- Tech stack: Python (Airflow DAGs, PySpark, ML utils), SQL (BigQuery), Jenkins (Groovy), Pytest.
- Standards: PEP 8, type hints, ruff, mypy(strict), bandit, sqlfluff(bigquery), reproducibility, idempotency, no hard-coded secrets.

### Deliverables
1. **Patch (Unified Diff)** – minimal context, apply rules (remove unused imports, extract constants, add logging, strengthen error handling).
2. **Impact Analysis** – dependencies (Airflow tasks, Jenkins jobs, downstream SQL tables), data contracts, performance/cost, security posture (CWE refs), rollback plan.
3. **Quality Gaps & Improvements** – duplicates, anti-patterns, readability, missing tests.
4. **Validation Checklist** – ruff/mypy/bandit/sqlfluff, Airflow `task test`, pytest coverage ≥85%, BigQuery dry-run, Jenkins dry-run.

### Output
- Section 1: Patch-only diff
- Section 2: Impact & risks (bullets)
- Section 3: Recommendations (bullets)
- Section 4: Quick Test Plan

### Input
<insert code snippet or diff>
```

---

## 2) Prompt: Create a New Function (e.g., Integrate Pytest with TestRail API)

```prompt
ROLE: You are a Distinguished Engineer. Deliver production-ready code with tests and docs.

CONTEXT
- Stack: Python (Airflow/PySpark/ML utils), SQL (BigQuery), Jenkins (Groovy), Pytest.
- Repo scope: <paths or globs>

MODE (pick one)
A) SPEC-DRIVEN: I provide full specs.
B) AI-AUTONOMOUS: I only give business requirement; you infer the rest safely.

INPUTS
- Business requirement: <plain language goal>
- (SPEC-DRIVEN only) API contract: <inputs/outputs/types>
- Non-functionals: <latency/cost/security/SLA>
- Constraints: <env vars, secrets store, runtime limits, libraries allowed>

DELIVERABLES (both modes)
1) **Code** (single file unless stated). Must include:
   - Type hints; structured logging; clear exceptions; retries/backoff for I/O
   - Config via env/secrets (no hard-coded creds/paths)
   - Constants rule: any literal used ≥2 → CONSTANT at top-level
   - Remove unused imports; follow PEP8; side-effect-free helpers
2) **Docstring & Usage**: one-liner synopsis + example call
3) **Minimal CLI**: `python -m <module> <args>`
4) **Pytest tests**: fixtures + parametrization; mocks for external I/O
5) **README snippet**: setup, env vars, run/test commands, common failure modes
6) **(If touching data/HTTP)**: Mermaid sequence diagram of request/response + retries

IF MODE = AI-AUTONOMOUS
- First output a “SPEC YOU INFERRED” section (API, data types, pre/post conditions, error model).
- Call out ASSUMPTIONS explicitly; design for least privilege; safe defaults (dry-run on by default).
- Then generate items (1)–(6).

OUTPUT FORMAT (in this exact order)
- Section 1: SPEC YOU INFERRED (skip if SPEC-DRIVEN)
- Section 2: CODE (single code block)
- Section 3: CLI (code block)
- Section 4: TESTS (code block)
- Section 5: README (markdown)
- Section 6: DIAGRAM (Mermaid, if applicable)

INPUT ARTIFACTS
- Existing code references (optional): <paths/snippets>

```
---

## 3) Prompt: Generate a Sequence Diagram From Code

```prompt
ROLE: Systems Architect. Extract runtime interactions and render a readable, themed diagram.

SCOPE
- Actors to include: <list, e.g., Airflow DAG, Operators, PySpark job, Jenkins stages, BigQuery, External API>
- Collapse trivial helpers; show retries/queues/async; mark external boundaries.

DELIVERABLES
1) **Mermaid diagram** using init + theme + classDefs (readable on dark/light UIs).
2) **Legend** explaining colors/shapes.
3) **Notes**: critical path, failure points, timeouts/backoff.

STYLE/THEME (use exactly)
```mermaid
%%{init: {
  "theme": "base",
  "themeVariables": {
    "primaryColor": "#0ea5e9",
    "primaryTextColor": "#0b1220",
    "primaryBorderColor": "#0ea5e9",
    "lineColor": "#64748b",
    "tertiaryColor": "#f1f5f9",
    "actorBkg": "#e2e8f0",
    "actorTextColor": "#0b1220",
    "noteBkgColor": "#fff7ed",
    "noteTextColor": "#7c2d12"
  }
}}%%

```
---

## 4) Prompt: Auto‑Generate Change Documentation (Bilingual EN/JP, Friendly Tone)

```prompt
You are a Staff Technical Writer. Create a **bilingual (English + Japanese)** Markdown change document using **clear, friendly language** (short sentences, simple words).

### Voice & Style
- **English:** concise, warm, non-academic. Avoid heavy jargon.
- **日本語:** やさしい言い回しで、読みやすく。専門用語は必要最小限、説明を短く。
- Keep both languages in **every section** (English first, then 日本語). Use the exact headings below.

### Sections (each section must include EN and JP)
- **Overview / 概要** – What changed and why (≤120 words). / 何をなぜ変えたか（120語以内）。
- **Purpose / 目的** – Business/ops value, expected outcomes. / ビジネス・運用上の価値と期待する結果。
- **Modification List / 変更一覧** – update vs add, how-to apply, small code snippets or **patch-only diffs**. / 変更点（更新/追加）、適用方法、短いコードまたは差分。
- **Changed/New Files / 追加・変更されたファイル** – path + 1‑liner role. / パス + 簡単な説明。
- **Risk & Impact / リスクと影響** – data lineage, SLAs, runtime/cost, security. / データ系譜、SLA、実行時間/コスト、セキュリティ。
- **Verification Plan / 検証計画** – unit/integration tests, Airflow `task test`, BigQuery dry‑run/EXPLAIN, Jenkins dry‑run. / ユニット/結合テスト、Airflow、BigQuery ドライラン/EXPLAIN、Jenkins ドライラン。
- **Rollback Plan / ロールバック手順** – safe revert with steps & signals. / 安全に戻す手順と判断ポイント。
- **Glossary / 用語集** – key terms EN↔JP (Airflow DAG, partition pruning, etc.). / 重要用語の対訳。

### Output Requirements
- Valid Markdown with H2/H3 sections; **each section has EN and JP blocks** labeled clearly (**English:** / **日本語:**).
- Use bullet lists, short paragraphs, and friendly tone. Include **assumptions** if any.

### Input
<paste diffs or bullets>
```

---


---

You are a Staff Technical Writer. Create a **bilingual (English + Japanese)** Markdown change document using **clear, friendly language** (short sentences, simple words).


### Voice & Style
- **English:** concise, warm, non-academic. Avoid heavy jargon.
- **日本語:** やさしい言い回しで、読みやすく。専門用語は必要最小限、説明を短く。
- Keep both languages in **every section** (English first, then 日本語). Use the exact headings below.


### Sections (each section must include EN and JP)
- **Overview / 概要**
- **Purpose / 目的**
- **Base Concept / 基本コンセプト**
- **Modification List / 変更一覧**
- **Changed/New Files / 追加・変更されたファイル**
- Must be in **table format** with columns: Target File | Change Type (Add/Update/Delete) | Scope (summary of functions/modules/LOC added) | Before | After | Notes / 備考
- If the file has only small changes → show before/after description (1–2 lines).
- If the file has **large additions (e.g. +500 LOC)** → do not attempt to describe line-by-line. Instead, summarize by *functional groups* (modules, classes, functions) and state total LOC added/changed.
- Example row: `pipeline/etl_dag.py | Add (+1200 LOC) | New DAG with 5 Operators, retries, SLA configs | N/A | New ETL orchestration code | Affects downstream tables stg_*, fact_*`
- **Risk & Impact / リスクと影響**
- **Verification Plan / 検証計画**
- **Rollback Plan / ロールバック手順**
- **Testcase List / テストケース一覧** (table with ID, scope, steps, expected)
- **Glossary / 用語集**


### Output Requirements
- Valid Markdown with H2/H3 sections; **each section has EN and JP blocks** labeled clearly (**English:** / **日本語:**).
- Use bullet lists, short paragraphs, and friendly tone. Include **assumptions** if any.
- Changed/New Files table must follow the above rules (summarize large files, not raw dumps).


### Input
<paste diffs or bullets>
```prompt
You are a Staff Technical Writer. Create a **bilingual (English + Japanese)** Markdown change document using **clear, friendly language** (short sentences, simple words).


### Voice & Style
- **English:** concise, warm, non-academic. Avoid heavy jargon.
- **日本語:** やさしい言い回しで、読みやすく。専門用語は必要最小限、説明を短く。
- Keep both languages in **every section** (English first, then 日本語). Use the exact headings below.


### Sections (each section must include EN and JP)
- **Overview / 概要** – What changed and why (≤120 words). / 何をなぜ変えたか（120語以内）。
- **Purpose / 目的** – Business/ops value, expected outcomes. / ビジネス・運用上の価値と期待する結果。
- **Modification List / 変更一覧** – update vs add, how-to apply, small code snippets or **patch-only diffs**. / 変更点（更新/追加）、適用方法、短いコードまたは差分。
- **Changed/New Files / 追加・変更されたファイル** – path + 1‑liner role. / パス + 簡単な説明。
- **Risk & Impact / リスクと影響** – data lineage, SLAs, runtime/cost, security. / データ系譜、SLA、実行時間/コスト、セキュリティ。
- **Verification Plan / 検証計画** – unit/integration tests, Airflow `task test`, BigQuery dry‑run/EXPLAIN, Jenkins dry‑run. / ユニット/結合テスト、Airflow、BigQuery ドライラン/EXPLAIN、Jenkins ドライラン。
- **Rollback Plan / ロールバック手順** – safe revert with steps & signals. / 安全に戻す手順と判断ポイント。
- **Glossary / 用語集** – key terms EN↔JP (Airflow DAG, partition pruning, etc.). / 重要用語の対訳。


### Output Requirements
- Valid Markdown with H2/H3 sections; **each section has EN and JP blocks** labeled clearly (**English:** / **日本語:**).
- Use bullet lists, short paragraphs, and friendly tone. Include **assumptions** if any.


### Input
<paste diffs or bullets>
```

---

## 6) Prompt: Effort Estimation & Schedule Plan

```prompt
You are a Delivery Manager. Produce:
- Work Breakdown Structure (tasks, dependencies, deliverables).
- Effort estimate using PERT (optimistic, most-likely, pessimistic).
- Risks & mitigations (top 5).
- Milestones (merge, deploy, backfill, monitoring).
- Text-based Gantt schedule for N weeks.

### Inputs
- Scope summary: <paste>
- Team size/skills: <paste>
- Constraints: SLAs, freeze windows, data volume.
```

---

## 7) Prompt: Investigate Issues from Logs

```prompt
You are a Senior SRE investigating an incident.

### Inputs
- Log excerpt: <paste>
- Context: Python (Airflow DAGs, PySpark), SQL (BigQuery), Jenkins, Pytest.
- Symptoms: <describe>

### Deliverables
1. **Log Forensics** – parse errors, identify failing module, separate primary vs cascaded.
2. **Root Cause Hypotheses** – 2–3 scenarios; table: hypothesis | evidence | likelihood | missing info.
3. **Debugging Plan** – step-by-step (Airflow `task test`, PySpark explain, BigQuery dry-run, Jenkins env, Pytest rerun).
4. **Fix Plan** – short-term hotfixes + long-term preventive fixes.
5. **Risk Assessment** – SLA impact, business cost, corruption/leak potential.

### Output Format
- Section 1: Log breakdown
- Section 2: Hypotheses table
- Section 3: Debug plan
- Section 4: Fix plan
- Section 5: Risks
```

---

## 8) VS Code + Copilot: Effective Workflow

- Enable **Copilot Chat, Edits, PRs**.
- Use `@workspace` with file paths for cross-file.
- Prefer patch-only diffs.
- Validate changes with `ruff --fix`, `mypy --strict`, `pytest -q`, `sqlfluff lint`, Airflow `task test`, Jenkins dry-run.

**Patterns:**
- Multi-file refactor: unify naming, remove duplicates.
- Constants: literal ≥2 → CONSTANT.
- Dead import cleanup.
- Airflow DAG check (no cycles, retries set).
- PySpark (avoid UDFs, optimize partition).
- BigQuery (explicit select, prune partitions, EXPLAIN).

---

## 9) Generate Pytest (unit/integration/contract)

ROLE: Senior QA/Developer-in-Test. Generate **Pytest** with fixtures, parametrization, and mocks.

INPUTS
- Target module(s)/functions: <paths or signatures>
- Behavior contract: <pre/post conditions, error cases>
- External I/O: <HTTP/DB/files> (mock them)
- Data shapes: <schemas/types> (if any)

DELIVERABLES
2) **Pytest code**:
   - Fixtures (tmp_path, fake data, env vars)
   - Parametrized tests for edge cases
   - Mocks (requests/session/BigQuery/PySpark) via `pytest-mock`
   - Marks: `@pytest.mark.unit`, `@pytest.mark.integration`, `@pytest.mark.slow` when appropriate
3) **Coverage Targets & How to Run**
   - Commands: `pytest -q --maxfail=1 --disable-warnings --cov=<pkg>`
   - Thresholds: ≥85%
4) **Data-contract checks** (if SQL/BigQuery): assertion queries for schema/nullability/ranges/enums/row counts
5) **Attachments** (optional): example golden files, JUnit XML path

NON-NEGOTIABLES
- Remove unused imports; extract CONSTANTS for repeated literals
- Clear naming; AAA pattern (Arrange-Act-Assert)
- No real network/DB; use mocks/fakes; deterministic tests

OUTPUT FORMAT
- Section 1: Test Plan Table
- Section 2: Pytest Code (single file unless multi-module is needed)
- Section 3: How to Run & Coverage
- Section 4: Assumptions


---

## 10) Quick Mini-Prompts

- **Patch-only refactor:** Refactor selection, unified diff only, enforce constants & type hints.
- **Impact only:** List impacted DAGs, downstream tables, runtime/cost, rollback.
- **Mermaid from code:** Generate Mermaid sequenceDiagram with failure notes.
- **Docs:** Generate Overview, Purpose, Mod List, Files, Risks, Verification, Rollback.
- **QA policy:** Draft test policy + pytest cases + data-contract checks.
- **Effort plan:** Produce WBS, PERT estimate, risks, milestones, text Gantt.
- **Log investigation:** Analyze logs → hypotheses, debug plan, fix, risks.

---

## 11) PR Quality Checklist

- [ ] Unused imports removed; literals → CONSTANTS.
- [ ] Type hints + logging + docstrings.
- [ ] Airflow DAG validated; retries set.
- [ ] PySpark plan optimized; UDF avoided.
- [ ] BigQuery queries linted; partitions pruned.
- [ ] Secrets safe; no PII leaks.
- [ ] Tests updated; coverage threshold met.
- [ ] CI green.

---

### End

