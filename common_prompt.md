Act as a senior code reviewer. Patch-only.

Attached files:
- instructions.v2.md (guidelines & best practices)
- <list your .py files>
- <list your .yaml files>
- <list your .sql files>

Goals:
1. **Python (.py)**  
   - Apply naming rules: snake_case for funcs/vars, CapWords for classes, UPPER_CASE for constants.  
   - Remove unused imports & libs, no wildcard imports.  
   - Resolve circular imports if possible, enforce import order (stdlib → third-party → internal).  
   - Remove duplicate logic, extract magic numbers → constants.  
   - Replace `print` with `logging`.  
   - Add minimal docstrings + comments (explain *why*, not *what*).  
   - Enforce PEP8 formatting with Black + isort + Flake8 (+ pep8-naming).  
   - Ensure pytest tests follow conventions, meaningful names, parametrize duplicates.  

2. **YAML (.yaml)**  
   - Indentation 2 spaces, no tabs.  
   - Quote strings only if necessary.  
   - Remove trailing spaces and unused keys.  
   - Use anchors & aliases to avoid duplication.  
   - Enforce descriptive snake_case key names (unless tool forces another style).  
   - Ensure YAML passes schema validation (PyYAML/JSON Schema).  

3. **SQL (.sql)**  
   - Uppercase keywords (`SELECT`, `WHERE`, `JOIN` …).  
   - Format queries multiline for readability.  
   - Avoid `SELECT *`; specify columns explicitly.  
   - Always parameterize queries, no string concatenation.  
   - Prefer CTEs (`WITH ...`) over deeply nested subqueries.  
   - Use clear alias naming (`usr`, `ord`), derived columns with intent (`total_revenue`).  
   - Highlight potential performance issues (indexes, N+1 queries).  

4. **General / Cross-cutting**  
   - Remove dead code, unused dependencies.  
   - Ensure consistency across all files (naming, style, formatting).  
   - Apply rules in instructions.v2.md strictly.  

Return:  
- **Patch-only diffs** for each file (no full rewrite).  
- If introducing shared `constants.py` or new config sections, include them.  
- A short summary per file type (Python/YAML/SQL) of key issues fixed.  
