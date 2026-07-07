# CAFA Agent Code Linter and Rules

v 20251219
## 1. Introduction

This document serves as a comprehensive guide and checklist for the syntax rules, best practices, and potential pitfalls when developing CAFA (Collective AI on the Foundation AI) agents. Adhering to these rules is essential for creating valid, functional, reliable, and maintainable agents on the CAFA platform. Use this guide for linting (analyzing code for potential errors), code reviews, and ensuring compliance with the CAFA Protocol.

## 2. General JSON Structure & Syntax

The foundation of every CAFA agent is a single, valid JSON object.

- Rule 2.1 (Valid JSON): The entire agent code must strictly adhere to JSON formatting rules.
	-  Check: Validate the entire code block using a JSON validator.
- Rule 2.2 (Root Keys): The root object must contain exactly two keys: "options" (a JSON object) and "prompts" (a JSON array).
	-  Check: Verify the presence and types of "options" and "prompts" at the root level.    

- Rule 2.3 (Double Quotes): All JSON keys and string values must be enclosed in double quotes (`"`). Single quotes (`'`) are forbidden.
    - Check: Scan for single quotes used for keys or string values.
    
- Rule 2.4 (No Trailing Commas): Trailing commas after the last element in an object or array are not allowed.
    - Check: Detect trailing commas.
    
- Rule 2.5 (No JSON Comments): Standard JSON does not support comments (`//`, `/* */`). Agent code must not contain JSON comments.
    - Exception: Use Symbolic Turn commenting (`/ Comment\n`) for in-code notes (See Section 5.3). Use the "desc" field in parameters for documentation.
    - Check: Detect JSON comment syntax.
    
- Rule 2.6 (Character Escaping): Avoid unnecessary or incorrect character escaping.
    - Backslashes: Never use a double backslash (`\\`). For literal newlines within strings (primarily in Symbolic Turn comments or specific string formatting), use a single escaped newline (`\n`). Double quotes within string values must be escaped (`\"`).
    - Square Brackets: Never use escaped square brackets (`\[` or `\]`). Use standard, unescaped brackets (`[` and `]`) for all parameter access and list slicing (e.g., `@AP[1:3]@`).
    - Check: Detect `\\`, `\[`, `\]`. Ensure `"` within strings are escaped as `\"`.
    
## 3. Agent Configuration: The options Object

This object contains agent metadata and pre-defined Agent Parameters (APs).

- Rule 3.1 (Required Metadata Keys): Must include required string keys: "title", "brief", "name", "description", and "greeting".
    - Info: The "title" field can accept basic HTML tags for formatting.
    -  Check: Verify the presence and string type of these required keys.
    
- Rule 3.2 (params Object): This nested object is the designated location for pre-defining Agent Parameters (APs) – the agent's static knowledge base or ontology model.
    - Best Practice: Store all static data (quiz questions, personas, rubrics, fixed lists, initial state variables) here. This separates content from logic, improving maintainability and modularity.
    - See Section 7 for detailed AP definition rules within params.
    

## 4. Workflow Definition: The prompts Array

This array defines the agent's step-by-step workflow. Each element must be a valid JSON object representing a single turn.

- Rule 4.1 (Turn Object Structure): Each turn object requires specific properties based on its type (See Section 5).
    
- Rule 4.2 (Relative Turn Numbering - `TN`): Always use the `TN()` command for references between turns (e.g., `@TR@TN(-1)@@`, `@JUMP(@TN(2)@)@`) instead of hardcoded absolute numbers (e.g., `@TR1@`, `@JUMP(3)@`).
    

- Benefit: Makes agent logic robust against adding/removing turns during development.
    
- Check: Detect hardcoded turn references like `@TR1@`, `@TU2@` and suggest replacing them with `TN()` equivalents.
    

- Rule 4.3 (Hiding Turns): Set "show": false to execute a turn's logic (setup, calculations, data storage/retrieval, routing) without displaying its output to the user.
    

- Best Practice: All turns containing only control flow commands (`REPEAT`, `JUMP`, `END`) or non-user-facing data manipulation (`SET`, `LOAD`, `IMPORT`, `SAVE`, `EXPORT`) should have `"show": false`.
    
- Check: Verify `show: false` on turns with only control/data commands.
    

- Rule 4.4 (Final Output Formatting): For the final user-facing turn displaying results or a summary, it is recommended to set `"markdown": true`.
    

- Best Practice Check: Suggest adding `"markdown": true` to the last visible turn if it's likely to contain formatted text (headings, lists, bolding).
    

## 5. Turn Specifications (LLM vs. Symbolic)

Every turn is processed as either an LLM Turn or a Symbolic Turn based solely on the content of its "user" or "system" prompt string.

- Rule 5.1 **Symbolic Turn Triggers & Location (The User-Key Rule)**

- **Definition:** A turn is Symbolic if the logic flow relies on CAFA commands or comments rather than LLM generation.
    
- **Requirement 1 (Location):** The symbolic trigger (a leading `/` for comments) **MUST be placed at the very beginning line of the `user` key string**, and the system prompt should be empty.
    
    - ❌ Incorrect: `"system": "/ This is a comment", "user": "@TEXT@"` (Engine ignores system for triggers).
        
    - ✅ Correct: `"system": "", "user": "/ This is a comment\n@TEXT@"`
        
- **Requirement 2 (Model Nullification):** These turns must have `"model": null`.
    
- **Check:** Verify that every turn with `"model": null` has a `user` string starting with `/`.
    

- Rule 5.2 (LLM Turn  Trigger): A turn is processed as an LLM Turn (default behavior) if it does not meet the Symbolic trigger criteria.
    

- Crucial Rule: An LLM turn's `user` or `system` prompt must not start with `/`. This will force it into Symbolic mode, skipping the LLM entirely.
    
- Processing: Sends `system` and `user` prompts (after parameter substitution) to the specified language model.
    
- Check: Flag LLM turns where `user` or `system` starts with `/`.
    

- Rule 5.3 (Symbolic Turn Commenting): Developer comments are allowed only within Symbolic Turns.
    

- Syntax: Any text following a `/` on the same line is ignored until the next line break (`\n`).
    
- Limit: Only one comment line (starting with `/`) is permitted per Symbolic turn prompt (`user` or `system`). Multiple lines starting with `/` are not supported for commenting.
    
- Example (Correct): `"user": "/` This comment is ignored.\nThis content is processed."
    
- Example (Incorrect): `"user": "/ `First comment line.\n/ Second comment line.\nThis content is processed."
    
- Usage: Use `/`, ` `, `\n` (slash, space, newline) if you need a symbolic turn to display content but have no comment.
    
- Check: Ensure comment syntax is used correctly only in Symbolic turns and that only one line starts with `/`.
    

- Rule 5.4 (User Input in LLM Turn): Setting `"user": ""` in an LLM turn pauses the agent to await user input.
    

- Info: This is the standard way to make an LLM turn interactive.
    

### 5.5 Turn Property Requirements Table

Adhere to these property requirements for clarity and performance.

|   |   |   |   |
|---|---|---|---|
|Property|LLM Turn 🤖|Symbolic Turn ⚙️|Notes|
|`"system"`|Required|Required|String. Can be `""`. Can contain `/` or command to trigger Symbolic.|
|`"user"`|Required|Required|String. Can be `""`. `""` in LLM Turn awaits user input.|
|`"show"`|Required|Required|`Boolean` (`true` or `false`).|
|`"model"`|Required|Omit|String (e.g., `"gpt-4.1-nano"`). Unnecessary, omit for Symbolic.|
|`"temperature"`|Optional|Omit|`String/Number` (e.g., `0.1`). Defaults to `0.1`. Unnecessary.|
|`"max-tokens"`|Optional|Omit|`String/Number` (e.g., `2000`). Defaults to `2000`. Unnecessary.|
|`"output-values"`|Optional|Omit|`String` (List `A|
|`"markdown"`|Optional|Optional|`Boolean` (`true` or `false`). Recommended true for final output.|

- Check (Symbolic): Flag if model, temperature, max-tokens, or output-values keys are present. They should be omitted.
    
- Check (LLM): Ensure model key is present and has a non-null string value. Ensure system, user, show are present.
    

## 6. Command Syntax & Rules

CAFA commands (format: `@COMMAND(arguments)@`) orchestrate logic and follow strict syntax.

### 6.1 General Command Rules

- Rule 6.1.1 (Double Quotes Only for Args): All arguments for all CAFA commands must be enclosed in double quotes (`"`). Single quotes (`'`) are forbidden. Numbers used as arguments must also be quoted strings (e.g., `@REPEAT("2", "5", "3")@`).
    

- Check: Validate syntax for all command arguments. Flag any using single quotes or unquoted numbers.
    

- Rule 6.1.2 (Dedicated Control Flow Turns): Commands that control the execution path (`@REPEAT()@`, `@JUMP()@`, `@END@`) must reside in their own dedicated, hidden (`"show": false`) symbolic turn, and be the only command or text in that turn's prompt string.
    

- Check: Ensure these commands appear alone in a Symbolic turn with `"show": false`.
    

- Rule 6.1.3 (Command Formatting Reference): When referencing commands in documentation or explanations, use the full syntax (`@SET()@`) or the uppercase name (`SET`). Never use only the leading `@` (`@SET`).
    

- Info: Style guide for documentation.
    

### 6.2 Specific Command Rules & Behavior

- `SET`
    - Atomicity / Dependency Rule: Commands within a single turn are processed simultaneously (atomically). Therefore, a parameter created or modified using `SET` in a turn is not guaranteed to be available to other commands within that same turn. It is only reliably available in subsequent turns. Do not `SET` ParamA and use ParamA (e.g., in `EVAL`, `MAP`, another `SET`, or as part of a prompt string being processed by the system or LLM) within the same turn.
        - Check: Detect if a parameter name assigned via `SET` is referenced by another command within the same turn's prompt string.
    

- `MAP`
    - Rule
        1. `return_list` must have exactly one more item (`N+1`) than `value_list` (`N`). 
        2. The last item is the default. End `return_list` with a pipe character for a `null/empty` default.
    

- `EVAL`
    - Executes JavaScript math/logic expressions. Can access standard Math object methods (e.g., `Math.sqrt()`, `Math.random()`, `Math.PI`). Handles basic arithmetic ($+$, $-$, $\times$, $\div$, $\bmod$, $**$) and comparisons (`>`, `>=`, `==`, `!=`, `<=`, `<`). 
    - Rule
        1. Respects the Atomicity/Dependency Rule for parameters used inside.
        2. Refer `General Rule 6.1.1`
    

- `INDEX`
    - Rule
        1. Returns `1-based index`; returns `0` if not found. 
        2. Case-sensitive search.
    

- `REPEAT`
    - Rules
        1. Must be in its own dedicated hidden turn. 
        2. `turn_start` argument must refer to a turn after the current turn. 
        3. Refer Rule 6.1.1
        4. Dynamic Turn Referencing: `TN()` 
    
    - Loop-Result Indexing Rule: Results of turns executed inside a `REPEAT` loop accumulate across iterations into a single pipe-delimited System Parameter. A reference to a loop-internal `TR`/`TU`/`TS` (e.g. `@TR@TN(-1)@@`) therefore returns the full accumulated list, not the current iteration's value. When that value is consumed by another command (`MAP`, `INDEX`, `EVAL`, `SET`) or stored, it MUST be indexed by the iteration number: `@TR@TN(-1)@[@R_i@]@`. Un-indexed access is correct only when the full accumulated list is intentionally wanted.
        - Check: Flag a loop-internal `@TR...@` / `@TU...@` / `@TS...@` fed into `MAP`/`INDEX`/`EVAL`/`SET` without a trailing `[@R_i@]` (or explicit iteration index). Common symptom: `MAP` returns its default on iterations ≥ 2 and per-iteration `SET` variables store a growing pipe-delimited string.
    

- `JUMP`
    - Rule
        1. Must be in its own dedicated hidden turn. 
        2. Refer `General Rule 6.1.1`
        3. Dynamic Turn Referencing: `TN()` 
    

- `END`
    - Rule
        1. Must be in its own dedicated hidden turn. 
        2. Immediately terminates the agent session.
    

#### Input Controls (`RADIO`, `CHECKBOX`, `TEXT`, `TEXTAREA`, `SELECT`)
    

- Default (recommended): one input control command per visible (`"show": true`) turn. Displaying input control(s) pauses the agent and automatically generates a single "Submit" button.
- Multiple input controls per visible turn are supported by the engine (one Submit gathers all). Every non-`CHECKBOX` control (`RADIO`, `TEXT`, `TEXTAREA`, `SELECT`) must be filled before Submit proceeds; a `CHECKBOX` may be left unchecked.
    

- `RADIO` (Extended)
    - Optional 4th argument (other_prompt) adds a text box (for `SCREAM` framework). Retrieval via `@RADIO("name")@` returns a pipe-separated string: `"SelectedOption|WrittenText"`. Without the 4th arg, it returns only the selected option.
    

- `SAVE`
    - Agent must be saved on platform first. Default action for `ID="LOG"` is append. To overwrite the `LOG`, the third argument must be explicitly `"false"`.
    

- `LOAD`
    - Separation Rule / Dependency Rule: `LOAD` data in one turn, then use/process it in a subsequent turn. The loaded data is not available within the same turn it is loaded.
        - Check: Detect usage of data loaded via `LOAD` within the same turn.
    

- `EXPORT`
    - Bundles specified `AP`s into an Ontology Model package. Default action for `ID="LOG"` is overwrite (replaces entire log). Agent must be saved first.
    

- `IMPORT`
    - Loads Ontology Model package and auto-`SET`s contained `AP`s. 
    - Separation Rule / Dependency Rule: `IMPORT` in one turn, use the imported parameters in subsequent turns. Parameters are not available within the same turn `IMPORT` is called.
        - Check: Detect usage of parameters populated via `IMPORT` within the same turn.
    

- `GS`
    - Fetches raw data from Google Sheet as a double-delimited string: `Row1Cell1&Row1Cell2` pipe-separated by `Row2Cell1&Row2Cell2`. 
    - Sheet requires "Anyone with link can view" permission.
    

- `GSTABLE`
    - Imports Google Sheet table, auto-creates `AP`s from headers (default behavior) or P1, P2... (if "NO" option is used as 3rd arg). 
    - Sheet requires "Anyone with link can view" permission. 
    - Respects the Atomicity/Dependency rule (use imported parameters in subsequent turns).
    

- `TTS`
    - Text-to-Speech. 
    - Symbolic command. 
    - Generates a button if caption argument is non-empty ("Click Me"). 
    - Plays audio automatically if caption is `""`. 
    - Recommended: one interactive command (`@TTS` with button, `@RADIO`, etc.) per visible turn. Multiple input controls are engine-supported (see Input Controls above).
    

#### output-values (Turn Property, not a command)
- Hard constraint on LLM output format (e.g., a pipe-separated list like "`Low|Medium|High`" or a JSON schema like "`{\"key\":\"ValueA|ValueB\"}`"). 
- Critical for reliable downstream symbolic logic (`MAP`, `EVAL`, `INDEX`) that processes LLM output.
    

## 7. Agent Parameter (`AP`) Specification

Rules for defining and accessing Agent Parameters (`AP`s).

### 7.1 Definition (in `options.params` or via `SET`)

- Structure (`options.params`): Each `AP` is a key-value pair. 
    - Key = parameter name (string). 
    - Value = object with required `"org"` (string) and `"cond"` (string) keys
        - optional `"desc"` (string).
        - `"org"`: String containing the value(s). Use pipe (`|`) for multiple values/list items. Avoid `|` and `@` within actual data values themselves.
        - `"cond"`: Required for standard `AP`s (holding simple strings or pipe-separated lists). Must be one of: `"SELF"`, `"SHUFFLE"`, `"SORT"`, `"DSORT"`, or `"LINK(TargetParameter)"`. 
- Controls ordering/linking.
    
#### Agent Parameters Properties
- `"SELF"`: Preserves original order.
- `"SHUFFLE"`: Randomizes order per session.
- `"SORT"`: Sorts ascending (A-Z, 0-9).
- `"DSORT"`: Sorts descending (Z-A, 9-0).
- `"LINK(TargetParameter)"`: Mirrors the order of TargetParameter. Crucial for parallel lists/Ontology Models. TargetParameter cannot be "SELF" if dynamic ordering is needed via the link.
- `"desc"`: Optional, but highly recommended. String for developer documentation explaining the parameter's purpose.

#### General Rules
- Rule 7.1.1 (Description Best Practice): Always include a meaningful `"desc"` key for parameters defined in options.params. This significantly improves code readability, maintainability, and semantic expressiveness, making the agent's ontology model easier to understand.
    - Check: Verify that standard `AP`s in `options.params` have a `"desc"` key with a non-empty string value.
    - Check: Verify that standard `AP`s in `options.params` have a valid `"cond"` value.
    
- Definition (`SET`): `@SET("ParamName", "Value1|Value2"[, "cond"])@`. Creates or modifies `AP` during execution.
- Default `cond`: If the optional `"cond"` argument is omitted when using the `SET` command, it defaults to `"SELF"`.
- Respect `SET` Atomicity/Dependency Rule (Rule 6.2).
    

### 7.2 Accessing APs

- `@ParamName[index]@`: Retrieves the item at the specified **1-based index**.
    
- `@ParamName[N]@`: Retrieves the total number of items in the list.
    
- `@ParamName[.]@`: Retrieves a single randomly chosen item from the list.
    
- `@ParamName[start:end]@`: Retrieves a sublist (slice) from start index to end index (**inclusive**).
    
- `@ParamName@`: Retrieves the entire pipe-separated string (useful for `MAP`'s `value_list` or `INDEX`'s `list`).
    
- Indirection: Use double-at syntax (`@@ParamNameContainingAnotherParamName@[index]@`) to dynamically access a parameter whose name is stored within another parameter.
    

## 8. System Parameter (SP) Specification

Provide contextual information about the agent's state. Always accessed using `@SP_NAME@`.

- Common `SP`s:
    - `@TUt[index]@`: User prompt content from turn `t` (optional index for loop results). Use `TN()` for `t`.
        
    - `@TRt[index]@`: Result (LLM response or Symbolic output) from turn `t`. Use `TN()` for `t`.
        
    - `@TSt[index]@`: System prompt content from turn `t`. Use `TN()` for `t`.
        
    - `@R_i@`: Current iteration number (**1-based**) within a `REPEAT()` loop.
        
    - `@R_s@`, `@R_e@`, `@R_n@`: Start turn, end turn, total repetitions for the current `REPEAT()` loop.
        
    - `@UID@`: Unique User Identifier for the current session user.
        
    - `@DATE@`, `@TIME@`: Current date and time (at the moment the turn executes).
    

## 9. Data Integrity & State Management Best Practices

Essential for stateful (memory-based) and multi-user agents.
### Rules
- Rule 9.1 (Sanitize User Input): User input intended for storage (especially `LOG`) or use in list-based commands must be validated or sanitized to remove reserved CAFA characters (`|`, `@`) to prevent data corruption and command injection/parsing errors.
    - Best Practice Check: Recommend adding validation/sanitation steps before saving user-provided free text.
- Rule 9.2 (Separation of Concerns for Data Ops): Strictly separate data operations into distinct, sequential turns following the Atomicity/Dependency rule:
    1. `LOAD` / `IMPORT` (Turn `N`)
    2. `MODIFY` (Operate on in-memory parameters using `SET`, `EVAL`, `INDEX` etc.) (Turn `N+1`)
    3. `SAVE` / `EXPORT` (Turn `N+2`)
    - Check: Detect violations of this Load → Modify → Save pattern across separate turns. Ensure data loaded/imported in Turn N is not used until Turn `N+1`.
    

- Rule 9.3 (Concurrency Golden Rule for `LOG` Updates): When updating data loaded from the `LOG` in a potentially multi-user context:
    

1. Get user input needed for the update (Turn `N`).
    
2. `MODIFY` Step (Hidden Turn `N+1`):
    

- Re-`LOAD` or `IMPORT` the `LOG` data into a temporary parameter (e.g., `TEMP_LOG_DATA`).
    
- Re-`INDEX` to find the specific user/record's current position within `TEMP_LOG_DATA`.
    
- `SET` the changes within the `TEMP_LOG_DATA` parameter using the calculated index.
    

3. `SAVE` Step (Hidden Turn `N+2`):
    - `SAVE` or `EXPORT` the entire modified `TEMP_LOG_DATA` parameter back to the `LOG`, overwriting the previous state (`"false"` for `SAVE`, default for `EXPORT`).
        - Check: Verify this Re-Fetch → Re-Index → Modify-in-Memory → Save-Modified pattern for `LOG` updates, ensuring separation of `LOAD/IMPORT`, modification, and `SAVE/EXPORT` across turns.
    

- Rule 9.4 (Initialize Stateful Parameters): Pre-define parameters that will be loaded via `IMPORT` (especially from `"LOG"`) with default empty values (e.g., `"org": ""`) in `options.params`.
    - Benefit: Prevents errors on the very first run when the `LOG` is empty and the parameters don't exist yet.
        - Check: Ensure parameters used in `@IMPORT("LOG")@` are also defined in `options.params`.
- Rule 9.5 (`LOG` is Not Permanent Storage): Treat Agent Data (`DID`s) and Agent Log (`LOG`) as transitional or semi-persistent storage. Do not rely on them for critical, long-term data archival.
- Best Practice: Recommend backing up or exporting critical LOG data to external storage (e.g., Google Sheets via `IMPORTDATA`) for long-term needs and robust analytics.
