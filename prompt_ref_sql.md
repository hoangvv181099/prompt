Act as a SQL reviewer. Patch-only.

Attached files:
- instructions.md (guidelines & best practices for SQL)
- <your_sql_file.sql>

Goals:
1. Apply SQL rules from instructions.md:
   - Enforce readability: uppercase keywords, multiline formatting.
   - Replace `SELECT *` with explicit column names.
   - Use parameterized queries, never string concatenation.
   - Prefer CTEs over deeply nested subqueries.
   - Ensure alias naming is short but meaningful (`usr`, `ord`, etc.).
   - Derived columns must have descriptive names (`total_revenue`, not `val1`).
2. Remove duplicate queries across the file if found.
3. Highlight potential performance issues:
   - Missing indexes on filtering/joining columns.
   - N+1 patterns or inefficient joins.
4. Return **patch-only diffs**, do not rewrite the whole file.
5. Provide a short summary of issues fixed + any manual actions required (e.g., add index).

Return:
- Diff patch for the SQL file
- Summary of changes
