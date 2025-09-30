Act as a YAML reviewer. Patch-only.

Attached files:
- instructions.md (guidelines & best practices for YAML)
- <your_yaml_file.yaml>

Goals:
1. Apply YAML rules from instructions.v2.md:
   - Indentation = 2 spaces, no tabs.
   - Quote strings **only when necessary** (avoid noise).
   - Remove trailing spaces, unused keys.
   - Use **anchors & aliases** (`&default`, `*default`) to avoid duplication.
   - Enforce consistent **naming** for keys: snake_case unless tool requires another style.
   - Keys must be descriptive (`retry_count`, `max_timeout_seconds`), no vague names (`cfg1`, `misc`).
2. Ensure the YAML passes schema validation (PyYAML/JSON Schema).
3. Reject anti-patterns:
   - Repetition without anchors.
   - Randomly quoted/unquoted strings.
   - Inconsistent key casing.
4. Return **patch-only diffs**, no full rewrite.
5. Provide a short summary of changes and note if schema validation is required externally.

Return:
- Diff patch for the YAML file
- Summary of applied fixes
