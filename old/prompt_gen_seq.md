Act as a system analyst.  

Attached files:
- module_a.py
- module_b.py
- <thêm file .yaml / .sql nếu cần>

Tasks:
1. Parse code and detect:
   - Main participants (modules, classes, external systems)
   - Key function calls and their order
   - External resources (DB, API, YAML config)

2. Generate a **Mermaid sequence diagram** with:
   - Clear lifelines for each participant
   - Call arrows with method names
   - Return arrows for responses
   - External DB/API shown as `Database` or `Actor`

3. Apply **Mermaid theming & style**:
   - Use `%%{init: ...}%%` block to customize:
     - Background: light gray
     - Actors: rounded corners, soft shadow
     - Color palette:  
       - Clients → blue  
       - Internal modules → green  
       - External systems (DB/API) → orange  
   - Increase font size for readability

4. Output only:
   - Mermaid code block (```mermaid … ```), no extra text
   - Then a short bullet summary of the flow
