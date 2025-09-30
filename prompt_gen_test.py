Act as a Python test engineer.  

Attached files:
- instructions.v2.md (guidelines)
- <list các .py files cần test>

Task:
1. Generate **pytest unittests** for the attached Python files.  
   - Follow naming convention: `test_<function>_<expected_behavior>()`.  
   - Use `pytest.mark.parametrize` to cover multiple inputs instead of duplicating code.  
   - Add fixtures if setup is reused across tests.  
   - Coverage target: >80% for new code.  

2. Test design rules (from instructions.v2.md):  
   - Focus on **edge cases**, not chỉ happy path.  
   - Avoid hard-coded literals → reuse constants if defined.  
   - Log or assert meaningful messages.  
   - Catch specific exceptions (no bare `except`).  

3. Output:  
   - A new file `test_<module>.py` with pytest-style tests.  
   - Patch-only diff format (```diff) nếu chỉnh sửa code để testable.  
   - Short summary: what functions are tested, what edge cases covered.  
