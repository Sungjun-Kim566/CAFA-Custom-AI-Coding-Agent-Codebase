CAFA Protocol: Technical Protocol Specification and Commands
- **Version:** 2025.12 
- **Scope:** Syntax, Commands, Data Structures
- **Target Audience:** Developers, Agent Modelers 
- **Description:** This document serves as the comprehensive technical reference for creating CAFA agents, detailing the mandatory JSON structure, the hierarchy of parameter systems (AP, SP, JP), and the syntax for all logic, flow control, UI, mathematics, and visualization commands.

# Master Index for CAFA Protocol

## 1. Agent Architecture

- CAFA Agent Code Linter and Rules
- Agent Code Elements and Structure (ACES): Technical Specification and Logic
        
- Turn Types (LLM vs. Symbolic): Hybrid Logic Execution Modes
    
    - **Keywords:** Turns LLM; Symbolic Flow Control; HybridAI; Execution Mode; Logic Separation
        

## 2. Parameter Systems (AP, SP, JP)

- Agent Parameters (AP): Ontology Model and Local Variable Storage
    
    - **Keywords:** Parameters AP; Variable Assignment; Local Scope; Ontology Model; Data Storage
        
- System Parameters (SP): Runtime Context Variables
    
    - **Keywords:** Parameters SP; Runtime Context; Turn Reference; User ID; System Scope
        
- JSON Parameters (JP): Complex Object Data Handling
    
    - **Keywords:** Parameters JP; Complex Data; JSON Objects; Arrays; Ontology Model Handling
        

## 3. Logic & Flow Control Commands

- **SET Command: Define and Update Agent Parameters**
    
    - **Keywords:** SET; VariableAssignment; DataManipulation; StateManagement; APUpdate; Logic
- TN Command: Relative Turn Numbering
        
- **SETJ Command: Define and Update JSON Parameters**
    
    - **Keywords:** SETJ; JSON; DataManipulation; ComplexData; ObjectCreation; JPSyntax; StateManagement
        
- **JSONVALS Command: Extract Values from JSON Object**
    
    - **Keywords:** JSONVALS; Extraction; DataParsing; ArrayConversion; ValuesOnly; JSONUtility
        
- **EVAL Command: Execute JavaScript Math and Logic**
    
    - **Keywords:** EVAL; Math; Logic Ternary; Calculation; JavaScript; ConditionalLogic; Expression
- **EVAL Command: Ternary Logic Gates**
            
- **MAP Command: Route Logic via Conditional Lookup**
    
    - **Keywords:** MAP; ConditionalLogic; Routing Lookup; FlowControl; N+1Rule; DataMatching
        
- **REPEAT Command: Iterate and Loop Through Turns**
    
    - **Keywords:** REPEAT; Loop; Iteration FlowControl; MultiTurn; Workflow; Automation
        
- **JUMP Command: Control Execution Flow and Branching**
    
    - **Keywords:** JUMP; Branching; Routing FlowControl; NonLinear; LogicGate; Sequence
        
- **END Command: Terminate and Close Agent Session**
    
    - **Keywords:** END; Exit; Termination; SessionControl; Stop; FlowControl
        
- **INDEX Command: Retrieving Knowledge from Tabular Ontology Models**
    
    - **Keywords:** INDEX; Search; Lookup Retrieval; 1BasedIndexing; Ontology; ListSearch
- **COMPARE Command: Element-wise List Comparison**
- EQUAL Command: Holistic List Equality and Pattern Matching
- FILTER Command: Conditional List Creation
- **D Command: Generate Distractors for Multiple Choice**
    
    - **Keywords:** D; Distractor; AIG Generation; ADAM; Assessment; ItemModeling; Choices
        
## 4. Data Persistence & I/O Commands

- **SAVE Command: Persist Data to System Log**
    
    - **Keywords:** SAVE; Persistence; Log Memory Write; Storage; DataID; State
        
- **LOAD Command: Retrieve Data from Artifacts or Log**
    
    - **Keywords:** LOAD; Retrieval; Memory Read; DID; DataAccess; StateRecovery
- **EXPORT Command: Serialize and Persist Structured Ontology Models**
    
    - **Keywords:** EXPORT; DataOutput; FileGeneration; Download; JSONExport; CSVExport     
    - 
- **IMPORT Command: Load Content from External Modules**
    
    - **Keywords:** IMPORT; ContentLoading; ExternalSource; DataIngestion; Integration; ModuleLoading
      
- **GS Command: Fetch Raw Data from Google Sheets**
    
    - **Keywords:** GS; GoogleSheets; ExternalData; Fetch; RawData; Import; IO
        
- **GSTABLE Command: Import Google Sheet as Data Table**
    
    - **Keywords:** GSTABLE; GoogleSheets; TableImport; Ontology; ExternalData; APCreation; Database
        
- **RUN Command: Execute Asynchronous Background Agent Process**
    
    - **Keywords:** RUN; MacroRun; Asynchronous Automation; BackgroundProcess; Orchestration; MultiAgent
                
## 5. UI & Interactive Commands

- **RADIO Command: Select Single Option via Radio Buttons**
    
    - **Keywords:** RADIO; UI; Input Form; Selection; UserInteraction; MultipleChoice; Control
        
- **CHECKBOX Command: Select Multiple Options via Checkboxes**
    
    - **Keywords:** CHECKBOX; UI; Input Form; MultiSelect; UserInteraction; ListSelection; Control
        
- **TEXT Command: Input Short Single Line Text**
    
    - **Keywords:** TEXT; UI; Input Form; UserInteraction; SingleLine; Control
        
- **TEXTAREA Command: Input Long Multi Line Text Block**
    
    - **Keywords:** TEXTAREA; UI; Input Form; UserInteraction; MultiLine; Control
        
- **SELECT Command: Choose Option from Dropdown Menu**
    
    - **Keywords:** SELECT; UI; Input Form; UserInteraction; Selection; Control
        
- **TTS Command: Output Audio via Text to Speech**
    
    - **Keywords:** TTS; Audio Output; Accessibility; SpeechSynthesis; Voice; UserInteraction
        

## 6. Math & Visualization Commands

- **MATH Command: Specialized Symbolic Mathematical Operations**
    
    - **Keywords:** MATH; Calculation; Functions Trigonometry; Combinatorics; Rounding; Scientific
        
- **FR Command: Format Fraction for Display Output and Arithmetic**
    
    - **Keywords:** FR; Fraction; LaTeX Display; MathOutput; Formatting; Arithmetic
        
- **FRADD Command: Symbolic Fraction Addition**
    
    - **Keywords:** FRADD; Arithmetic; Calculation Fraction; MathOutput; SymbolicMath; Operation
- **FRSUB Command: Symbolic Fraction Subtraction**
        
- **FRMULT Command: Symbolic Fraction Multiplication**
    
    - **Keywords:** FRMULT; Arithmetic; Calculation Fraction; MathOutput; SymbolicMath; Operation
- **FRDIV Command: Symbolic Fraction Division**
- **FRREC Command: Symbolic Fraction Reciprocal**
- **FRVAL Command: Convert Symbolic Fraction to Decimal Value**
- **SIMPLIFY Command: Reduce Fractions to Lowest Terms**
        
- **POLY Command: Format and Display Polynomials**
    
    - **Keywords:** POLY; Polynomial; LaTeX Display; Algebra; MathOutput; Formatting; Expression
        
- **POLYDISP Command: Display Polynomial in Math Mode**
    
    - **Keywords:** POLYDISP; Polynomial; LaTeX Display; Visualization; MathOutput; Formatting; Output
        
- **POLYEVAL Command: Calculate Numerical Value of Polynomial**
    
    - **Keywords:** POLYEVAL; Polynomial; Evaluation Calculation; Math; Numerical; Substitution; Function
        
- **POLYDIFF Command: Symbolic Polynomial Differentiation**
    
    - **Keywords:** POLYDIFF; Calculus; Differentiation; SymbolicMath; MathOutput; Algebra; Derivative
        
- **POLYINT Command: Compute Symbolic Integral of Polynomial**
    
    - **Keywords:** POLYINT; Calculus; Integration; SymbolicMath; MathOutput; Algebra; Integral
        
- **MERMAID Command: Render Flowcharts and Diagrams Code**
    
    - **Keywords:** MERMAID; Visualization; Flowchart Diagrams; ProcessMapping; CodeToImage; Display
        

# CAFA Agent Code Linter and Rules

20251023
## 1. Introduction

This document serves as a comprehensive guide and checklist for the syntax rules, best practices, and potential pitfalls when developing CAFA (Collective AI on the Foundation AI) agents. Adhering to these rules is essential for creating valid, functional, reliable, and maintainable agents on the CAFA platform. Use this guide for linting (analyzing code for potential errors), code reviews, and ensuring compliance with the CAFA Protocol.

## 2. General JSON Structure & Syntax

The foundation of every CAFA agent is a single, valid JSON object.

- Rule 2.1 (Valid JSON): The entire agent code must strictly adhere to JSON formatting rules.
	-  Check: Validate the entire code block using a JSON validator.
- Rule 2.2 (Root Keys): The root object must contain exactly two keys: "options" (a JSON object) and "prompts" (a JSON array).
	-  Check: Verify the presence and types of "options" and "prompts" at the root level.    

- Rule 2.3 (Double Quotes): All JSON keys and string values must be enclosed in double quotes ("). Single quotes (') are forbidden.
    - Check: Scan for single quotes used for keys or string values.
    
- Rule 2.4 (No Trailing Commas): Trailing commas after the last element in an object or array are not allowed.
    - Check: Detect trailing commas.
    
- Rule 2.5 (No JSON Comments): Standard JSON does not support comments (//, /* */). Agent code must not contain JSON comments.
    - Exception: Use Symbolic Turn commenting (/ Comment\n) for in-code notes (See Section 5.3). Use the "desc" field in parameters for documentation.
    - Check: Detect JSON comment syntax.
    
- Rule 2.6 (Character Escaping): Avoid unnecessary or incorrect character escaping.
    - Backslashes: Never use a double backslash (\\). For literal newlines within strings (primarily in Symbolic Turn comments or specific string formatting), use a single escaped newline (\n). Double quotes within string values must be escaped (\").
    - Square Brackets: Never use escaped square brackets (\[ or \]). Use standard, unescaped brackets ([ and ]) for all parameter access and list slicing (e.g., @AP[1:3]@).
    - Check: Detect \\, \[, \]. Ensure " within strings are escaped as \".
    
## 3. Agent Configuration: The options Object

This object contains agent metadata and pre-defined Agent Parameters (APs).

- Rule 3.1 (Metadata Keys): Must include standard string keys: "title", "brief", "name", "description", and "greeting".
    - Info: The "title" field can accept basic HTML tags for formatting.
    -  Check: Verify the presence and string type of these keys.
    
- Rule 3.2 (params Object): This nested object is the designated location for pre-defining Agent Parameters (APs) – the agent's static knowledge base or ontology model.
    - Best Practice: Store all static data (quiz questions, personas, rubrics, fixed lists, initial state variables) here. This separates content from logic, improving maintainability and modularity.
    - See Section 7 for detailed AP definition rules within params.
    

## 4. Workflow Definition: The prompts Array

This array defines the agent's step-by-step workflow. Each element must be a valid JSON object representing a single turn.

- Rule 4.1 (Turn Object Structure): Each turn object requires specific properties based on its type (See Section 5).
    
- Rule 4.2 (Relative Turn Numbering - TN): Always use the TN() command for references between turns (e.g., @TR@TN(-1)@@, @JUMP(@TN(2)@)@) instead of hardcoded absolute numbers (e.g., @TR1@, @JUMP(3)@).
    

- Benefit: Makes agent logic robust against adding/removing turns during development.
    
- Check: Detect hardcoded turn references like @TR1@, @TU2@ and suggest replacing them with TN() equivalents.
    

- Rule 4.3 (Hiding Turns): Set "show": false to execute a turn's logic (setup, calculations, data storage/retrieval, routing) without displaying its output to the user.
    

- Best Practice: All turns containing only control flow commands (REPEAT, JUMP, END) or non-user-facing data manipulation (SET, LOAD, IMPORT, SAVE, EXPORT) should have "show": false.
    
- Check: Verify show: false on turns with only control/data commands.
    

- Rule 4.4 (Final Output Formatting): For the final user-facing turn displaying results or a summary, it is recommended to set "markdown": true.
    

- Best Practice Check: Suggest adding "markdown": true to the last visible turn if it's likely to contain formatted text (headings, lists, bolding).
    

## 5. Turn Specifications (LLM vs. Symbolic)

Every turn is processed as either an LLM Turn or a Symbolic Turn based solely on the content of its "user" or "system" prompt string.

- Rule 5.1 (Symbolic Turn Trigger): A turn becomes Symbolic if its "user" or "system" prompt string starts with:
    

- A forward slash (/)
    
- OR a control flow command (@REPEAT()@, @JUMP()@, @END@).
    
- Processing: Bypasses the LLM. Commands are executed directly by the CAFA system.
    
- Check: Identify turns starting with / or control commands as Symbolic.
    

- Rule 5.2 (LLM Turn  Trigger): A turn is processed as an LLM Turn (default behavior) if it does not meet the Symbolic trigger criteria.
    

- Crucial Rule: An LLM turn's "user" or "system" prompt must not start with /. This will force it into Symbolic mode, skipping the LLM entirely.
    
- Processing: Sends "system" and "user" prompts (after parameter substitution) to the specified language model.
    
- Check: Flag LLM turns where "user" or "system" starts with /.
    

- Rule 5.3 (Symbolic Turn Commenting): Developer comments are allowed only within Symbolic Turns.
    

- Syntax: Any text following a / on the same line is ignored until the next line break (\n).
    
- Limit: Only one comment line (starting with /) is permitted per Symbolic turn prompt ("user" or "system"). Multiple lines starting with / are not supported for commenting.
    
- Example (Correct): "user": "/ This comment is ignored.\nThis content is processed."
    
- Example (Incorrect): "user": "/ First comment line.\n/ Second comment line.\nThis content is processed."
    
- Usage: Use / \n (slash, space, newline) if you need a symbolic turn to display content but have no comment.
    
- Check: Ensure comment syntax is used correctly only in Symbolic turns and that only one line starts with /.
    

- Rule 5.4 (User Input in LLM Turn): Setting "user": "" in an LLM turn pauses the agent to await user input.
    

- Info: This is the standard way to make an LLM turn interactive.
    

### 5.5 Turn Property Requirements Table

Adhere to these property requirements for clarity and performance.

|   |   |   |   |
|---|---|---|---|
|Property|LLM Turn 🤖|Symbolic Turn ⚙️|Notes|
|"system"|Required|Required|String. Can be "". Can contain / or command to trigger Symbolic.|
|"user"|Required|Required|String. Can be "". "" in LLM Turn awaits user input.|
|"show"|Required|Required|Boolean (true or false).|
|"model"|Required|Omit|String (e.g., "gpt-4.1-nano"). Unnecessary, omit for Symbolic.|
|"temperature"|Optional|Omit|String/Number (e.g., "0.1"). Defaults to 0.1. Unnecessary.|
|"max-tokens"|Optional|Omit|String/Number (e.g., "2000"). Defaults to 2000. Unnecessary.|
|"output-values"|Optional|Omit|String (List `A|
|"markdown"|Optional|Optional|Boolean (true or false). Recommended true for final output.|

- Check (Symbolic): Flag if model, temperature, max-tokens, or output-values keys are present. They should be omitted.
    
- Check (LLM): Ensure model key is present and has a non-null string value. Ensure system, user, show are present.
    

## 6. Command Syntax & Rules

CAFA commands (@COMMAND(...)@) orchestrate logic and follow strict syntax.

### 6.1 General Command Rules

- Rule 6.1.1 (Double Quotes Only for Args): All arguments for all CAFA commands must be enclosed in double quotes ("). Single quotes (') are forbidden and will cause errors. Numbers used as arguments must also be quoted strings (e.g., @REPEAT("2", "5", "3")@).
    

- Check: Validate syntax for all command arguments. Flag any using single quotes or unquoted numbers.
    

- Rule 6.1.2 (Dedicated Control Flow Turns): Commands that control the execution path (@REPEAT()@, @JUMP()@, @END@) must reside in their own dedicated, hidden ("show": false) symbolic turn, and be the only command or text in that turn's prompt string.
    

- Check: Ensure these commands appear alone in a Symbolic turn with "show": false.
    

- Rule 6.1.3 (Command Formatting Reference): When referencing commands in documentation or explanations, use the full syntax (@SET()@) or the uppercase name (SET). Never use only the leading @ (@SET).
    

- Info: Style guide for documentation.
    

### 6.2 Specific Command Rules & Behavior

- SET
    

- Atomicity / Dependency Rule: Commands within a single turn are processed simultaneously (atomically). Therefore, a parameter created or modified using SET in a turn is not guaranteed to be available to other commands within that same turn. It is only reliably available in subsequent turns. Do not SET ParamA and use ParamA (e.g., in EVAL, MAP, another SET, or as part of a prompt string being processed by the system or LLM) within the same turn.
    
- Check: Detect if a parameter name assigned via SET is referenced by another command within the same turn's prompt string.
    

- MAP
    

- return_list must have exactly one more item (N+1) than value_list (N). The last item is the default. End return_list with a pipe character for a null/empty default.
    

- EVAL
    

- Executes JavaScript math/logic expressions. Can access standard Math object methods (e.g., Math.sqrt(), Math.random(), Math.PI). Handles basic arithmetic (+, -, *, /, %, **) and comparisons (>, >=, ==, !=, <=, <). Respects the Atomicity/Dependency Rule for parameters used inside.
    

- INDEX
    

- Returns 1-based index; returns 0 if not found. Case-sensitive search.
    

- REPEAT
    

- Must be in its own dedicated hidden turn. turn_start argument must refer to a turn after the current turn. All arguments (start, end, number) must be quoted strings. Use TN() for robustness.
    
- Loop-Result Accumulation: Results of turns inside the loop accumulate across iterations into pipe-delimited SPs. To read a single iteration's value, index it with `[@R_i@]` (e.g. `@TR@TN(-1)@[@R_i@]@`). See Section 8.1.
    

- JUMP
    

- Must be in its own dedicated hidden turn. Target turn argument must be a quoted string. Use TN() for robustness.
    

- END
    

- Must be in its own dedicated hidden turn. Immediately terminates the agent session.
    

- Input Controls (RADIO, CHECKBOX, TEXT, TEXTAREA, SELECT)
    

- Only one input control command per visible ("show": true) turn. Displaying an input control pauses the agent and automatically generates a "Submit" button.
    

- RADIO (Extended)
    

- Optional 4th argument (other_prompt) adds a text box (for SCREAM framework). Retrieval via @RADIO("name")@ returns a pipe-separated string: "SelectedOption|WrittenText". Without the 4th arg, it returns only the selected option.
    

- SAVE
    

- Agent must be saved on platform first. Default action for ID="LOG" is append. To overwrite the LOG, the third argument must be explicitly "false".
    

- LOAD
    

- Separation Rule / Dependency Rule: LOAD data in one turn, then use/process it in a subsequent turn. The loaded data is not available within the same turn it is loaded.
    
- Check: Detect usage of data loaded via LOAD within the same turn.
    

- EXPORT
    

- Bundles specified APs into an Ontology Model package. Default action for ID="LOG" is overwrite (replaces entire log). Agent must be saved first.
    

- IMPORT
    

- Loads Ontology Model package and auto-SETs contained APs. Separation Rule / Dependency Rule: IMPORT in one turn, use the imported parameters in subsequent turns. Parameters are not available within the same turn IMPORT is called.
    
- Check: Detect usage of parameters populated via IMPORT within the same turn.
    

- GS
    

- Fetches raw data from Google Sheet as a double-delimited string: Row1Cell1&Row1Cell2 pipe-separated by Row2Cell1&Row2Cell2. Sheet requires "Anyone with link can view" permission.
    

- GSTABLE
    

- Imports Google Sheet table, auto-creates APs from headers (default behavior) or P1, P2... (if "NO" option is used as 3rd arg). Sheet requires "Anyone with link can view" permission. Respects the Atomicity/Dependency rule (use imported parameters in subsequent turns).
    

- TTS
    

- Text-to-Speech. Symbolic command. Generates a button if caption argument is non-empty ("Click Me"). Plays audio automatically if caption is "". Only one interactive command (@TTS with button, @RADIO, etc.) per visible turn.
    

- output-values (Turn Property, not a command)
    

- Hard constraint on LLM output format (e.g., a pipe-separated list like "Low|Medium|High" or a JSON schema like "{\"key\":\"ValueA|ValueB\"}"). Critical for reliable downstream symbolic logic (MAP, EVAL, INDEX) that processes LLM output.
    

## 7. Agent Parameter (AP) Specification

Rules for defining and accessing Agent Parameters (APs).

### 7.1 Definition (in options.params or via SET)

- Structure (options.params): Each AP is a key-value pair. Key = parameter name (string). Value = object with required "org" (string) and "cond" (string) keys, optional "desc" (string).
    

- "org": String containing the value(s). Use pipe (|) for multiple values/list items. Avoid | and @ within actual data values themselves.
    
- "cond": Required for standard APs (holding simple strings or pipe-separated lists). Must be one of: "SELF", "SHUFFLE", "SORT", "DSORT", or "LINK(TargetParameter)". Controls ordering/linking.
    

- "SELF": Preserves original order.
    
- "SHUFFLE": Randomizes order per session.
    
- "SORT": Sorts ascending (A-Z, 0-9).
    
- "DSORT": Sorts descending (Z-A, 9-0).
    
- "LINK(TargetParameter)": Mirrors the order of TargetParameter. Crucial for parallel lists/Ontology Models. TargetParameter cannot be "SELF" if dynamic ordering is needed via the link.
    

- "desc": Optional, but highly recommended. String for developer documentation explaining the parameter's purpose.
    

- Rule 7.1.1 (Description Best Practice): Always include a meaningful "desc" key for parameters defined in options.params. This significantly improves code readability, maintainability, and semantic expressiveness, making the agent's ontology model easier to understand.
    
- Check: Verify that standard APs in options.params have a "desc" key with a non-empty string value.
    

- Check: Verify that standard APs in options.params have a valid "cond" value.
    

- Definition (SET): @SET("ParamName", "Value1|Value2"[, "cond"])@. Creates or modifies AP during execution.
    

- Default cond: If the optional "cond" argument is omitted when using the SET command, it defaults to "SELF".
    
- Respect SET Atomicity/Dependency Rule (Rule 6.2).
    

### 7.2 Accessing APs

- @ParamName[index]@: Retrieves the item at the specified 1-based index.
    
- @ParamName[N]@: Retrieves the total number of items in the list.
    
- @ParamName[.]@: Retrieves a single randomly chosen item from the list.
    
- @ParamName[start:end]@: Retrieves a sublist (slice) from start index to end index (inclusive).
    
- @ParamName@: Retrieves the entire pipe-separated string (useful for MAP's value_list or INDEX's list).
    
- Indirection: Use double-at syntax (@@ParamNameContainingAnotherParamName@[index]@) to dynamically access a parameter whose name is stored within another parameter.
    

## 8. System Parameter (SP) Specification

Provide contextual information about the agent's state. Always accessed using @SP_NAME@.

- Common SPs:
    

- @TUt[index]@: User prompt content from turn t (optional index for loop results). Use TN() for t.
    
- @TRt[index]@: Result (LLM response or Symbolic output) from turn t. Use TN() for t.
    
- @TSt[index]@: System prompt content from turn t. Use TN() for t.
    
- @R_i@: Current iteration number (1-based) within a REPEAT() loop.
    
- @R_s@, @R_e@, @R_n@: Start turn, end turn, total repetitions for the current REPEAT() loop.
    
- @UID@: Unique User Identifier for the current session user.
    
- @DATE@, @TIME@: Current date and time (at the moment the turn executes).
    

### 8.1 Loop-Result Indexing (TR / TU inside REPEAT)

When a turn runs inside a REPEAT() loop, its results are **accumulated**, not overwritten. Each iteration appends its output to a single pipe-delimited System Parameter. Therefore, after the loop has run k times, `@TR@TN(-1)@@` (or `@TU...@`) returns the entire list so far — e.g. `verdict1|verdict2|...|verdictk` — not just the latest value.

- **Symptom:** Feeding an un-indexed loop result into MAP, INDEX, EVAL, or SET on iteration ≥ 2 silently fails. MAP cannot match the multi-element string against a single-value `value_list`, so it returns the default; a SET stores the appended list instead of the current item; downstream scores/branches are corrupted.

- **Fix — index by the iteration number:** Use `@TRt[@R_i@]@` (e.g. `@TR@TN(-1)@[@R_i@]@`) to retrieve only the **current** iteration's result before any symbolic processing. The same applies to `@TUt[@R_i@]@` and `@TSt[@R_i@]@`.

- **Rule 8.1 (Index loop-internal results):** Any reference to `TR`/`TU`/`TS` of a turn that executes inside a REPEAT loop must be indexed with `[@R_i@]` (or the specific iteration index) when its value is consumed by another command (MAP, INDEX, EVAL, SET) or stored. Un-indexed loop results are valid only when you intentionally want the full accumulated list.
    - Check: Flag `@TR@TN(...)@@` / `@TU@TN(...)@@` used inside a loop body and fed to MAP/INDEX/EVAL/SET without a trailing `[@R_i@]` index.
    - Example (Incorrect): `@SET("V_@R_i@", "@TR@TN(-1)@@")@` — stores the growing list.
    - Example (Correct): `@SET("V_@R_i@", "@TR@TN(-1)@[@R_i@]@")@` — stores only this iteration's result.
    

## 9. Data Integrity & State Management Best Practices

Essential for stateful (memory-based) and multi-user agents.

- Rule 9.1 (Sanitize User Input): User input intended for storage (especially LOG) or use in list-based commands must be validated or sanitized to remove reserved CAFA characters (|, @) to prevent data corruption and command injection/parsing errors.
    

- Best Practice Check: Recommend adding validation/sanitation steps before saving user-provided free text.
    

- Rule 9.2 (Separation of Concerns for Data Ops): Strictly separate data operations into distinct, sequential turns following the Atomicity/Dependency rule:
    

1. LOAD / IMPORT (Turn N)
    
2. MODIFY (Operate on in-memory parameters using SET, EVAL, INDEX etc.) (Turn N+1)
    
3. SAVE / EXPORT (Turn N+2)
    

- Check: Detect violations of this Load → Modify → Save pattern across separate turns. Ensure data loaded/imported in Turn N is not used until Turn N+1.
    

- Rule 9.3 (Concurrency Golden Rule for LOG Updates): When updating data loaded from the LOG in a potentially multi-user context:
    

1. Get user input needed for the update (Turn N).
    
2. MODIFY Step (Hidden Turn N+1):
    

- Re-LOAD or IMPORT the LOG data into a temporary parameter (e.g., TEMP_LOG_DATA).
    
- Re-INDEX to find the specific user/record's current position within TEMP_LOG_DATA.
    
- SET the changes within the TEMP_LOG_DATA parameter using the calculated index.
    

3. SAVE Step (Hidden Turn N+2):
    

- SAVE or EXPORT the entire modified TEMP_LOG_DATA parameter back to the LOG, overwriting the previous state ("false" for SAVE, default for EXPORT).
    

- Check: Verify this Re-Fetch → Re-Index → Modify-in-Memory → Save-Modified pattern for LOG updates, ensuring separation of LOAD/IMPORT, modification, and SAVE/EXPORT across turns.
    

- Rule 9.4 (Initialize Stateful Parameters): Pre-define parameters that will be loaded via IMPORT (especially from "LOG") with default empty values (e.g., "org": "") in options.params.
    

- Benefit: Prevents errors on the very first run when the LOG is empty and the parameters don't exist yet.
    
- Check: Ensure parameters used in @IMPORT("LOG")@ are also defined in options.params.
    

- Rule 9.5 (LOG is Not Permanent Storage): Treat Agent Data (DIDs) and Agent Log (LOG) as transitional or semi-persistent storage. Do not rely on them for critical, long-term data archival.
    

- Best Practice: Recommend backing up or exporting critical LOG data to external storage (e.g., Google Sheets via IMPORTDATA) for long-term needs and robust analytics.
    

## 10. Conclusion

Rigorous adherence to these rules and best practices is crucial for developing functional, reliable, scalable, and maintainable CAFA agents. Consistent validation against these guidelines during the development process will minimize errors, improve debugging efficiency, and lead to more successful agent deployments.

---
# Agent Code Elements and Structure (ACES): Technical Specification and Logic

## 1. Metadata & Retrieval Keys

- Category: Agent Architecture / Core Schema
    
- Summary: ACES specifies the root JSON structure for all CAFA agents, enforcing a bifurcation between static configuration/ontology (options) and the sequential execution pipeline (prompts).
    
- RAG Keywords: JSON, schema, options, prompts, metadata, agent-structure, blueprint, workflow-engine, state-machine, initialization, global-config, turn-array, parameters, serialization, execution-context, ontology-model.
    
- Related Commands: SET, AP, SP, LLM-Turn, Symbolic-Turn, TN().
    

## 2. Architectural Logic & Rationale (The "Why")

- The Operational Friction: In standard LLM implementations, "context drift" occurs because there is no persistent memory outside the transient chat window. ACES solves this by providing a "Permanent State" (options.params) and a "Execution Thread" (prompts).
    
- Theoretical Grounding: Aligns with Assessment Engineering (AE) where the options represent the task model (ontology) and the prompts represent the evidence-gathering process (workflow).
    
- Execution Mode: System-Level Protocol Rule. The CAFA engine parses the options to instantiate the global state before the first index of the prompts array is called.
    

## 3. Formal Syntax & Parameter Schema (The "What")

### Golden Template (Root Structure)

{  
  "options": {  
    "title": "Agent Title",  
    "brief": "Summary for the library",  
    "name": "InternalID",  
    "description": "Long-form instructions",  
    "greeting": "The first user interaction",  
    "params": {}  
  },  
  "prompts": [  
    {  
      "system": "Persona/Instruction",  
      "user": "Input/Command",  
      "show": true,  
      "model": "gpt-4.1-nano"  
    }  
  ]  
}  
  
  

### Argument Table: Root Keys

|   |   |   |   |
|---|---|---|---|
|Key|Data Type|Req.|Description|
|options|Object|Yes|Global configuration, identity, and static data.|
|prompts|Array|Yes|Ordered collection of Turn Objects defining logic.|

### Argument Table: options Object Properties

|   |   |   |   |
|---|---|---|---|
|Property|Data Type|Req.|Description|
|title|String|Yes|UI display title. Supports basic HTML formatting.|
|brief|String|Yes|2-3 sentence overview for cataloging.|
|name|String|Yes|System-level identifier used for storage/logs.|
|description|String|Yes|Detailed operational guide displayed in the sidebar.|
|greeting|String|Yes|The static message displayed when the session initializes.|
|params|Object|Yes|Storage for pre-defined Agent Parameters (APs).|

### Argument Table: prompts (Turn) Object Properties

|   |   |   |   |
|---|---|---|---|
|Property|Data Type|Req.|Description|
|system|String|Yes|LLM persona or Symbolic command start (if /).|
|user|String|Yes|Task description. If "", system awaits user input.|
|show|Boolean|Yes|Visibility flag. false hides turn from the UI history.|
|model|String|Yes*|LLM selection. Required for LLM turns; omit for Symbolic.|
|temperature|String|No|Randomness control (0.1 to 1.0). Default "0.1".|
|max-tokens|String|No|Completion length cap. Default "2000".|
|output-values|String|No|Constraints LLM output format (e.g., "A|

## 4. Execution Mechanics & State Impact (The "How")

- Internal Logic Flow:
    

1. Validation: Engine checks for valid JSON keys and types.
    
2. State Hydration: Every key inside options.params is loaded into the AP memory space.
    
3. UI Sync: The greeting is rendered in the chat window.
    
4. Step-Through: The engine initializes index 0 of prompts.
    

- Common Implementation Pattern:
    

- Hidden Orchestration: Multiple symbolic turns with "show": false at the start of the prompts array to IMPORT data and SET initial logic before the first visible LLM turn.
    
- Ontology Loading: Defining thousands of items in options.params as a pipe-separated list and using INDEX or slicing ([1:5]) to present subsets to the user.
    

## 5. Reference

- Choi, J. (2025). Agent Code Elements and Structure (ACES). In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# Turn Specifications (TS): Hybrid Logic Execution Modes

## 1. Metadata & Retrieval Keys

- Category: Workflow & Execution Mode
    
- Summary: TS defines the dual-mode execution logic of CAFA agents, distinguishing between generative LLM Turns and deterministic Symbolic Turns based on prompt syntax triggers. This system ensures that agents can oscillate between high-creativity inference and high-reliability protocol execution within a single sequential workflow.
    
- RAG Keywords: LLM-Turn, Symbolic-Turn, Hybrid-Logic, Execution-Mode, Trigger, Forward-Slash, Command-Trigger, Deterministic, Generative, Turn-Logic, Case-Logic, Commenting, Bypassing, Internal-Processor, Sequence, Execution-Branching, Protocol-Override, State-Control, Automation-Bypass.
    
- Related Commands: REPEAT, JUMP, END, SET, TN(), RADIO, TEXT, EVAL, SAVE, LOAD.
    

## 2. Architectural Logic & Rationale (The "Why")

- The Operational Friction: Generative AI models are inherently stochastic and non-deterministic, making them unsuitable for structural infrastructure tasks. If an agent needs to perform a mathematical calculation, update a persistent log, or manage a complex loop, relying on an LLM's "prediction" of that logic introduces unacceptable error rates. TS solves this by providing a "Symbolic Override" mechanism.
    
- Theoretical Grounding: This architecture is inspired by Dual-Process Theory from cognitive science, which posits that human cognition consists of System 1 (intuitive, fast, associative) and System 2 (logical, slow, rule-governed). Within CAFA, the LLM Turn functions as System 1, handling nuanced natural language, while the Symbolic Turn functions as System 2, providing the "prefrontal cortex" for logic, memory, and flow control.
    
- Execution Mode: Hybrid Turn Execution. The CAFA engine acts as a pre-processor and router. Before any content is sent to an external inference endpoint, the engine scans the prompt strings to determine if the turn should be handled by the Generative Foundation AI or the Symbolic CAFA Processor. This prevents "hallucinated logic" by ensuring that rule-based tasks never touch the probabilistic model.
    
- Systemic Implications: By separating these concerns, CAFA agents achieve "Forensic Proficiency." A developer can guarantee that a scoring algorithm (Symbolic) will always execute the same way, regardless of how creative the preceding feedback (LLM) was.
    

## 3. Formal Syntax & Parameter Schema (The "What")

### Golden Template: LLM Turn (Default)

The LLM Turn is the workhorse of conversational intelligence. It requires a model and typically includes temperature and max-tokens to control the quality of the generative output.

{  
  "system": "You are a senior technical architect. Provide a high-level summary of the provided data.",  
  "user": "@InputData@",  
  "show": true,  
  "model": "gpt-4.1-nano",  
  "temperature": "0.1",  
  "max-tokens": "2000"  
}  
  

### Golden Template: Symbolic Turn (Triggered)

Symbolic turns focus on protocol actions. The model key is discarded, and the show key is frequently set to false to perform "under the hood" data processing without cluttering the user's chat history.

{  
  "system": "/ LOGIC: Calculate final grade\n@SET(\"FinalGrade\", @EVAL(\"@Score@ / @Total@ * 100\")@)@",  
  "user": "/ This turn is hidden from the user\n@JUMP(@TN(2)@)@",  
  "show": false  
}  
  

### Trigger Mechanisms Table: Deep Dive

|   |   |   |   |
|---|---|---|---|
|Mode|Trigger (Starts With)|Internal Processing Logic|Data Path|
|LLM Turn|Any alphanumeric character|Standard NLP pipeline; parameter substitution occurs before sending to model.|App → LLM API → App|
|Symbolic Turn|/ (Forward Slash)|The string is parsed as a developer comment (line 1) followed by static content or commands.|Internal Engine Only|
|Symbolic Turn|@ (Command Char)|The engine identifies the command (e.g., @REPEAT@) and routes directly to the specific functional module.|Internal Engine Only|

### Turn Specification Cases: Comprehensive Analysis

|   |   |   |   |
|---|---|---|---|
|Case|Primary Function|Trigger Syntax|State Impact|
|Case 1: Interactive LLM|Information Retrieval|user: ""|The engine creates a WAIT state, halting execution until the User input is captured and injected into the prompt.|
|Case 2: Symbolic UI Render|Data Visualization|user: "/\n# Results\nScore: @S@"|Bypasses the LLM to render markdown or system parameters instantly, ensuring 0ms latency for display.|
|Case 3: Logic Gateway|Flow Control|system: "@JUMP()@"|Immediately moves the turn pointer to the target index without generating a response or waiting for input.|
|Case 4: Hidden Processing|State Hydration|show: false|Executes commands like LOAD, IMPORT, or SET silently, preparing the environment for the next LLM turn.|

## 4. Execution Mechanics & State Impact (The "How")

### Detailed Internal Logic Flow

1. Input Pre-Scan: The CAFA engine examines the first non-whitespace character of the system prompt, then the user prompt.
    
2. Execution Branching:
    

- Branch A (Symbolic): If the character is / or @, the turn is diverted from the inference queue. The model key is ignored to save computational resources.
    
- Branch B (Generative): If no symbolic triggers are found, the engine aggregates all system instructions and user inputs.
    

3. Parameter Resolution: Regardless of the branch, the engine replaces all @ParameterName@ placeholders with their current values from the AP (Agent Parameters) or SP (System Parameters) state.
    
4. Symbolic Execution:
    

- The engine splits the string by newlines (\n).
    
- Line 1 starting with / is stripped and logged as a developer comment.
    
- Subsequent lines are evaluated for protocol commands.
    

5. Output Finalization: The resulting string (Symbolic) or model response (LLM) is stored in @TRt@ (Turn Result) and displayed to the user if "show": true.
    

### Implementation Pattern: The Commenting Rule & Documentation

The use of forward slashes (/) serves a dual purpose: it triggers the symbolic engine and allows for "Self-Documenting Agents." Because CAFA JSON does not support standard // comments, this pattern is the only way to leave notes for future developers.

- Syntax: / Comment Content\nActual Logic
    
- Rule: The comment must be the very first line. If a command precedes the /, the slash might be treated as literal text.
    

### State Transformation Example: Hybrid Workflow

// TURN 1: LLM (Analytical)  
{  
  "system": "Categorize this feedback as Positive or Negative.",  
  "user": "",  
  "show": true,  
  "model": "gpt-4.1-nano"  
}  
// RESULT: User types "I love this!", LLM responds "@TR1@ = Positive"  
  
// TURN 2: SYMBOLIC (Logical Update)  
{  
  "system": "/ If positive, add bonus point\n@SET(\"Score\", @EVAL(\"@Score@ + 1\")@)@",  
  "show": false  
}  
// EXECUTION: Bypasses LLM. AP "Score" increments. No UI output.  
  
// TURN 3: SYMBOLIC (UI Rendering)  
{  
  "user": "/\n### Thank You!\nYour current score is: @Score@.",  
  "show": true  
}  
// EXECUTION: Bypasses LLM. Instantly renders the updated score in Markdown.  
  

## 5. Architectural Implications & Best Practices

1. Atomicity: Remember that commands within a single Symbolic turn are processed together. Avoid setting a variable and trying to use it in an EVAL in the same turn; split these across two turns for reliability.
    
2. Latency Optimization: Use Symbolic turns (Case 2) to display static instructions or headers. This feels "snappier" to the user than waiting for an LLM to generate text that is already known.
    
3. Security: Always use Symbolic turns for SAVE or EXPORT operations to ensure that the LLM cannot "hallucinate" or manipulate the data being written to the platform logs.
    

## 6. Reference

- Choi, J. (2025). Turn Specifications (TS): Hybrid Logic Execution Modes. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# Agent Parameters (AP): Ontology Model and Local Variable Storage

## 1. Metadata & Retrieval Keys

- Category: State Management & Data Ontology
    
- Summary: Agent-local variables that encapsulate session-specific state, ontology models, and dynamic content. APs function as the primary mechanism for deterministic data manipulation and persistent variable storage across asynchronous, multi-turn workflows.
    
- RAG Keywords: Agent Parameters, AP, SET, local-variable, session-state, ontology-model, pipe-delimited, shuffling, LINK, data-persistence, indexing, sublist-slicing, atomicity, SET-command, parameter-access, variable-substitution, data-sanitization, condition-logic, dynamic-routing.
    
- Related Commands: SET, MAP, EVAL, INDEX, SAVE, EXPORT, LOAD, IMPORT, REPEAT, JUMP.
    

## 2. Architectural Logic & Rationale (The "Why")

- The Operational Friction: Standard Large Language Models (LLMs) operate on a stateless "context window" which is inherently probabilistic and prone to "context drift" or hallucination as conversation length increases. CAFA resolves this structural instability by introducing Agent Parameters (APs) as fixed anchor points for truth. APs act as a reliable "system memory" that preserves critical variables—such as user preferences, scoring metrics, or specific domain rubrics—preventing information degradation during turn transitions.
    
- Theoretical Grounding: This system is rooted in the Ontology Modeling framework. Rather than forcing an LLM to remember complex rules via prompting alone, CAFA structures an agent's knowledge as a symbolic database. This architecture facilitates "Deterministic Symbolic Turns," where the system performs operations (like calculating a score or selecting a specific prompt variant) based on rigid logical rules rather than generative guesses. This dual-layer approach ensures that while the interaction is natural, the underlying logic is mathematically verifiable.
    
- Execution Mode: APs are managed primarily through Symbolic Turns. These are system-level commands that bypass the LLM entirely to modify the agent's internal state machine. By executing these modifications in hidden turns ("show": false), the agent can perform complex background data preparation, ensuring that when an LLM turn is triggered, it receives a perfectly curated and up-to-date context.
    

## 3. Formal Syntax & Parameter Schema (The "What")

- Golden Template (SET Command):
    

{  
  "C": "SET",  
  "A": ["PARAMETER_NAME", "Value1|Value2|Value3", "CONDITION"]  
}  
  

Note: Within the agent's prompt strings, this logic is encapsulated as: @SET("ParamName", "Values", "Cond")@. This syntax allows for inline parameter definition during symbolic processing.

- Golden Template (AP Access):
    

- Single Item Retrieval: @AP_NAME[index]@ (Uses 1-based indexing for human-readable logic).
    
- Global Count: @AP_NAME[N]@ (Returns the total number of elements currently stored in the pipe-delimited list).
    
- Stochastic Selection: @AP_NAME[.]@ (Retrieves a single randomly selected item; ideal for varied greetings or diverse distractors).
    
- List Slicing: @AP_NAME[start:end]@ (Returns a sublist of values including both boundaries).
    

- Argument Table:
    

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|parameter_name|String|Required|The unique identifier for the variable. Must use alphanumeric characters or underscores. Case-sensitive.|
|values|String|Required|The content to store. Multiple entries are separated by a pipe (`|
|condition|String|Optional|Controls the organization of the stored array: SELF (no change), SHUFFLE (randomizes per session), SORT (alphanumeric ascending), DSORT (descending), or LINK(TargetVar) (aligns indices with another AP).|

- Return/Output Value: The command modifies the internal Agent Parameter map for the active session. In the UI, a @SET command resolves to an empty string, ensuring it does not clutter the user's view when executed in a visible turn.
    

## 4. Execution Mechanics & State Impact (The "How")

- Internal Logic Flow: 1. Identification: The CAFA engine scans the turn content for the SET command signature.  
    2. Lexical Parsing: The engine extracts the three arguments, handling nested parameter substitutions (e.g., @SET("A", "@B@")@) before final assignment.  
    3. Array Transformation: The values string is split into an internal list. If a condition like SHUFFLE is provided, the engine applies the transformation immediately, persisting this specific order for the remainder of the session.  
    4. State Persistence: The resulting list is stored in the session's memory. If a parameter with the same name already exists, it is overwritten, enabling dynamic state updates (e.g., incrementing a counter).
    
- Atomicity/Dependency Rule: A critical constraint of the CAFA Protocol is that parameters are updated atomically at the end of a turn's execution cycle. Consequently, a variable updated via SET in Turn N is unreliable if accessed within the same Turn N. Developers must follow the "Set-then-Use" pattern: define or update data in one turn, and reference that updated data in the subsequent turn (Turn N+1) to guarantee state integrity.
    
- Common Implementation Patterns: * The Hidden Orchestrator: Turn 1 is frequently a hidden symbolic turn ("show": false) used to initialize the entire session's ontology. For example, setting a @LEVEL@ variable that dictates the complexity of all subsequent LLM prompts.
    

- The Parallel Ontology (LINK): When dealing with paired data (e.g., a list of Spanish words and their English translations), developers use SHUFFLE on the first list and LINK on the second. This ensures that even when the words are randomized for a quiz, the correct translation always moves with its corresponding word.
    
- Generative-to-Symbolic Handover: An LLM generates a pipe-separated list (e.g., "Feature A|Feature B") which is then captured via SET in a following symbolic turn. This allows unstructured generative output to be "promoted" into structured symbolic data for use in logic gates or evaluation commands.
    

## 5. Reference

- Choi, J. (2025). Agent Parameters (AP): Ontology Model and Local Variable Storage. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# System Parameters (SP): Runtime Context Variables

## 1. Metadata & Retrieval Keys

- Category: State Management / Runtime Context
    
- Summary: Reserved read-only variables providing high-fidelity access to the agent's execution history, loop status, and environmental metadata.
    
- RAG Keywords: SP, System Parameter, Runtime Context, Execution State, Turn Reference, Metadata, Global Scope, Read-only, TR, TU, TS, History, Repeat State, UID, Temporal Data, State Machine, IMPACT, GAMER, State Persistence, Contextual Memory, Session Metadata, Evidence-Centered Design, Between-Turn Collective AI, Micro-Agent Coordination, Temporal Grounding, Data Lineage.
    
- Related Commands: SET, REPEAT, JUMP, EVAL, INDEX, MAP, SAVE, LOAD, IMPORT, EXPORT, GS, GSTABLE.
    

## 2. Architectural Logic & Rationale (The "Why")

- The Operational Friction: Generative AI models are inherently stateless and "ephemeral" in their raw form. Each turn is processed as an isolated event. Without a structured system parameter layer, an agent loses its temporal continuity with every new user interaction. While standard LLM APIs often use "chat history" as a long string, this approach is imprecise, token-heavy, and prone to "context drift"—where the AI loses track of specific early constraints, system prompts, or user inputs. SP provides a deterministic, surgically precise method for an agent to "look back" at specific historical snapshots without needing to re-process the entire narrative thread, ensuring consistency across complex, high-stakes workflows.
    
- Between-Turn Collective AI Logic: In the CAFA ecosystem, we do not view an agent as a monolithic intelligence. Instead, it is conceptualized as a Collective of Micro-Agents, where each "Turn" represents a distinct specialized cognitive state or persona. SP acts as the cognitive bridge for Between-Turn Collective AI. This enables a "Refiner Agent" in Turn 3 to have perfect, unmediated recall of the "Goal-Setting Agent" in Turn 1 and the "Drafting Agent" in Turn 2. By persisting the triad of intent (TS), interaction (TU), and output (TR), SP facilitates a form of temporal collaboration. The current turn isn't just "continuing" a chat; it is actively collaborating with its own past versions, using previous outputs as foundational evidence to reach a higher state of collective accuracy. This "Collective Intelligence" across turn-boundaries allows for self-correction, iterative refinement, and recursive logic.
    
- Execution Mode: System Level Variable. These variables are immutable at the user level and cannot be modified via the SET command. They are automatically instantiated, managed, and incremented by the CAFA engine's state machine at the boundary of every turn transition. They reside in the "Volatile Session Memory," ensuring that while they persist throughout a single session, they remain isolated to that specific user session to prevent data leakage.
    

## 3. Formal Syntax & Parameter Schema (The "What")

- Comprehensive Parameter Table:
    

|   |   |   |   |
|---|---|---|---|
|SP Name|Data Type|Scope|Technical Description & Implementation Use-Case|
|@TUt@|String|Global|User Prompt History: The raw input submitted by the user at turn t. Essential for checking user compliance or extracting specific requirements mentioned early in a session.|
|@TRt@|String|Global|Turn Result: The payload generated at turn t. For LLM turns, this is the text response. For Symbolic turns, it is the result of the logic (e.g., the value of a calculation or a specific list item).|
|@TSt@|String|Global|System Prompt History: The instruction set used at turn t. This is critical for "Meta-Analysis" turns where the agent must evaluate if it followed its own instructions correctly.|
|@T_i@|Integer|Session|Turn Index: The current 1-based turn number. Useful for conditional logic like: @IF("@T_i@ > 5", "TargetTurn", "NextTurn")@.|
|@R_i@|Integer|Loop|Iteration Index: The current cycle number within a REPEAT block. Often used as an index for linked Agent Parameters (e.g., @Questions[@R_i@]@).|
|@R_s@|Integer|Loop|Loop Start: The turn number where the current REPEAT block began. Used to calculate jump-back points for complex nested loops.|
|@R_e@|Integer|Loop|Loop End: The turn number where the current REPEAT block is scheduled to terminate.|
|@R_n@|Integer|Loop|Total Repetitions: The static integer representing the total count of intended loop iterations.|
|@UID@|String|Session|User Identity: A unique hash representing the session user. Crucial for partitioning data in the LOG during SAVE or EXPORT operations.|
|@DATE@|String|System|Temporal Metadata: Current date (YYYY-MM-DD). Used for timestamping log entries or generating dated reports.|
|@TIME@|String|System|Temporal Metadata: Current time (HH:MM:SS). Used for performance auditing and session duration tracking.|

- Example CAFA Agent Code: Using System Parameters to Chain Turns  
    This agent demonstrates the utility of System Parameters by creating a workflow where the output of one turn becomes the input for the next.
    

{  
    "options": {  
        "title": "System Parameter Chaining",  
        "brief": "An agent that demonstrates how to use TSt, TRt, and TUt to link turns together.",  
        "name": "System Parameter TR TU TS Example",  
        "description": "This agent takes a number, adds one to it, then shows how to re-use the previous turn's system prompt, result, and original user input in subsequent turns.",  
        "greeting": "Please provide a number.",  
        "params": {}  
    },  
    "prompts": [  
        {  
            "system": "Add one to the provided number.",  
            "user": "",  
            "temperature": "0.1",  
            "max-tokens": "2000",  
            "model": "gpt-4.1-nano"  
        },  
        {  
            "system": "@TS1@",  
            "user": "@TR1@",  
            "temperature": "0.1",  
            "max-tokens": "2000",  
            "model": "gpt-4.1-nano"  
        },  
        {  
            "system": "@TS1@",  
            "user": "@TU1@",  
            "temperature": "0.1",  
            "max-tokens": "2000",  
            "model": "gpt-4.1-nano"  
        }  
    ]  
}  
  

### Code Explanation: Chaining Logic Breakdown

This agent demonstrates three distinct methods of re-using state across turns, showcasing the Between-Turn Collective AI in action:

1. Turn 1: Base Execution: The agent receives a number from the user. The prompt Add one to the provided number. is stored in @TS1@, the user input is in @TU1@, and the LLM's answer (e.g., "5") is stored in @TR1@.
    
2. Turn 2: Logic Propagation (@TS1@ + @TR1@): * Context Reuse: By setting the system prompt to @TS1@, the agent inherits the instructions from the first turn without re-typing them, ensuring instructional consistency.
    

- Chain of Thought: By setting the user prompt to @TR1@, the output of Turn 1 becomes the input for Turn 2. The LLM sees the previous answer and applies the same instruction again (e.g., adding 1 to 5 to get 6). This is the simplest form of generative chaining.
    

3. Turn 3: Original Input Retrieval (@TS1@ + @TU1@):
    

- Contextual Anchoring: While Turn 2 built upon the result of Turn 1, Turn 3 goes back to the source. By referencing @TU1@, the agent ignores the intermediate calculation in @TR1@ and performs a fresh operation on the original user input, demonstrating the ability to retrieve unpolluted "source of truth" data.
    

- Return/Output Value: SPs are resolved via Pre-execution String Interpolation. Before a turn is processed, the engine performs a regex scan. If it finds @TR1@, it retrieves the value "5" from memory and replaces the placeholder. This means that the LLM or the Symbolic processor never sees the @ syntax; it only sees the actual data.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow & Lifecycle

The life cycle of a System Parameter follows a strict "Post-Write, Pre-Read" sequence:

1. Turn Execution: Turn t executes and generates an output (TR) and consumes a system instruction (TS) and user input (TU).
    
2. State Commit: At the conclusion of the turn, the CAFA engine commits these three strings to the SP stack associated with the session ID. This commit is atomic.
    
3. Regex Interception: When Turn t+1 (or any future turn) begins, the engine intercepts the prompt strings defined in the JSON.
    
4. Hydration (Substitution): The engine "hydrates" the prompt by injecting values from the SP stack. This occurs before any model parameters (temperature, model name) are evaluated.
    
5. Null Handling: If an agent references a future or non-existent turn (e.g., @TR99@ in turn 5), the engine resolves this to an empty string "" to prevent execution crashes.
    

### 4.2 Sophisticated Implementation Patterns

- The IMPACT Framework (Iterative Multi-turn Process): This utilizes SP to create a "Reasoning Chain."
    

- Phase 1 (Collection): User input is stored in @TU1@.
    
- Phase 2 (Drafting): LLM generates content based on @TU1@, outputting @TR2@.
    
- Phase 3 (Critique): A separate persona evaluates @TR2@ against @TU1@, resulting in @TR3@.
    
- Phase 4 (Finalization): Turn 4 reads @TR2@ and @TR3@ to produce a high-fidelity final artifact.
    

- The GAMER Framework (Evolutionary Reflection): Focuses on the "Reflection" turn. Turn 2 might be a hidden symbolic turn that performs an EVAL or INDEX check on @TR1@ to determine if the next turn should be a revision or an advancement. It uses SP to ensure the "Evolution" is grounded in "Evidence."
    
- Diagnostic Looping with @R_i@: In a math quiz agent, @R_i@ is used to pull specific problems from a parameter PROBLEMS. The agent then compares the user input in @TUt@ with the correct answer via an EVAL command, using @R_i@ to keep the scoring logic synchronized with the current question.
    

### 4.3 Security, Scope, and State Integrity

- Atomic Isolation: System Parameters are scoped strictly to the Session Level. This prevents "data bleeding," ensuring that User A's execution history is never accessible to User B's session.
    
- Immutability (Read-Only): Unlike Agent Parameters (AP), SPs cannot be overwritten by the developer using SET. They are "Read-Only History." This ensures the integrity of the evidence trail for auditing and debugging.
    
- Symbolic Sanitization: When SP data is passed into symbolic commands (like SET or EVAL), the CAFA engine automatically escapes reserved characters (e.g., pipes | or at-signs @) if they are present in the text, preventing "Prompt Injection" or logic breakage from user-supplied content.
    

## 5. Reference

- Choi, J. (2025). System Parameters (SP): Runtime Context Variables. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# JSON Parameter (JP): Structured Data Engineering

## 1. Metadata & Retrieval Keys

- Category: State Management / Logic & Flow Control
    
- Summary: A high-density data system enabling the storage, manipulation, and retrieval of hierarchical JSON objects and arrays within CAFA agents, bridging the gap between generative output and deterministic symbolic logic.
    
- RAG Keywords: JP, JSON Parameter, SETJ, P2JSON, JSONVALS, Structured Data, Hierarchical Ontology, Nested Objects, Array Indexing, 1-based Index, 0-based Index, Data Transformation, LLM Context, QTI Item, Multi-layered knowledge, Parallel List Conversion, Data Serialization, Persistence, Semantic Richness, JSON Pathing, State Integrity, Cognitive Load Reduction, Complex Adaptive Systems, Ontology Mapping, Epistemological Integrity.
    
- Related Commands: SET, AP, SP, INDEX, MAP, RADIO, TEXT, EVAL, SAVE, LOAD, IMPORT, EXPORT, TN().
    

## 2. Architectural Logic & Rationale (The "Why")

- The Operational Friction: Standard Agent Parameters (AP) operate on a flat, tabular model using parallel pipe-separated lists. While highly efficient for simple 1-to-1 associations (e.g., matching a "Question" with an "Answer"), this model encounters "Pointer Fatigue" when data is intrinsically nested or multi-dimensional. For example, a "Medical Diagnosis" object might contain nested arrays for "Symptoms," "Treatment Options," and "Risk Factors." Attempting to model this in flat lists leads to "Ontology Bloat"—where dozens of parallel lists must be manually synchronized—increasing the probability of index mismatch errors. JP solves this by allowing a single variable to encapsulate an entire multi-dimensional knowledge cluster.
    
- Between-Turn Collective AI Logic: JP serves as the "Structured Memory" for Between-Turn Collective AI. In multi-turn workflows like IMPACT or GAMER, an agent often generates a complex artifact in Turn 1 (e.g., a rubric) and refines specific attributes of it in Turn 3. By storing the artifact as a JP, the agent maintains Epistemological Integrity throughout the session. An LLM receiving a JSON object understands the semantic relationships between keys automatically (e.g., that a "rationale" belongs to a specific "distractor"). In contrast, receiving ten separate parameters requires the LLM to expend "probabilistic reasoning" just to re-associate the data, leading to higher latency and potential halluncination.
    
- Execution Mode: Symbolic Turn / System Level Command. Unlike generative LLM output which is probabilistic, JP manipulation via SETJ and JSONVALS is deterministic. This creates a "Hybrid Architecture" where the "Creative" (LLM) generates the raw JSON structure, but the "Architect" (Symbolic logic) parses, validates, and presents it through deterministic UI controls.
    

## 3. Formal Syntax & Parameter Schema (The "What")

### 3.1 The Dual-Indexing Mandate (CRITICAL)

This is the most frequent point of logic failure in CAFA development. The engine bridges the pedagogical world (1-based) and the engineering world (0-based).

- Top-Level Array Indexing (1-based): If a JSON Parameter is the "Root" container and is an array (e.g., [{}, {}]), you access the first object using index [1]. This ensures JP is a drop-in replacement for standard AP parallel lists.
    
- Nested (Lower-Level) Array Indexing (0-based): Once you navigate "inside" a JSON object or access an array property (e.g., {"key": []}), the system reverts to standard JavaScript/JSON 0-based indexing.
    
- Implication: Failure to observe this "1-to-0 handover" results in undefined errors. For instance, accessing the first feature of the second product would correctly be @Products[2].features[0]@.
    

### 3.2 Command Reference & Quoting Exceptions

|   |   |   |   |
|---|---|---|---|
|Command|Syntax|Quoting Rule|Description|
|SETJ|@SETJ(name, JSON_STRING)@|NO OUTER QUOTES|MANDATORY EXCEPTION: Do not quote the name or the JSON payload. This prevents quote-nesting collisions.|
|P2JSON|@P2JSON("P1\|P2\|P3")@|QUOTES REQUIRED|Merges parallel AP lists into a single structured JSON array string.|
|JSONVALS|@JSONVALS(JP, "key"[, "pattern"])@|MIXED|The JP name is unquoted; the key and optional pattern must be double-quoted.|

### 3.3 Example CAFA Agent Code: Dynamic QTI Item Generation

This agent demonstrates the complete JP lifecycle: Collection -> Generation -> Transformation -> Presentation -> Logic Check.

{  
    "options": {  
        "title": "Dynamic QTI Item Generator",  
        "brief": "Generates a quiz item, transforms it to JSON, and displays it as a poll.",  
        "name": "QTI Generator with JSON",  
        "description": "Uses LLM structured output to generate JSON, then uses JSONVALS to present choices in a RADIO control.",  
        "greeting": "Let's create a quiz question!",  
        "params": {  
            "JSONFORMAT": {  
                "org": "[{\"stem\":\"string\",\"choices\":[{\"identifier\":\"A\",\"text\":\"<string>\"},{\"identifier\":\"B\",\"text\":\"<string>\"},{\"identifier\":\"C\",\"text\":\"<string>\"},{\"identifier\":\"D\",\"text\":\"<string>\"}],\"correctAnswer\":\"string\"}]"  
            }  
        }  
    },  
    "prompts": [  
        {  
            "user": "/ T1: Collect Topic.\n@TEXT(\"user_topic\", \"What topic should I create a multiple-choice question about?\")@",  
            "show": true  
        },  
        {  
            "system": "You are a quiz designer. Output *only* valid JSON matching @JSONFORMAT@. Ensure no markdown formatting (like ```json) is in the output.",  
            "user": "Topic: @TEXT(user_topic)@",  
            "show": false,  
            "model": "gpt-4.1-nano",  
            "output-values": "@JSONFORMAT@"  
        },  
        {  
            "user": "/ T3: Store result using SETJ exception rule. Arguments are NOT quoted.\n@SETJ(JSON_ITEM, @TR@TN(-1)@@)@",  
            "show": false  
        },  
        {  
            "user": "/ T4: Isolate nested array for JSONVALS. Navigation follows 1-based top level and dot notation.\n@SETJ(CHOICES, @JSON_ITEM[1].choices@)@",  
            "show": false  
        },  
        {  
            "user": "/ T5: Presentation via JSONVALS. Flattening 'text' key into a pipe-separated string for RADIO.\n@RADIO(\"user_answer\", \"@JSON_ITEM[1].stem@\", \"@JSONVALS(CHOICES, \"text\")@\")@",  
            "show": true  
        },  
        {  
            "user": "/ T6: Feedback loop using JP properties. Selection is compared to the 'correctAnswer' key.\nSelection: @RADIO(user_answer)@ | Correct Answer: @JSON_ITEM[1].correctAnswer@.\n\nLogic Validation: @EVAL(\"'@RADIO(user_answer)@' == '@JSON_ITEM[1].correctAnswer@' ? 'Correct!' : 'Incorrect.'\")@",  
            "show": true,  
            "markdown": true  
        }  
    ]  
}  
  

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Serialization & Transformation (P2JSON)

The P2JSON command is the "ETL" (Extract, Transform, Load) bridge.

1. Parallel Extraction: The engine identifies the parameters (e.g., Stem|Answer).
    
2. Synchronous Iteration: It loops through the pipe-separated values of all specified parameters simultaneously.
    
3. Structured Boxing: It wraps values at index i into an object where keys are the parameter names.
    
4. Serialization: The resulting array is stringified for storage in a TR or assignment via SETJ.
    

### 4.2 Querying & Bridging (JSONVALS)

JSONVALS acts as the "Column Selector" or "Map function." It is the critical bridge back to the AP format required by UI controls.

- Scan Phase: It iterates through every object in the specified JSON array.
    
- Extraction Phase: It pulls the value associated with the provided "key".
    
- Filtering (Optional): If a "pattern" is provided, the engine performs a regex match; only hits are included.
    
- Flattening: All extracted values are joined using the pipe (|) character, making the result immediately valid for commands like @RADIO()@ or @MAP()@.
    

### 4.3 State Integrity & Atomic Persistence

- Atomic Overwrites: JP does not support granular "property-level" updates via standard SET. You cannot modify @JP[1].key@ directly. You must replace the entire object using SETJ. This ensures that the object schema remains valid and prevents "Schema Drift."
    
- Regex Hydration: During turn pre-processing, the CAFA engine scans for JP placeholders. It resolves the JSON pathing before the prompt is sent to the LLM. If a path is invalid (e.g., @JP[1].wrongKey@), it resolves to an empty string "" to prevent execution crashes.
    
- Complexity Guardrails: While the engine supports deep nesting, developers should avoid exceeding 4-5 levels of depth to optimize pre-processing speed and prevent regex stack overflows in large agents.
    

## 5. Ontology Mapping Patterns

- The "Bridge" Pattern: Use standard AP for user-facing data entry (human-readable) and then convert to JP using P2JSON for "Thematic Analysis" or "Generative Refinement" phases where the AI needs to see the structural whole.
    
- The "Snapshot" Pattern: Use SETJ to capture the structured result of an LLM turn (@TR@TN(-1)@@). This prevents subsequent turns from being polluted by LLM "conversational filler" (e.g., "Here is the JSON you asked for...").
    
- The "Isolation" Pattern: For complex items (like QTI questions), use SETJ to pull a nested array (like "choices") into its own top-level parameter. This simplifies the logic of presentation commands like JSONVALS.
    

## 6. Reference

- Choi, J. (2025). JSON Parameter (JP): Structured Data Engineering. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---

# SET Command: Define and Update Agent Parameters

## 1. Metadata & Retrieval Keys

- Category: State Management / Logic & Flow Control
    
- Summary: The primary symbolic directive for instantiating, assigning, and mutating Agent Parameters (APs) during runtime. It serves as the bridge between transient generative output and persistent, deterministic agent memory.
    
- RAG Keywords: SET, VariableAssignment, DataManipulation, StateManagement, APUpdate, Logic, ParameterMutation, GlobalScope, Persistence, RuntimeInitialization, StatePersistence, SymbolicTurn, Atomicity, ValueOverride, DataBinding, InteractionEvidence, MemoryAllocation, CAFAState, DeterministicMemory, VariableScoping, OntologyMemory, RuntimeMutation, StateMachineSync, EpistemologicalIntegrity, Micro-AgentSynchronization, ReasoningPropagation.
    
- Related Commands: EVAL, MAP, INDEX, LOAD, SAVE, IMPORT, EXPORT, TN().
    

## 2. Architectural Logic & Rationale (The "Why")

- The Operational Friction: Resolving the Stateless Void: Foundation AI models are inherently stateless; they lack a persistent internal memory that can be programmatically addressed and modified outside of the context window. While System Parameters (SP) offer a read-only history, they cannot store "derived truths," synthetic ontologies, or evolving user scores. The SET command resolves this "Persistence Gap" by providing a writable symbolic memory layer. It allows the agent to capture probabilistic LLM outputs, user-provided strings, or deterministic mathematical results and transform them into stable Agent Parameters (APs) that reside in the agent's global state. This prevents "Reasoning Fragmentation" where an agent loses the thread of its own logic across complex, multi-turn interactions.
    
- Between-Turn Collective AI Logic: The State Synchronizer: In the CAFA ecosystem, SET acts as the "State Synchronizer" between discrete Micro-Agents (Turns). It allows an "Evaluator Micro-Agent" in Turn 1 to store a diagnostic score into an AP, which a "Navigator Micro-Agent" in Turn 5 can then use to branch the workflow. This transforms the agent from a linear conversation into a complex adaptive system. It is the fundamental mechanism that converts transient interaction into a persistent, multi-layered ontology model, enabling "Memory" to exist across the execution timeline. It ensures that the "Truth" established in early turns is preserved as an immutable constraint for later generative phases.
    
- Execution Mode: Symbolic Turn Sovereignty: While SET can be embedded in an LLM turn's prompt for immediate post-processing, it is architecturally prioritized for dedicated, hidden symbolic turns ("show": false). This ensures that state changes are fully committed and synchronized before the next generative cycle begins, preventing "State Hallucinations" where an LLM might misinterpret its own past output before it is codified as a formal parameter.
    

## 3. Formal Syntax & Parameter Schema (The "What")

- Golden Template: Initializing and Mutating State  
    This example demonstrates a hidden turn using relative turn numbering (TN) to capture and codify data from a previous generative turn.
    

{  
  "system": "/ Symbolic Turn: Initialize user state and capture LLM sentiment from previous turn.",  
  "user": "@SET(\"UserScore\", \"0\")@\n@SET(\"UserSentiment\", \"@TR@TN(-1)@@\", \"SELF\")@",  
  "show": false  
}  
  

- Argument Table:
    

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|parameter_name|String|Required|The unique identifier for the AP. Must be enclosed in double quotes.|
|value|String|Required|The data string to store. Can be a literal, a pipe-separated list (`"A|
|cond|String|Optional|Controls ordering/linking: SELF (Default), SHUFFLE (Randomize), SORT (Ascending), DSORT (Descending), or LINK(Target).|

- Return/Output Value: The SET command is a "silent" directive; it returns no visible text to the UI. Instead, it modifies the agent's internal parameter stack (params). The updated data is accessed in subsequent turns using the standard @ParameterName@ syntax.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 The Atomicity & Dependency Rule (CRITICAL)

CAFA parameters follow a strict Turn-Boundary Lifecycle. Commands within a single prompt string are processed atomically and simultaneously.

- The Friction (Race Conditions): If Turn 5 executes @SET("Score", "10")@, referencing @Score@ elsewhere in that same Turn 5 prompt will yield the old value (or an empty string if it didn't exist). The engine does not support sequential "Read-After-Write" within the same turn cycle.
    
- The Mandate (The Next-Turn Rule): An updated AP value is only reliably available for retrieval (in EVAL, MAP, or display) starting from Turn 6 (or Turn N+1). Developers must strictly separate "State Assignment" logic and "State Retrieval" logic into sequential turns to ensure data integrity and prevent logical race conditions.
    

### 4.2 Sophisticated Dynamic Assignment Patterns

- The LLM-to-Ontology Bridge: Capturing generative insight for downstream symbolic use.
    

- Syntax: @SET("Categorization", "@TR@TN(-1)@@")@
    
- Impact: This "freezes" the model's probabilistic output into a deterministic variable that can be used for MAP or INDEX routing.
    

- Recursive Counter Logic: Tracking progress through a REPEAT block.
    

- Syntax: @SET("StepCount", "@EVAL(\"@StepCount@ + 1\")@")@
    
- Impact: Allows the agent to maintain a persistent tally of iterations that survives the loop's termination.
    

- Dynamic List Accumulation: Building a session log or a list of user errors.
    

- Syntax: @SET("ErrorLog", "@ErrorLog@|@NewError@")@
    
- Impact: Dynamically grows a pipe-separated list. Note: Ensure @ErrorLog@ is pre-defined as "" in options.params to avoid the leading pipe on the first entry.
    

### 4.3 State Integrity & Data Sanitization

- Character Collision: When using SET to store user-generated content (retrieved from @TUt@), developers must account for "Reserved Character Collision." If a user inputs a pipe (|) or an at-sign (@), it can inadvertently break list parsing or command execution in subsequent turns.
    
- Ontology Protection: For mission-critical storage, utilize a symbolic turn to wrap or sanitize input. If the AP is intended for INDEX or MAP, ensure the value argument is properly cleaned of reserved delimiters to maintain the structural integrity of the AP list.
    
- Memory Persistence: Parameters defined or updated via SET persist for the duration of the session. Unlike SP (which is session-volatile), AP values can be explicitly saved to the platform's long-term storage using the SAVE or EXPORT commands, effectively "crystallizing" the runtime state into a permanent record.
    

## 5. Reference

- Choi, J. (2025). SET Command: Define and Update Agent Parameters. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    


---
# TN Command: Relative Turn Numbering

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / State Machine Orchestration
    
- Summary: A dynamic resolution command that calculates absolute turn indices based on a relative integer offset from the current turn pointer. It serves as the primary mechanism for maintaining structural integrity in complex, non-linear workflows.
    
- RAG Keywords: TN, TurnNumbering, RelativeOffset, DynamicRouting, StructuralRobustness, AgileModeling, ExecutionPointer, WorkflowAutomation, TN(-1), ContextualReference, LogicPortability, MaintenanceEfficiency, Between-TurnCollaboration, StateMachine, PointerResolution, Decoupling, StatePersistence, LogicScalability, EncapsulatedLogic.
    
- Related Commands: JUMP, REPEAT, TR, TU, TS, SET, EVAL, MAP.
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Eliminating Structural Fragility and Technical Debt

In early or naive agent modeling, developers often rely on hardcoded absolute turn numbers (e.g., @JUMP("5")@ or @TR4@). While functional in small prototypes, this approach creates significant "Structural Fragility" as the agent scales. If a developer inserts a new diagnostic turn or a "Reflection" prompt at index 3, every subsequent jump and historical reference in a 50-turn agent would break. This necessitates a manual, error-prone audit of the entire JSON structure. The TN command solves this by decoupling the logical relationship from the physical array index. By using relative offsets (e.g., "return to the previous instruction block"), the logic remains valid regardless of how many turns are inserted, deleted, or reordered around it.

### 2.2 Theoretical Grounding: Location-Invariant Logic

TN implements the principle of Location-Invariance. In the CAFA Protocol, a logical module (like a feedback loop or a scoring sequence) should be portable. If a developer copies a 5-turn logic block from one agent to another, the internal references should not need re-indexing. TN treats the agent workflow as a set of relative cognitive relationships rather than a fixed grid. This aligns with Agile Modeling practices where agents are iteratively refined and expanded. It allows for the "Dynamic Expansion" of the context window without corrupting the state machine's execution path.

### 2.3 Between-Turn Collective AI Logic

The TN command acts as the "Cognitive Bridge" between distinct Micro-Agents (Turns). It allows a "Critic Micro-Agent" to say, "I need the data from the turn immediately preceding me," without requiring the architect to hardcode that turn's identity. This abstraction is critical for creating Modular Ontology Models. By using relative pointers, Micro-Agents can be swapped or updated independently, provided their relative positioning remains consistent with the intended logic flow.

## 3. Formal Syntax & Parameter Schema (The "What")

- Golden Template: Dynamic Context Retrieval  
    This example demonstrates how TN is nested within system parameters to pull data from the most recent historical turn, creating a seamless refinement loop.
    

{  
  "system": "Analyze the evidence provided in the instruction set from Turn @TN(\"-2\")@ and the resulting output from Turn @TN(\"-1\")@.",  
  "user": "Summarize the final result based on: @TR@TN(\"-1\")@@",  
  "show": true  
}  
  

- Argument Table:
    

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Technical Description|
|offset|String|Required|A signed integer representing the relative distance from the current turn. Negative values (e.g., "-1") look backward at history; positive values (e.g., "2") look forward for navigation. Must be enclosed in double quotes.|

- Return/Output Value: The command resolves to a raw Integer representing the absolute index of the target turn. This integer is consumed by parent commands (like @TRt@, @TUt@, or @JUMP()@) during the final hydration phase.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 The Pre-processing Resolution Lifecycle

The TN command is the highest-priority directive in the Prompt Hydration Phase. It must be resolved before any other command to ensure the engine has a valid pointer for data retrieval.

1. Regex Detection: The engine performs a high-priority scan of the current turn's prompt for the @TN(...)@ pattern.
    
2. Execution Pointer Retrieval: The engine identifies the current turn's absolute index (T_i) within the prompts array.
    
3. Integer Arithmetic: The engine applies the offset: TargetIndex = T_i + offset.
    
4. Recursive Substitution: The engine replaces the TN command string with the calculated TargetIndex integer.
    

- Example: If the agent is at Turn 10, @TR@TN("-2")@@ is first transformed into @TR8@.
    

5. Final Hydration: Only after TN is resolved does the engine attempt to fetch the data for @TR8@ from the SP (System Parameter) stack.
    

### 4.2 Handling Out-of-Bounds and Errors

If a relative offset results in a TargetIndex that is less than 1 or greater than the total length of the prompts array, the engine follows the Null Pointer Protocol:

- Historical References: If @TN("-10")@ points to index -4, it resolves to index 1 (the greeting/start).
    
- Navigational References: If a JUMP points beyond the array, the session is terminated via an implicit END command to prevent execution loops.
    

### 4.3 Implications for Control Flow and Loops

The use of TN is mandatory for building complex, reusable logic blocks:

- Dynamic Loop Bounds: In a REPEAT block, using @REPEAT("@TN("1")@", "@T_i@", "3")@ ensures the loop always encapsulates the turns immediately following the command. This allows developers to move the entire loop "unit" anywhere in the agent without breaking the iteration.
    
- Conditional Branching (Skip Logic): When paired with MAP or EVAL, TN facilitates "Agile Branching." For example, @JUMP("@MAP("@Score@", "Pass|Fail", "@TN("2")@|@TN("1")@", "@TN("3")@")@")@ creates a dynamic routing system that is entirely self-contained and index-independent.
    

## 5. Structural Best Practices

- Negative Offsets (Temporal History): Primarily used for TR, TU, and TS retrieval (e.g., @TN("-1")@). This is the standard for IMPACT and RISE frameworks where the current turn evaluates the immediate predecessor.
    
- Positive Offsets (Navigational Steering): Primarily used for JUMP and REPEAT to bypass instructions or define the boundaries of a logical sub-routine.
    
- The "One-Level" Rule: While TN can be nested, developers should prioritize readability. Nesting TN more than 2 levels deep (e.g., a TN inside an EVAL inside a SET) increases "Cognitive Load" for the human modeler and should be avoided in favor of clear, sequential turn logic.
    
- Avoid Zero Offsets: @TN("0")@ refers to the current turn. While technically valid, referencing the result of the current turn (@TR@TN("0")@@) will always return an empty string because the result has not yet been generated.
    

## 6. Reference

- Choi, J. (2025). TN Command: Relative Turn Numbering. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# SETJ Command: Define and Update JSON Parameters

## 1. Metadata & Retrieval Keys

- Category: State Management / Complex Data Handling / Knowledge Engineering
    
- Summary: A specialized symbolic command designed to instantiate or update JSON Parameters (JP) with structured, multi-dimensional data, utilizing a unique syntax that bypasses standard CAFA quoting rules to preserve nested schema integrity.
    
- RAG Keywords: SETJ, JSON, JP, DataManipulation, ComplexData, ObjectCreation, JPSyntax, StateManagement, HierarchicalData, NestedObject, ArrayStorage, StructuredMemory, NoQuotes, ParameterMutation, DataSerialization, OntologyModeling, JSONPath, BridgeLogic, SchemaMapping, EpistemologicalIntegrity, DataSovereignty, SemanticAnchoring, Micro-AgentCoordination.
    
- Related Commands: SET, P2JSON, JSONVALS, INDEX, MAP, EVAL, TN().
    

## 2. Architectural Logic & Rationale (The "Why")

- The Operational Friction: Resolving the "Quote Nesting" Conflict: In standard CAFA logic, the SET command requires all arguments to be enclosed in double quotes. However, valid JSON strings inherently use double quotes for keys and string values. Using SET to store JSON would require excessive, recursive, and error-prone character escaping (e.g., \"). This "Syntax Collision" creates significant technical debt and increases the risk of parsing failures. SETJ solves this by creating a dedicated argument space where outer quotes are strictly forbidden. This allows the CAFA engine to treat the second argument as a raw literal, facilitating the direct insertion of complex JSON objects and arrays without disrupting the parent JSON structure of the agent code.
    
- Between-Turn Collective AI Logic: Structured Schema Memory: Within the CAFA "Collective AI" framework, an agent is a sequence of Micro-Agents (Turns). SETJ serves as the cognitive bridge that allows these turns to share "Knowledge Objects" rather than just raw strings. While SET handles flat tabular data (AP), SETJ enables a "Specialist Micro-Agent" to output a complex, valid schema (such as a QTI assessment item, a medical diagnostic report, or an organizational hierarchy) and "crystallize" it as a single, coherent entity. This ensures that the Epistemological Integrity of the data is preserved as it propagates through the state machine, reducing the cognitive load on downstream LLMs by providing them with a pre-structured, semantic context.
    
- Execution Mode: Symbolic Turn / System Level Command: This command is deterministic and non-generative. It must reside in hidden turns ("show": false) to serve as a pre-processor for the agent's complex knowledge base. By separating data structuring (Symbolic) from data generation (LLM), CAFA achieves a "Hybrid Logic" where the structure is guaranteed even if the content is probabilistic.
    

## 3. Formal Syntax & Parameter Schema (The "What")

- Golden Template: The Quote-Free Exception  
    Unlike virtually every other CAFA command, SETJ arguments MUST NOT be enclosed in their own pair of double quotes. This is a mandatory exception to Rule 6.1.1.
    

Template A: Object Root

{  
  "user": "/ Create a structured product record dynamically.\n@SETJ(productInfo, {\"name\":\"Smart Watch\",\"features\":[\"GPS\",\"Heart Rate\"],\"price\":299.99})@",  
  "show": false  
}  
  

Template B: Array Root (Common for Parallel Item Banks)

{  
  "user": "/ Initialize an array of items.\n@SETJ(Inventory, [{\"id\":\"01\",\"qty\":\"5\"},{\"id\":\"02\",\"qty\":\"12\"}])@",  
  "show": false  
}  
  

- Argument Table:
    

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Technical Description|
|parameter_name|String|Required|The unique identifier for the JP. DO NOT QUOTE.|
|json_string|JSON String|Required|A valid JSON object or array literal. DO NOT QUOTE. Internal JSON quotes must be escaped as \" within the agent's turn string to remain valid JSON.|

- Return/Output Value: Resolves silently. The command does not produce visible output in the UI. The resulting parameter is accessible in all subsequent turns via dot notation for objects (e.g., @productInfo.name@) or index-based pathing for arrays.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 The Syntax Exception Rule and Parsing Lifecycle (CRITICAL)

Developers must strictly adhere to the No-Outer-Quotes Mandate.

1. Detection Phase: The CAFA engine identifies the @SETJ( prefix.
    
2. Literal Capture: It treats the segment from the first comma to the final closing parenthesis )@ as a raw string literal.
    
3. Regex Bypass: Unlike SET, which uses commas to split multiple arguments, SETJ uses only the first comma as a delimiter. This allows the JSON payload itself to contain commas (separating keys/values) without breaking the command.
    
4. Validation: If the captured string is not a valid JSON structure, the engine fails silently and initializes the parameter as an empty string "".
    

### 4.2 State Impact and the Dual-Indexing Mandate

SETJ commits the structured data to the params stack. The resulting data follows the specific indexing handover rules of the CAFA state machine:

1. Root-Level Access (Pedagogical 1-based): If the JSON parameter is a root-level array, access follows the CAFA pedagogical standard. The first object is accessed at index [1], the second at [2].
    

- Example: @Inventory[1].id@
    

2. Nested Access (Engineering 0-based): Once the engine moves "inside" a JSON object or into a nested property, it reverts to standard JavaScript/Engineering 0-based indexing.
    

- Example: If an object has a property tags: ["new", "sale"], the first tag is accessed via @Inventory[1].tags[0]@.
    

3. Next-Turn Rule (Atomicity): Due to the atomic nature of turn processing, a parameter set via SETJ in Turn N is not available for path-based access until Turn N+1.
    

### 4.3 Data Pipeline: The P2JSON Chaining Pattern

A sophisticated CAFA architectural pattern involves creating a "Data Pipeline" using P2JSON and SETJ to transform flat user input into structured intelligence:

- Turn N (Transformation): @P2JSON("UserNames|UserScores")@
    

- This merges two parallel pipe-separated lists into a single JSON array string.
    

- Turn N+1 (Crystallization): @SETJ(ClassRecord, @TR@TN(-1)@@)@
    

- This saves the generated string as a structured JP, applying the SETJ exception rule to the result of the previous turn (TR).
    

- Turn N+2 (Retrieval): @ClassRecord[1].UserNames@
    

- The data is now available as a structured object for high-fidelity presentation or LLM context.
    

## 5. Security and Integrity Implications

- Memory Volatility: JSON Parameters created via SETJ exist in the session's active memory. To ensure long-term persistence across sessions, the EXPORT command should be used to bundle these JPs into an Ontology Model.
    
- Sanitization: When populating SETJ with user input (via @TUt@), the developer must ensure that the user input does not contain unescaped double quotes, as this would invalidate the JSON structure and cause the SETJ command to fail during the hydration phase.
    

## 6. Reference

- Choi, J. (2025). SETJ Command: Define and Update JSON Parameters. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# JSONVALS Command: Extract and Flatten JSON Data

## 1. Metadata & Retrieval Keys

- Category: State Management / Data Transformation / JSON Utility
    
- Summary: A specialized bridge command that iterates through a JSON array of objects to extract values of a specific key and flattens them into a pipe-separated string compatible with AP logic and UI controls. It serves as the primary "Data Deserializer" for moving from complex hierarchical states to interactive linear states.
    
- RAG Keywords: JSONVALS, Extraction, DataParsing, ArrayConversion, ValuesOnly, JSONUtility, Flattening, JPtoAP, DataPipeline, BridgeLogic, Querying, Filtering, PatternMatching, ColumnSelector, StateTransformation, InteractionEvidence, UIAutomation, SchemaBridging, EpistemologicalFlattening, StateHydration, AttributeExtraction, Cross-SystemInteroperability, MacroExpansion, SemanticSlicing, LogicProjection, DistractorExtraction, OntologyRefinement.
    
- Related Commands: SETJ, P2JSON, RADIO, CHECKBOX, SELECT, INDEX, MAP, EVAL, TN(), SET, D().
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 The Operational Friction: Hierarchical Storage vs. Linear Interaction

In the CAFA Protocol, knowledge is often modeled as complex, nested structures using JSON Parameters (JP) to maintain depth and semantic relationships. However, CAFA’s symbolic UI controls (e.g., @RADIO()@, @CHECKBOX()@) and deterministic logic tools (e.g., @MAP()@, @INDEX()@) are architecturally optimized for flat, linear, pipe-separated strings ("A|B|C"). There is a structural disconnect between how data is stored (hierarchical) and how it is interacted with (linear). Without a bridge like JSONVALS, developers would be forced to maintain redundant parallel lists, leading to "Synchronicity Debt"—where the JSON database and the UI lists inevitably drift apart during runtime updates, causing logic failures and state corruption.

### 2.2 The Solution: The "Column Selector" Bridge

JSONVALS serves as the architectural "Column Selector" (analogous to a SQL SELECT [key] FROM [array]). It allows the CAFA engine to query a complex JP array and extract a specific attribute "column," flattening it into the pipe-delimited format required by the symbolic layer. This provides a "Unified Source of Truth" where the user interface is merely a dynamic, filtered view of the underlying JSON ontology. By projecting structured data into a linear format, JSONVALS preserves the sophistication of the knowledge base while ensuring the simplicity of the interaction.

### 2.3 Between-Turn Collective AI Logic

Within the Collective AI framework, JSONVALS enables a "Curator Micro-Agent" (a turn dedicated to data management) to maintain a complex database (JP) while allowing a "Presenter Micro-Agent" (a turn dedicated to UI) to easily extract and display only relevant user-facing labels. This process, termed Epistemological Flattening, ensures that the "Truth" remains stored in the structured JP, while the "Display" is dynamically generated. This separation of concerns reduces the "Cognitive Token Cost" for LLMs, as they do not need to parse raw JSON to generate options; the symbolic engine handles the extraction deterministically, ensuring that the distractors or options presented to a user are always exactly as defined in the ontology.

## 3. Formal Syntax & Parameter Schema (The "What")

### 3.1 The Mixed Quoting Rule

JSONVALS follows a unique quoting protocol: the parameter name is treated as a symbolic reference (unquoted), while the key and optional filter pattern are treated as string literals (quoted).

- Golden Template A: Standard Attribute Extraction  
    This template demonstrates extracting the "label" key from a JSON array stored in itemData to populate a Radio button.
    

{  
  "user": "/ T1: Present options extracted from a structured JSON array.\n@RADIO(\"user_choice\", \"Select an item:\", \"@JSONVALS(itemData, \"label\")@\")@",  
  "show": true  
}  
  

- Golden Template B: Conditional Filtering Extraction  
    This template extracts only the names of items marked as "correct" within an assessment JP.
    

{  
  "user": "/ T1: Extract correct answers for logic validation.\n@SET(\"CORRECT_LIST\", \"@JSONVALS(quizData, \"answer\", \"true\")@\")@",  
  "show": false  
}  
  

- Argument Table:
    

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Technical Description|
|json_param_name|String|Required|The name of the parameter holding the JSON array (e.g., inventory). DO NOT QUOTE.|
|"key"|String|Required|The specific JSON key whose values should be extracted. MUST BE QUOTED.|
|"pattern"|String|Optional|A string filter. Only objects where the value of the key contains this substring are returned. MUST BE QUOTED.|

- Return/Output Value: A Pipe-Separated String (e.g., "Value1|Value2|Value3").
    

- If the key is not found in an object, that entry is silently skipped.
    
- If the input is not a valid JSON array, it returns an empty string "".
    
- If the pattern results in no matches, it returns an empty string "".
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Lifecycle: The 5-Step Extraction Process

1. Hydration Phase: The engine identifies the json_param_name and retrieves the stored JSON string from the params stack.
    
2. Parsing Phase: The string is parsed into a memory-resident array of objects.
    
3. Scan & Match Phase: The engine iterates through the array.
    

- Pattern Filter: If a "pattern" is provided, the engine performs a substring check on the value of the targeted "key".
    
- Capture: Only values that exist and (if applicable) match the pattern are added to the extraction buffer.
    

4. Flattening Phase: The extraction buffer is joined using the CAFA delimiter (|).
    
5. Macro Injection: The resulting string is injected into the parent prompt string before the prompt is finalized for display or LLM processing. This allows the LLM to see the result as a standard list, completely unaware of the underlying JSON structure.
    

### 4.2 Pattern Matching as a Symbolic Query Engine

The optional third argument transforms JSONVALS into a functional query engine for Conditional UI Generation.

- Use Case: Extracting only "High-Priority" tasks from a project management JSON.
    
- Syntax: @JSONVALS(TaskList, "title", "high")@
    
- Consequence: This ensures that the user interface adapts dynamically to the current state of the data without requiring complex IF/ELSE loops or multiple symbolic turns.
    

### 4.3 The Isolation Pattern (Architectural Best Practice)

JSONVALS is optimized for simple arrays of objects ([{}, {}]). When dealing with deeply nested JSON structures (e.g., objects nested three levels deep), developers should utilize the Isolation Pattern to maintain performance and accuracy:

1. Isolate: Use @SETJ(TempArray, @RootObject[1].nestedCategory.items@)@ to pull the target array into a top-level, flat JP.
    
2. Extract: Use @JSONVALS(TempArray, "targetKey")@ to perform the extraction.
    
3. Impact: This ensures the engine's pointer is correctly positioned, prevents "Path Resolution Latency," and significantly reduces the regex overhead during the prompt hydration phase.
    

## 5. Security, State Integrity, and Failure Modes

- Delimitation Safety (Pipe Collisions): JSONVALS does not automatically escape pipes (|) within the data itself. If a JSON value contains a pipe (e.g., "Size: L|XL"), JSONVALS will treat this as two separate options when passed to a UI control like RADIO. Architects must sanitize source JSON data to ensure values do not contain reserved CAFA delimiters to prevent Ghost Option Injection.
    
- The Next-Turn Rule (Atomicity): While JSONVALS provides immediate results when used as a nested argument (e.g., inside @RADIO(...)@), if the result is stored via @SET()@, it follows the standard Atomicity Dependency. The extraction is committed during the turn transition and is only available for retrieval in Turn $N+1$.
    
- Type Coercion: JSONVALS strictly extracts values as strings. If the JSON value is a number or boolean, it is cast to a string during the flattening process. This is crucial for EVAL logic, where numeric strings may need to be wrapped in quotes.
    
- Fail-Soft Behavior: If a JSON array contains heterogeneous objects (some with the key, some without), JSONVALS simply skips the missing entries rather than throwing an error. This allows for "sparse" data structures.
    

## 6. Functional Implications for Assessment Engineering

In the context of Evidence-Centered Design (ECD), JSONVALS is used to reconstruct the "Interaction Space" from the "Student Model." For example, an agent can store a student's entire performance history as a JP and use JSONVALS to extract only the "incorrect_rationale" fields for a final review turn, allowing for focused, personalized feedback without cluttering the prompt with irrelevant data.

## 7. Reference

- Choi, J. (2025). JSONVALS Command: Extract and Flatten JSON Data. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

**

# EVAL Command: Execute JavaScript Math and Logic

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / Mathematical Operations
    
- Summary: A high-precision deterministic symbolic engine that parses and executes JavaScript-standard arithmetic and Boolean expressions at runtime, serving as the "Rationality Module" to ground generative stochasticity in empirical logic. It ensures that the agent's logic transitions are governed by rules rather than probabilities.
    
- RAG Keywords: EVAL, JavaScript, Arithmetic, Boolean, Logic, Calculation, MathObject, Deterministic
    
- Related Commands: SET, MAP, INDEX, TN(), REPEAT, JUMP, RADIO, TEXT, D().
    

## 2. Architectural Logic & Rationale (The "Why")

- The Operational Friction: Resolving Stochastic Hallucination: Foundation AI models are inherently probabilistic; they predict the "next most likely token" based on distributional weights rather than executing discrete mathematical or logical rules. Consequently, LLMs frequently fail at high-precision arithmetic, multi-step algebraic operations, or strict Boolean comparisons—a phenomenon known as "LLM Math Hallucination." In the context of Assessment Engineering (AE) or technical diagnostics, these errors degrade the validity of the entire agent. The EVAL command solves this by offloading computational and logical tasks to a deterministic symbolic processor, ensuring that the agent's "Rationality" is decoupled from its "Creativity."
    
- Between-Turn Collective AI Logic: The Truth Anchor: Within the CAFA Collective AI framework, EVAL acts as the cognitive bridge for Computational Intelligence. It allows a "Micro-Agent" (Turn) to perform a "Truth Check" on the interaction evidence generated by previous turns. For instance, if Turn 1 collects user input and Turn 2 generates a generative rationale, Turn 3 can use EVAL to perform a deterministic comparison against a key stored in the Ontology Model AP. This creates a "Truth Anchor" within the state machine, preventing the propagation of generative errors and ensuring that the final "Claim" about a user's ability is based on situated, verifiable evidence rather than probabilistic guesswork. Without EVAL, the agent lacks the "Rationality Module" required to sustain a rigorous assessment argument.
    
- Execution Mode: Deterministic Sovereignty: EVAL is a non-generative, system-level directive. It bypasses the probabilistic layer of the LLM entirely and executes within a restricted JavaScript sandbox. This guarantees $100\%$ repeatability, auditability, and mathematical precision across all turn transitions. This sovereignty is a prerequisite for any agent performing scoring, diagnostic, or adaptive routing functions where error tolerance is zero.
    

## 3. Formal Syntax & Parameter Schema (The "What")

- Golden Template: Complex Logic & Ternary Operations  
    This template demonstrates a nested EVAL within a SET command, utilizing relative turn numbering (TN), ternary logic, and the JavaScript Math object to calculate a weighted score and trigger a logic gate.
    

{  
  "user": "/ Calculate weighted score and apply a boolean pass/fail gate.\n@SET(\"RawScore\", \"@EVAL(\"Math.round(@TR@TN(-1)@@ * 1.5)\")@\")@\n@SET(\"IsPassed\", \"@EVAL(\"@RawScore@ >= 70 ? 'true' : 'false'\")@\")@",  
  "show": false  
}  
  

- Argument Table:
    

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Technical Description|
|"expression"|String|Required|A valid JavaScript-compatible math or logic string. Must be enclosed in double quotes. Supports arithmetic $(+, -, *, /, \%, **)$, comparisons $(>, <, >=, <=, ==, !=)$, bitwise operators, and ternary logic $(? :)$.|

- Return/Output Value: A String representation of the result (e.g., "42", "3.14159", "true", or "false").
    
- Extended Capabilities (Math Object): EVAL provides full access to the standard JavaScript Math library, enabling advanced scientific computation:
    

- Algebraic: Math.sqrt(x), Math.pow(x, y), Math.abs(x), Math.log(x), Math.exp(x).
    
- Rounding/Truncation: Math.floor(x), Math.ceil(x), Math.round(x), Math.trunc(x).
    
- Trigonometry: Math.sin(x), Math.cos(x), Math.tan(x) (Inputs in radians).
    
- Stochastic Control: Math.random() (Essential for symbolic shuffling, randomized item selection in CAT, or Monte Carlo simulations).
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 The 4-Stage Hydration & Execution Lifecycle

The EVAL command follows a precise order of operations to ensure data integrity during the "Prompt Hydration" phase:

1. Parameter Hydration (Level 0 - Macro Expansion): The engine scans the expression string and replaces all @Parameter@ placeholders with their literal string values retrieved from the AP or SP stacks. This occurs before the JavaScript parser is invoked.
    
2. Implicit Type Coercion: The engine attempts to coerce these strings into numbers or booleans for the JS engine. For example, the string "10" is treated as the literal 10.
    

- Critical Quoting Rule: Strings intended for literal comparison (non-numeric data) must be wrapped in single quotes within the double-quoted expression to prevent JS syntax errors.
    
- Correct: @EVAL("'@UserStatus@' == 'Active'")@
    
- Incorrect: @EVAL("@UserStatus@ == Active")@
    

3. Sandboxed Execution: The coerced expression is executed in an isolated, memory-limited JavaScript environment. This environment is "stateless" relative to the browser—it does not have access to window, document, or external network resources, ensuring high security and performance.
    
4. Result Stringification: The final JS output (e.g., a numeric 42 or a boolean true) is cast back into a CAFA-standard string. This is crucial because CAFA parameters are stored as strings to ensure cross-compatibility between AP, SP, and JP systems.
    

### 4.2 The Atomicity Constraint & Synchronization (Rule 6.2)

EVAL is subject to the Turn-Boundary Dependency Rule. Because turns are processed atomically, an EVAL command cannot access a parameter that was updated in the same turn.

- Race Condition (Fail Pattern): @SET("X", "1")@@EVAL("@X@ + 1")@ in Turn 5 will resolve based on the old value of X (or an empty string if it didn't exist), because the SET operation is committed to the state machine only at the turn boundary transition.
    
- Synchronization (Correct Pattern): * Turn 5 (Assignment): @SET("X", "1")@
    

- Turn 6 (Calculation): @EVAL("@X@ + 1")@
    

### 4.3 Advanced Implementation Patterns

- SCREAM Framework Scoring Logic (Diagnostic Eval):  
    @SET("ItemScore", "@EVAL(\"@RADIO(user_answer)@ == '@CorrectAnswer@' ? 1 : 0\")@")@  
    This enables automated, deterministic grading of selected-response items, providing the foundational data for the Diagnostic Evaluation pillar of the Trinity of Assessment (ToA).
    
- Dynamic Adaptive Routing (CAT Logic):  
    @JUMP(\"@MAP("@EVAL("@TotalScore@ >= 80")@", "true|false", "@TN("5")@|@TN("1")@", "@TN("2")@")@\")@  
    Using EVAL as a boolean predicate for the MAP command to drive non-linear, adaptive branching based on student mastery levels. This is the core engine for Computerized Adaptive Testing (CAT).
    
- Randomized Item Selection (Preventing Item Exposure):  
    @SET("TargetIndex", "@EVAL(\"Math.floor(Math.random() * @ItemList[N]@) + 1\")@")@  
    Then accessing the item via index indirection: @ItemList[@@TargetIndex@@]@. This pattern is critical for maintaining security in longitudinal assessments by ensuring students receive different items from a pool.
    
- Constructed Response Fidelity Checks:  
    @EVAL(\"'@TUt@'.length > 100 ? 'Valid' : 'Too Short'\")@  
    Used for automated fidelity checks on user-provided constructed responses. This ensures the interaction meets minimum evidence requirements (e.g., word count) before triggering an expensive LLM turn, thereby optimizing token usage and instructional quality.
    
- Time-Based Logic (Session Management):  
    @EVAL(\"Math.floor((@TIME@ - @StartTime@) / 60000)\")@  
    Calculating the elapsed minutes in a session to trigger "Time's Up" warnings or session-timeout jumps.
    

## 5. Reference

- Choi, J. (2025). EVAL Command: Execute JavaScript Math and Logic. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# EVAL Command: Ternary Logic Gates

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / State Transformation
    
- Summary: A specialized application of the EVAL command utilizing the JavaScript ternary operator ($condition \ ? \ true \ : \ false$) to implement concise, predicate-based conditional logic within a single turn string. It serves as the primary mechanism for binary branching based on quantitative interaction evidence.
    
- RAG Keywords: EVAL, TernaryOperator, BooleanLogic, PredicateLogic, LogicGate, ConditionalBranching
    
- Related Commands: EVAL (General), MAP, SET, JUMP, TN(), RADIO, TEXT, D().
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 The "Boolean Router" vs. The "List Matcher"

In the CAFA Protocol, conditional logic is bifurcated into two primary systems: Match-based logic (handled by MAP) and Predicate-based logic (handled by EVAL Ternary).

While the MAP command is architecturally optimized for matching a specific input against a discrete list of values (e.g., $A \rightarrow 1, B \rightarrow 2$), the EVAL Ternary operator is designed for Boolean Logic Gates. It evaluates a condition—typically involving comparisons ($>, <, ==$), logical operators ($&&, ||$), or truthiness checks—to project one of two possible outcomes. This makes it the ideal tool for "Pass/Fail" scenarios, threshold-based branching, and complex validations that cannot be easily listed as discrete keys. It represents the "Frontal Lobe" of the agent—the executive function that makes binary choices based on the raw data processed by the rest of the symbolic engine.

### 2.2 Cognitive Load and Logic Flattening

Using the ternary operator inside an EVAL command achieves significant Logic Flattening. In standard programming, an "If-Else" block increases the cognitive complexity and line count of the script. In the CAFA environment, every extra turn or nested JSON block adds to the "Instructional Overhead" and token consumption.

By encapsulating decision logic into a single line, the architect keeps the state machine compact and auditable. It functions as a Rationality Gate, ensuring that subsequent turns are grounded in a deterministic evaluation of previous interaction evidence rather than the probabilistic guesswork of a generative model. This is critical in high-stakes environments where an agent must justify why it routed a user to a specific remedial path.

### 2.3 Execution Mode: JavaScript Sandbox Context

Like the general EVAL command, ternary logic executes within a secure, stateless JavaScript sandbox. This ensures that the evaluation is performed with mathematical precision, completely independent of the LLM's stochastic nature. The result becomes a "hard" string that serves as the "Ground Truth" for the session. This deterministic output can then be utilized to drive UI controls, navigational jumps, or further symbolic assignments, effectively "locking in" the logic before the next generative turn begins.

## 3. Formal Syntax & Parameter Schema (The "What")

### 3.1 The Quoting Mandate and Escaping Rule

The most critical requirement for EVAL ternary logic is the strict hierarchy of quotes. Because the command itself is enclosed in double quotes ($"$), any literal strings inside the ternary expression (the outcomes) must be enclosed in single quotes ($'$).

Golden Template Syntax:

@EVAL("condition ? 'value_if_true' : 'value_if_false'")@

|   |   |
|---|---|
|Component|Technical Description|
|"condition"|A JavaScript expression resolving to a Boolean ($true/false$). Parameters like @SCORE@ >= 70 are hydrated before evaluation.|
|?|The ternary trigger; indicates the transition from the predicate to the potential outcomes.|
|'value_if_true'|The return value if the condition is truthy. Literals must be single-quoted; numeric results do not require quotes.|
|:|The binary separator; identifies the fallback (else) outcome.|
|'value_if_false'|The return value if the condition is falsy. Literals must be single-quoted.|

### 3.2 Output Versatility

The ternary operator is not limited to static labels. It can project dynamic state data:

- Numeric States: @EVAL("@TU1@ > 10 ? 100 : 0")@ (returns a raw numeric string for further math).
    
- Reference Chaining: @EVAL("@SCORE@ > 50 ? '@PassMsg@' : '@FailMsg@'")@ (injects the content of another parameter).
    
- Instructional Payloads: Returning a pipe-separated list (e.g., 'Hint1|Hint2') that can be parsed by INDEX or MAP in the very next turn.
    
- Boolean Flags: Returning 'true' or 'false' as strings to be used by the MAP command's switch logic.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 The Hydration Lifecycle

The CAFA engine processes ternary logic through a four-stage lifecycle:

1. Macro Expansion (Level 0 Hydration): The engine replaces all @Placeholder@ tokens with their current string values.
    

- Draft: @EVAL("@TU1@ >= 70 ? 'Pass' : 'Fail'")@
    
- Expanded: @EVAL("85 >= 70 ? 'Pass' : 'Fail'")@
    

2. Implicit Type Coercion: The engine interprets the expanded string as JavaScript. Crucially, it attempts to coerce strings like "85" into numeric literals. If the architect intends for string comparison, they must wrap the placeholder in single quotes: @EVAL("'@TU1@' == 'Yes' ? ...")@.
    
3. Sandbox Evaluation: The JS engine evaluates the truthiness of the predicate.
    
4. Stringification: The winning outcome is extracted and returned as a standard CAFA string, ready for display or further symbolic processing.
    

### 4.2 Handling Nested Ternaries (The Logic Chain)

For scenarios requiring a "Multi-Stage Gate" (more than binary but less than a full MAP list), EVAL supports Nested Ternary Logic. This effectively implements an $if-else-if$ chain in a single line.

Syntax Example (Grading Scale):

@EVAL("@Score@ >= 90 ? 'A' : (@Score@ >= 80 ? 'B' : (@Score@ >= 70 ? 'C' : 'F'))")@

## 5. Implementation Patterns

### Pattern 1: Deterministic Grading (Evidence-Centered Design)

In Evidence-Centered Design (ECD), the agent must convert raw performance (a number) into an interpretive claim (a status).

{  
    "user": "/ This hidden turn determines if the student has reached mastery.\n@SET(Status, \"@EVAL(\"@UserScore@ >= @PASSING_THRESHOLD@ ? 'Mastery Achieved' : 'Remediation Required'\")@\")@",  
    "show": false  
}  
  

### Pattern 2: Dynamic Instruction Injection

Ternary logic can be used to inject specific instructions into a System Prompt based on previous errors, effectively personalizing the AI's "Coaching Style" without multiple prompt variants.

{  
    "system": "You are a helpful tutor. @EVAL(\"@ErrorCount@ > 2 ? 'Be more encouraging and provide a step-by-step hint.' : 'Keep your hints brief and challenge the user.'\")@",  
    "user": "@TUt@",  
    "model": "gpt-4.1-nano"  
}  
  

### Pattern 3: Semantic Logic Switches (Persona/Tone)

This pattern dynamically switches the system persona based on a boolean interaction flag, such as whether the user selected "Professional" or "Casual" mode.

{  
    "system": "You are a @EVAL(\"'@Mode@' == 'Advanced' ? 'Strict Professor of Quantum Physics' : 'Friendly Science Communicator'\")@. Answer the user's question accurately.",  
    "user": "@TUt@",  
    "model": "gpt-4.1-nano"  
}  
  

### Pattern 4: Adaptive List Generation

Returning different "Action Lists" based on performance. This allows Turn $N+1$ to iterate through different sets of tasks using the same REPEAT logic, enabling truly adaptive workflows.

{  
    "user": "/ Determine the remediation path list.\n@SET(NextSteps, \"@EVAL(\"@ErrorCount@ == 0 ? 'Review|Module 2' : 'Remediate|Module 1|Practice')@\")@\")@",  
    "show": false  
}  
  

## 6. Comparison: EVAL Ternary vs. MAP

|   |   |   |
|---|---|---|
|Feature|MAP Command|EVAL Ternary Operator|
|Logic Type|Match-based ($Match \rightarrow Result$)|Predicate-based ($Condition \rightarrow Result$)|
|Complexity|Best for many discrete options ($N+1$ Rule).|Best for binary/nested comparisons ($>, <, ==$).|
|Operators|Containment/Exact matching only.|Full JavaScript ($>, <, ==, !=, \&\&, \\|$).|
|Default|Mandatory final item in list (default case).|Required "Else" ($falsy$) outcome.|
|Primary Use|Routing by Selection (RADIO/SELECT).|Routing by Performance (Scoring/Math).|
|Flexibility|High for large datasets/lookups.|High for complex logic/calculated gates.|

## 7. Troubleshooting & Common Pitfalls

1. The Quote Collision: Forgetting single quotes around literal outcomes inside @EVAL(...)@. This is the #1 cause of agent execution crashes.
    
2. Type Mismatch: Comparing a string variable to a number without allowing the engine to coerce it. Always ensure the "Condition" side is mathematically valid.
    
3. Logic Deep-Nesting: While nesting ternaries is powerful, nesting more than 3 levels deep significantly reduces human readability and makes the JSON difficult to maintain. For complex multi-branching, switch to the MAP command.
    
4. Empty Outcomes: If an outcome is intended to be an empty string, it must still be represented as ''. Example: @EVAL("@Score@ > 10 ? 'High' : ''")@.
    

## 8. Reference

- Choi, J. (2025). Conditional Logic: EVAL Ternary Operator. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---

# MAP Command: Route Logic via Conditional Lookup

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / State Transformation
    
- Summary: A high-precision deterministic lookup engine that projects an input value onto a discrete set of return values based on predefined matches. It serves as the primary "Symbolic Router" for non-linear state transitions, automated scoring, and adaptive content delivery, ensuring that agent behavior is governed by empirical evidence rather than stochastic inference.
    
- RAG Keywords: MAP, ConditionalLogic, Routing, SwitchCase, N+1Rule, SymbolicInteraction, StateDrivenBranching
    
- Related Commands: JUMP, REPEAT, SET, EVAL, INDEX, RADIO, CHECKBOX, TN(), D(), SELECT, IMPORT, EXPORT, JSONVALS.
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Resolving Branching Complexity and Cognitive Debt

In traditional generative or scripted environments, handling multiple logic paths typically requires nested IF-ELSE structures or complex boolean trees. As the number of conditions grows, these structures manifest as Cognitive Debt—complex, indent-heavy blocks of code that are difficult to audit, prone to "unhandled case" hallucinations, and mathematically fragile. In a production environment, a 10-way branch implemented via nested logic is a primary point of failure.

The MAP command resolves this by implementing Logic Flattening. It transforms deep, branching decision trees into a single-line, data-driven lookup table. This shift ensures that the relationship between user evidence (input) and the resulting state (output) is explicit, transparent, and horizontally scalable. By moving logic from the code structure to a parameter-driven list, the architect can maintain thousands of potential paths without increasing the complexity of the execution prompt or the token count of the instruction set.

### 2.2 Between-Turn Collective AI Logic: The Switchboard

Within the CAFA Collective AI framework, an agent is conceptualized not as a monolithic prompt, but as a sequence of specialized Micro-Agents (Turns). MAP acts as the "Cognitive Switchboard" connecting these agents. It allows a "Diagnostic Micro-Agent" in one turn to classify a user's performance level (e.g., "Novice", "Intermediate", "Expert"), which MAP then projects onto a specific "Instructional Path" or "Jump Target" for the subsequent turn.

This decoupling of logic (the command) from the data (the pipe-separated lists) allows for Agile Agent Modeling. Architects can hot-swap behavioral strategies by simply updating the Agent Parameters (AP) via an IMPORT or SET command without altering the core execution instructions. This modularity is what enables CAFA agents to evolve in real-time based on session metadata, effectively allowing the agent to "change its mind" about the workflow based on symbolic evidence.

### 2.3 Execution Mode: Deterministic Mapping vs. Stochastic Inference

MAP is a non-probabilistic, system-level directive. While an LLM might "guess" which path to take based on the conversational context, MAP operates within the CAFA engine's symbolic layer to ensure that for a given input, the outcome is $100\%$ predictable.

This is essential for maintaining Epistemological Integrity in high-stakes environments—such as medical diagnostics, legal reasoning, or formal assessment—where the "Logic of the Jump" must be legally or scientifically defensible. In these scenarios, "hallucinated routing" (where an AI takes a wrong turn due to prompt noise) is a critical failure; MAP provides the mathematical warrant required to justify every state transition in the session log.

## 3. Formal Syntax & Parameter Schema (The "What")

### 3.1 Syntax Structure

The MAP command follows a strict three-argument structure. It is almost always nested inside navigational commands like JUMP or state-assignment commands like SET.

- Golden Template A: Adaptive Routing Pattern  
    This template demonstrates how MAP determines a JUMP target based on a user's performance score calculated via a previous EVAL turn.
    

{  
  "user": "/ Route user to remedial, standard, or advanced turns based on score.\n@JUMP(\"@MAP(\"@EVAL(\"@Score@ >= 80 ? 'High' : (@Score@ >= 50 ? 'Mid' : 'Low')\")@\", \"High|Mid|Low\", \"@TN(\"5\")@|@TN(\"3\")@|@TN(\"1\")@\", \"@TN(\"1\")@\")@\")@",  
  "show": false  
}  
  

- Golden Template B: Dynamic Persona Swapping  
    Assigning a system persona based on user sentiment or domain choice.
    

{  
  "user": "/ Set the agent persona based on user's professional domain.\n@SET(\"AGENT_ROLE\", \"@MAP(\"@TU1@\", \"Healthcare|Finance|Tech\", \"Medical Expert|Financial Advisor|Technical Support\", \"General Assistant\")@\")@",  
  "show": false  
}  
  

- Argument Table:
    

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Technical Description|
|"value"|String|Required|The input string to be evaluated. This can be a static string, a System Parameter (@TU1@), or the result of a nested command (@EVAL(...)@).|
|"value_list"|String|Required|A pipe-separated string representing the "Keys" in the lookup table. The engine scans this list for an exact match.|
|"return_list"|String|Required|A pipe-separated string representing the outcomes. Must adhere to the N+1 Rule.|

### 3.2 The N+1 Rule: The Mathematical Mandate

The integrity of the MAP command relies on the specific $N+1$ ratio between the key-list and the result-list. This rule ensures there are no unhandled exceptions in the logic flow, effectively creating an ELSE clause for every lookup.

1. The $N$ Matches: The first $N$ items in the return_list correspond $1$-to-$1$ with the items in the value_list. If the input matches the $i$-th item in the value_list, the $i$-th item in the return_list is returned.
    
2. The $+1$ Default: The final item in the return_list (the $N+1$ position) is the "Catch-all" or Default Value. This value is returned if and only if the input does not match any key in the value_list.
    
3. The Null Default Pattern: If a developer wishes to return an empty string for unrecognized inputs (common in "Display Filters"), they must terminate the return_list with a trailing pipe (e.g., "A|B|"), which creates an empty $(N+1)$ segment.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 The Lookup Lifecycle and Internal Resolution

The CAFA engine processes MAP in a multi-stage hydration lifecycle during the pre-processing phase:

1. Hydration Phase: The engine resolves all inner parameters. If MAP is nested (e.g., inside an EVAL), the inner commands are executed first. The engine ensures that the "value" argument is a clean string before the lookup begins.
    
2. Sequential Scanning: The engine performs a linear, index-based scan of the value_list. It uses an Exact Match protocol; trailing whitespaces or case differences (unless normalized) will prevent a match. Substrings do not trigger a match unless the entire segment is identical to the input.
    
3. Pointer Projection: * If a match is found at the $i$-th position (1-based), the engine stores the index $i$.
    

- If the scan completes without a match, the index pointer is automatically set to $N+1$.
    

4. Outcome Retrieval: The engine retrieves the item at the stored index $i$ from the return_list.
    
5. Substitution: The resolved return value is substituted into the parent prompt or command, and the hydration continues.
    

### 4.2 Pattern Comparison: MAP vs. EVAL

While EVAL can handle simple ternary logic (condition ? true : false), MAP is architecturally superior for Multivariate Selection.

- EVAL is optimized for binary mathematical comparisons and raw calculation. It is the "Arithmetric Unit" of the agent.
    
- MAP is optimized for categorical routing, ontology lookup, and managing large sets of discrete outcomes (e.g., mapping $50$ state codes to $50$ specific tax regulations). It is the "Control Unit" of the agent.
    

### 4.3 Advanced Implementation Patterns

- The "State Machine Router" (SMR): In complex diagnostic loops, MAP determines the next "Cognitive State." For example, mapping a user's answer "I don't understand" to a "Clarification Turn" while mapping "Proceed" to a "Content Turn." This allows for the creation of non-linear state machines within a single JSON agent.
    
- The SCREAM Framework (Automated Feedback): This pattern maps a student's specific distractor (incorrect answer) to a targeted pedagogical rationale.
    

- Syntax: @MAP("@RADIO(ans)@", "@DistractorList@", "@RationaleList@", "Excellent choice!")@
    
- Impact: Provides immediate, deterministic feedback that mirrors a human tutor’s specificity without the latency or "Model Drift" of a generative turn.
    

- The "Sentiment Logic Switch": Using a high-speed LLM turn to categorize sentiment into Positive|Neutral|Negative, then using MAP in a subsequent hidden turn to switch the agent's @PERSONA@ parameter to match the user's emotional state.
    
- The "Display Filter" Logic Gate: Using MAP to return a Markdown string or an empty string to dynamically show/hide instructional blocks based on the user's progress through a REPEAT loop. This is essential for building "Progressive Disclosure" interfaces.
    

## 5. Security, State Integrity, and Error Handling

### 5.1 Delimitation Integrity and "Ghost Matches"

A critical failure mode occurs if a return value itself contains a pipe character (|). Because MAP uses the pipe as a hard delimiter to count items for the $N+1$ Rule, an internal pipe will shift the index of every subsequent item, leading to "Index Drift" and catastrophic logic failure.

- Mandate: Architects must sanitize all data used in MAP outcomes. If pipes are required in the final output string, they should be replaced with a placeholder (like [PIPE]) and restored in a subsequent turn, or the architect should utilize JSONVALS to extract data from a structured JP object where delimiters are encapsulated.
    

### 5.2 Atomicity Dependency

If the result of a MAP is stored via the SET command, the Next-Turn Rule applies. The result is committed during the turn transition and is only available for retrieval in Turn $N+1$. However, if MAP is used within a navigational command like JUMP, it resolves and executes the pointer shift within the same turn cycle, allowing for immediate redirection.

### 5.3 Normalization and Robustness

Standard MAP execution is case-sensitive. To ensure logical robustness, especially when dealing with user-typed text (@TU@), it is a best practice to wrap the input in an EVAL function that normalizes case:

- Robust Syntax: @MAP("@EVAL(\"'@TU1@'.toLowerCase()\")@\", \"yes|no\", \"Target1|Target2\", \"Default\")@
    

## 6. Functional Implications for Assessment Engineering

In Evidence-Centered Design (ECD), MAP is the primary tool for the Evidence Rules layer. It converts raw task performance (a user's click or text) into an observation (a score or a competency flag). By explicitly defining these mappings in the params object, the agent becomes an "Open Book" for auditors; one can trace exactly why a user was routed to a specific remedial turn based on their previous interaction evidence.

This transparency is the foundation of Algorithmic Accountability in AI. MAP ensures that the "Warrant" for any instructional decision is based on a deterministic projection of evidence onto an ontological model, rather than the "Black Box" reasoning of a neural network.

## 7. Reference

- Choi, J. (2025). Conditional Logic: MAP Command. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# REPEAT Command: Iterate and Loop Through Turns

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / State Machine Orchestration
    
- Summary: The primary navigational directive for executing sequences of turns multiple times. It facilitates multi-item workflows, recursive refinement, and deterministic data aggregation by managing a local loop stack and the @R_i@ iteration index.
    
- RAG Keywords: REPEAT, Looping, Iteration, Turn Logic, State Machine,
    
- Related Commands: JUMP, END, TN(), TR, SET, SETJ, EVAL, MAP, INDEX, JSONVALS, D().
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Resolving the Linearity Constraint and Temporal Bottlenecks

Generative AI models are fundamentally sequential and "chat-centric." In their native state, they process a single thread of context in a one-way path, treating every interaction as a linear progression. Without iterative control, an agent is restricted to a "one-shot" interaction pattern. This architectural limitation makes it impossible to perform high-stakes tasks that require revision, batching, or parallel evaluation—such as scoring a 10-item quiz, refining a complex draft through multiple evolutionary cycles (GAMER), or generating a batch of synthetic data (IOTA) without manually defining every single turn in the JSON structure.

The REPEAT command transforms the CAFA agent from a linear script into a Looping State Machine. By implementing a symbolic execution loop, the protocol allows a small set of "Logic Turns" to process an arbitrary amount of "Data Atoms." This effectively decouples the complexity of the task from the length of the agent's code, enabling a "Compact Logic" architecture where 3 turns can manage an interaction of infinite length.

### 2.2 Between-Turn Collective AI Logic: Temporal Collaboration

Within the CAFA framework, we conceptualize turns as distinct Micro-Agents. REPEAT orchestrates Temporal Collaboration between these agents. It allows a single "Expert Micro-Agent" turn (e.g., an "Evaluator") to be reused across varying contexts within a single session. For example, a "Scoring Turn" can be defined once and then repeated for every user response in a list.

This ensures that the logical criteria for success remain consistent and centralized. It reduces Prompt Bloat (redundant instructions) and ensures that the agent's behavioral Warrant—the logical justification for its decisions—is identical across every iteration of a task. This consistency is vital for maintaining Epistemological Integrity in assessment and diagnostic workflows.

### 2.3 The "Repeat Spell" Pattern: The Tripartite Workflow

In advanced CAFA modeling, developers use the "Repeat Spell" idea. A "Spell" is a multi-turn sequence (usually 2-3 turns) designed to perform a complex generative or logical operation that is "cast" repeatedly via the REPEAT command. This pattern follows a strict Tripartite Workflow:

1. The Cast (Generation/Interaction): A turn that generates content, asks a question, or collects interaction evidence.
    
2. The Channel (Logic/Transformation): A turn that evaluates, scores, or transforms that evidence using symbolic commands like EVAL or MAP. This turn is often hidden ("show": false) to serve as the engine's "inner monologue."
    
3. The Bind (Aggregation/Crystallization): The final exit of the loop where the engine automatically "crystallizes" the results into a structured format (Pipe or JSON) for downstream use.
    

## 3. Formal Syntax & Parameters (The "What")

### 3.1 Command Structure

The command defines a "Loop Block" by identifying the starting turn, the ending turn, and the total number of cycles.

@REPEAT(start_turn, end_turn, count)@

|   |   |   |   |
|---|---|---|---|
|Argument|Data Type|Requirement|Technical Description|
|start_turn|String/Integer|Required|The index of the turn where the loop begins. Always reference via @TN(t)@ to ensure the logic survives turn insertions or deletions (Structural Loose Coupling).|
|end_turn|String/Integer|Required|The index of the turn where the loop evaluates its exit condition. Usually the current turn pointer.|
|count|String/Integer|Required|The total number of iterations. Can be a static integer, a dynamic parameter (e.g., @ItemCount@), or the length of a list retrieved via @INDEX(LIST, "COUNT")@.|

### 3.2 The @R_i@ Iteration Index: The Pointer of State

During a loop, the engine provides the reserved System Parameter @R_i@. This $1$-based integer tracks the current iteration and serves as the primary pointer for data mapping.

- Scope and Lifecycle: @R_i@ is updated after the turn boundary transition. Inside a loop, referencing @R_i@ always yields the current cycle count.
    
- Dynamic Mapping: It is used to "slice" parallel lists. Example: Accessing the current question in a quiz: @Questions[@R_i@]@ or the current user answer @RADIO(ans_@R_i@)@.
    
- Nested Contexts: In nested loops, @R_i@ refers to the index of the innermost active loop. To access outer loop indices, they must be stored in a custom parameter via @SET(Outer_i, "@R_i@")@ before entering the inner loop.
    

## 4. Intelligent Result Aggregation

A unique feature of REPEAT is its ability to automatically synthesize the results of all iterations into a single, usable data format stored in the TR (Turn Result) of the turn that initiated the REPEAT command.

### 4.1 Heuristic Detection Logic

Upon the termination of a loop, the engine performs a high-speed heuristic analysis on the first non-whitespace character of the output produced in the first iteration ($R_i=1$):

- Strategy A (Pipe/AP Aggregation): If the result is plain text, numbers, or standard symbolic strings, the system aggregates them into a Pipe-Separated List (e.g., Val1|Val2|Val3). This is the default for parameters intended for RADIO, INDEX, or MAP.
    
- Strategy B (JSON/JP Aggregation): If the result starts with {, indicating a JSON object, the system aggregates them into a JSON Array (e.g., [{"id":1}, {"id":2}]). This ensures that iterative structured data is immediately valid for SETJ or JSONVALS without further cleanup.
    
- Strategy C (Fallback/Mixed): If iterations produce heterogeneous data (e.g., iteration 1 is JSON, iteration 2 is text), the engine defaults to Pipe Aggregation to prevent syntax errors in JSON parsing.
    

### 4.2 The "Spell" Aggregation Lifecycle

1. The Gathering (Buffering): Individual outputs from every turn within the loop block are held in a temporary, temporal loop buffer.
    
2. The Synthesis (Formatting): Upon the final iteration's exit, the engine applies the detected delimiter (pipe or comma/bracket).
    
3. The Manifestation (Commit): The final aggregated string is committed to the TR of the turn that called @REPEAT@. It is now accessible via @TR@TN(-t)@.
    

## 5. Execution Mechanics & Life Cycle (The "How")

### 5.1 The Loop Stack and Recursion

CAFA manages iterations using a Loop Stack. This allows for sophisticated nested logic where a loop can contain another loop.

1. Instantiation: When the engine hits @REPEAT@, it pushes a new loop state to the stack, initializing @R_i@ to $1$.
    
2. Sequential Execution: The engine executes all turns from start_turn to end_turn.
    
3. Boundary Evaluation: At the conclusion of end_turn, the engine performs an arithmetic check: Is @R_i@ < count?
    

- The Continue Path: If true, the turn pointer resets to start_turn and @R_i@ increments.
    
- The Exit Path: If false, the loop state is popped from the stack, and execution proceeds to the next turn in the sequence.
    

4. Infinite Loop Protection: To prevent server-side resource exhaustion, the engine enforces a hard limit of $1,000$ total turn-jumps (including loops) per session. If a REPEAT count is too high or logic is circular, the session terminates safely.
    

### 5.2 Pre-Hydration and symbolic Resolution

Loop boundaries defined via @TN()@ are resolved before the first iteration begins. This ensures that even if the turn indices change dynamically during execution (due to some other complex logic), the loop boundaries remain anchored to the intended logical block.

## 6. Security, State Integrity, and Failure Modes

- Turn-Boundary Atomicity: Parameters set inside a loop (via SET) are available in subsequent iterations. This allows for "Accumulator Patterns" (e.g., @SET(Total, "@EVAL("@Total@ + @Current@")@")@).
    
- Aggregation Availability: Aggregated results of the entire loop are only available after the loop terminates. Accessing @TR@TN(-1)@@ during the loop will return the result of the turn prior to the loop starting.
    
- Null Handling: If an iteration produces an empty string "", it is preserved in the aggregation to maintain index parity. In a pipe list, this results in a "Null" segment (e.g., A||C). In JSON mode, it results in a blank entry, which may invalidate the array if not handled via a default object {}.
    
- Structural Fragility: Always use TN() relative numbering. Hardcoding absolute indices (e.g., "5") is a primary source of "Logic Drift," where simple agent edits break complex loop structures.
    

## 7. Advanced Design Patterns

### 7.1 The GAMER Pattern (Recursive Refinement)

This pattern involves a loop where the LLM critiques its own output from the previous iteration to improve quality.

- Iteration 1: Generate initial draft.
    
- Iteration 2: Critique Draft 1 and generate Draft 2.
    
- Iteration 3: Critique Draft 2 and generate Final Draft.
    

### 7.2 The IOTA Pattern (Synthetic Item Generation)

Used for generating massive item banks. A single "Logic Turn" is defined to generate a JSON object representing a quiz question. The REPEAT command is then used to generate 50 unique items, which are aggregated into a single JSON array and saved to a database via SETJ and EXPORT.

## 8. Golden Template: The "Quiz Spell" Pattern

This agent demonstrates a fully compliant CAFA JSON structure utilizing the "Quiz Spell" pattern. It includes all mandatory keys (name, params) and initializes state via @IMPORT@.

{  
    "options": {  
        "name": "Quiz_Spell_Aggregation_Demo_v1",  
        "title": "Interactive Quiz Aggregator",  
        "brief": "Demonstrates iterative turn logic and automatic result aggregation.",  
        "description": "This agent asks a series of quiz questions in a loop, grades them instantly, and presents a summarized report at the end.",  
        "greeting": "Welcome! I will now evaluate your knowledge through a series of questions.",  
        "params": {  
            "QUESTIONS": { "org": "Capital of France|2+2|Red Planet", "cond": "SELF" },  
            "ANSWERS": { "org": "Paris|4|Mars", "cond": "SELF" }  
        }  
    },  
    "prompts": [  
        {  
            "user": "/ T1: Initialize parameters and start loop.\n@IMPORT@\n@REPEAT(\"@TN(1)@\", \"@TN(2)@\", \"3\")@",  
            "show": false  
        },  
        {  
            "user": "/ T2: The 'Cast' (Visible). Ask question @R_i@.\n@RADIO(\"ans_@R_i@\", \"@QUESTIONS[@R_i@]@\", \"Paris|London|4|5|Mars|Venus\")@",  
            "show": true  
        },  
        {  
            "user": "/ T3: The 'Channel' (Logic). Check answer and output status.\n@EVAL(\"'@RADIO(ans_@R_i@)@' == '@ANSWERS[@R_i@]@' ? 'Correct' : 'Incorrect'\")@",  
            "show": false  
        },  
        {  
            "user": "/ T4: The 'Bind' (Presentation). Aggregated results from T3 are shown.\nFinal Grade List: @TR@TN(-1)@@",  
            "show": true  
        }  
    ]  
}  
  

## 9. Reference

- Choi, J. (2025). REPEAT Command: Iterate and Loop Through Turns. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    
---
# JUMP Command: Control Execution Flow and Branching

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / State Machine Orchestration
    
- Summary: The universal symbolic router for non-linear state transitions. It allows an agent to dynamically re-point the execution pointer to a specific turn index based on real-time diagnostics, user input, or calculated scores, enabling complex adaptive workflows that deviate from sequential instruction sets.
    
- RAG Keywords: JUMP, Branching, Routing, Non-linear, State Machine, Navigation, Logical Routing, Conditional Jump, Flow Control, Micro-Agent Coordination.
    
- Related Commands: REPEAT, END, TN(), MAP, EVAL, SET, INDEX, TR, TU, TS, D().
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Decoupling from Generative Linearity: Determinism over Probability

Generative AI models are fundamentally sequential; they process context in a one-way temporal path, predicting tokens based on distributional probability. Without a symbolic redirection layer, an agent is trapped in a linear conversation where the only way "forward" is more generation. This linearity makes it architecturally impossible to implement sophisticated logic like "skip logic," "remedial loops," or "advanced pathways" without overwhelming the context window with contradictory instructions.

The JUMP command provides the Symbolic Redirection required to transform the LLM from a simple chatbot into a complex adaptive system. By using JUMP, the architect defines a multi-path workflow where the "next step" is determined by empirical evidence (symbolic data) rather than the next token prediction. This ensures that the agent follows a strictly defined logical path, preserving Epistemological Integrity in high-stakes environments like assessment or technical troubleshooting.

### 2.2 Between-Turn Collective AI Logic: The Task Switcher and Persona Orchestrator

In the CAFA ecosystem, we view the agent as a Collective of Micro-Agents. Each turn index typically represents a specific task, persona, or cognitive state. JUMP acts as the primary Task Switcher. For example, after a diagnostic turn, the agent might evaluate user performance and "Jump" to a "Coach" persona in Turn 10 if the user fails, or to a "Challenger" persona in Turn 20 if the user succeeds.

This enables a form of Micro-Agent Coordination where the current turn evaluates the environment and programmatically decides which specialized version of itself (or which different Micro-Agent entirely) should handle the next interaction. This modularity allows for "Agile Modeling," where complex agents are built from smaller, reusable turn-blocks connected by JUMP logic.

### 2.3 Execution Mode: Symbolic Sovereignty

JUMP is a deterministic system-level directive. It is executed directly by the CAFA engine's navigation controller, bypassing the LLM's probabilistic nature entirely. This ensures that transitions are $100\%$ predictable and auditable. In practice, JUMP is almost always utilized within hidden turns ("show": false) to serve as a "Logic Gate" or "Pre-processor." This allows the engine to perform its internal routing "behind the curtain," maintaining a seamless and coherent experience for the end-user while the underlying state machine shifts gears.

## 3. Formal Syntax & Parameter Schema (The "What")

### 3.1 Syntax Structure

The command takes a single argument: the index of the target turn.

@JUMP("target_turn")@

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Technical Description|
|"target_turn"|String|Required|The index of the turn to transition to. This must resolve to a valid integer. Supported sources include static integers, TN() references, or the output of nested MAP or EVAL logic.|

### 3.2 The Mandatory Use of TN(): Ensuring Structural Loose Coupling

To prevent Structural Fragility, developers must strictly avoid hardcoding absolute turn indices (e.g., @JUMP("15")@). In an agile development cycle, turns are frequently inserted or deleted to refine logic. If absolute pointers are used, a single edit at the beginning of the agent can break every downstream jump.

- The Principle of Loose Coupling: By using @TN(t)@, the logic becomes relative.
    
- Relative Jumps: @JUMP("@TN("-2")@")@ instructs the engine to "jump back two turns," regardless of their absolute index.
    
- Absolute Reference via TN: @JUMP("@TN(5)@")@ identifies the 5th turn in the current prompt array, allowing the engine to handle internal indexing updates automatically if the structure changes.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 The Hydration & Redirection Lifecycle

The JUMP command follows a strict pre-execution hydration sequence within the CAFA engine:

1. Macro Expansion (Level 0): The engine resolves all standard parameters (e.g., @Score@, @UserStatus@) embedded within the jump string.
    
2. Symbolic Resolution (Level 1): If the jump target is a dynamic command like MAP or TN(), the engine executes that logic first to calculate the final destination as a raw integer.
    
3. Pointer Hijacking: The CAFA engine intercepts the standard sequential pointer (the default $T_i + 1$) and overrides it with the resolved target_turn value.
    
4. Context Preparation: The engine "flushes" the current turn execution and prepares the target turn as the active state. Note: JUMP does not clear the params stack; all Agent Parameters (AP) persist across the transition, ensuring continuity of the student model or session state.
    

### 4.2 Pattern: The Multi-Branch Assessment (Scoring Gate)

Combining EVAL, MAP, and JUMP creates a "Scoring Gate" that routes users into three distinct instructional streams based on performance.

{  
  "user": "/ Route based on three-tier scoring: <50 (Remedial), 50-80 (Standard), >80 (Advanced).\n@JUMP(\"@MAP(\"@EVAL(\"@Score@ >= 80 ? 'Adv' : (@Score@ >= 50 ? 'Std' : 'Rem')\")@\", \"Adv|Std|Rem\", \"@TN(20)@|@TN(10)@|@TN(5)@\", \"@TN(10)@\")@\")@",  
  "show": false  
}  
  

### 4.3 Pattern: The Error Recovery and Validation Loop

A JUMP can be used to create a "Validation Loop" where a user is returned to an input turn if their provided data fails a symbolic check (e.g., word count or regex).

{  
  "user": "/ If text length < 50, jump back to T1 (Input), else proceed to T3 (Analysis).\n@JUMP(\"@MAP(\"@EVAL(\"'@TU1@'.length >= 50\")@\", \"true|false\", \"@TN(1)@|@TN(-1)@\", \"@TN(1)@\")@\")@",  
  "show": false  
}  
  

## 5. Security, State Integrity, and Failure Modes

### 5.1 The Infinite Loop Trap and Recursion Depth

Unlike the REPEAT command, which manages a local iteration stack, JUMP is "stateless" navigation. If an architect jumps backward (e.g., @JUMP("@TN("-3")@")@) without a conditional exit or an incrementing counter, they create a "Logic Deadlock."

### 5.2 The "Next-Turn" Execution Constraint

A JUMP command only takes effect after the current turn has completed its full lifecycle (Hydration -> Display -> Result Capture). You cannot "Jump" midway through a prompt to truncate it; the command merely determines the destination once the current turn is finished.

### 5.3 Target Nullification and Graceful Failure

If a JUMP resolves to a target that is out-of-bounds (e.g., Turn 500 in a 10-turn agent) or a non-integer string (e.g., "Home"), the engine executes Target Nullification. It ignores the jump and defaults to the standard sequential execution ($T_i + 1$). This "Fail-Safe" prevents the session from crashing due to malformed logic or edge-case scoring results.

## 6. Reference

- Choi, J. (2025). Logic & Flow Control: JUMP Command. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# END Command: Terminate and Close Agent Session

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / Session Lifecycle Management
    
- Summary: The definitive symbolic directive for the immediate termination of an agent session. It provides a "Hard Exit" mechanism that closes the execution pipeline, prevents further turn transitions, and triggers final state persistence protocols.
    
- RAG Keywords: END, Exit, Termination, SessionControl, Stop, FlowControl, HardExit, SessionLifecycle.
    
- Related Commands: JUMP, REPEAT, SAVE, EXPORT, LOG, TN(), TR.
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 The Necessity of the "Hard Exit"

In a complex adaptive system composed of non-linear jumps and iterative loops, establishing a clear execution boundary is critical. Without a dedicated termination command, an agent might inadvertently continue into empty turns or become trapped in circular logic. The END command provides the Symbolic Boundary required to signal the successful (or unsuccessful) completion of a task. It ensures that the session does not "wander" into undefined states, maintaining the professional integrity of the user experience and the efficiency of the platform's processing resources.

### 2.2 Session Lifecycle Orchestration

In the CAFA ecosystem, the END command acts as the final orchestrator of the session lifecycle. While JUMP and REPEAT manage the active "Movement" of the state machine, END manages its "Crystallization." Upon execution, the engine recognizes that no further turns are required. This allows the system to finalize the session log and prepare any data for long-term storage or reporting. It is the architectural equivalent of a "return" statement in a function, closing the scope of the current interaction.

### 2.3 Execution Mode: Deterministic System Directive

END is a non-generative, system-level command. It is processed by the CAFA engine's session controller with absolute priority. Once an @END@ token is hydrated and executed, all subsequent commands in the same turn are ignored, and the session is transitioned to a "Closed" state. To ensure a professional UI experience, it is often placed in a final "Summary Turn" where the agent delivers its closing remarks before shutting down the pipeline.

## 3. Formal Syntax & Parameter Schema (The "What")

### 3.1 Syntax Structure

The command is a standalone symbolic directive and requires no arguments.

@END@

|   |   |   |   |
|---|---|---|---|
|Component|Type|Requirement|Technical Description|
|@END@|Token|Required|The reserved symbolic trigger for session termination.|

### 3.2 Strategic Placement

- The "Summary Exit": Placing @END@ in the user prompt of the final visible turn.
    
- The "Logic Gate Exit": Placing @END@ in a hidden symbolic turn ("show": false) following a specific diagnostic condition (e.g., a user failing a safety check).
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 The Termination Lifecycle

1. Detection & Hydration: The engine detects the @END@ token during the prompt pre-processing phase.
    
2. Instruction Truncation: The engine marks the current turn as the terminal turn. Any JUMP or REPEAT commands that might follow the @END@ token in the same string are invalidated.
    
3. Pipeline Flush: The engine completes the current turn's output (if it is a visible LLM turn) and then "locks" the turn pointer.
    
4. Finalization: The session state is committed to the database, and the user's interface transitions to the "Session Complete" view, disabling further input.
    

### 4.2 Pattern: The Emergency Shutdown (Guardrail)

END is frequently used in conjunction with EVAL and MAP to create safety guardrails that terminate a session if a user violates specific constraints.

{  
  "user": "/ Check for violation; if true, Terminate, else Jump to next task.\n@MAP(\"@EVAL(\"@SafetyFlag@ == 'RED'\")@\", \"true|false\", \"@END@|@TN(1)@\", \"@TN(1)@\")@",  
  "show": false  
}  
  

### 4.3 Pattern: The Automated Timeout

In high-fidelity assessments, an EVAL turn can calculate total elapsed time. If the time exceeds a threshold, the agent delivers a "Time's Up" message and executes @END@.

{  
  "user": "/ Final summary for timeout.\nYour time has expired. Your progress has been saved.\n@END@",  
  "show": true  
}  
  

## 5. Security, State Integrity, and Failure Modes

### 5.1 Automatic Termination (The 1,000 Jump Guard)

To protect platform stability, the CAFA engine maintains a "Safety Watcher." If an agent executes more than 1,000 turn-jumps in a single session—indicating an infinite loop or logic deadlock—the system executes an Automatic Internal END. This prevents resource exhaustion and provides a fail-safe against malformed agent logic.

### 5.2 Persistence Persistence

A common misconception is that END deletes session data. In reality, END simply stops the execution of the agent. All Agent Parameters (AP) and System Parameters (SP) remain preserved in the platform's log and can be retrieved for subsequent auditing or used in future sessions via the LOAD or IMPORT commands.

### 5.3 Post-Termination Interaction

Once a session has been terminated by @END@, the turn pointer cannot be "revived" within that same session instance. Any attempt to interact with the closed agent will result in a "Session Terminal" message, necessitating the instantiation of a new session.

## 6. Reference

- Choi, J. (2025). Logic & Flow Control: END Command. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    
---
# INDEX Command: Retrieving Knowledge from Tabular Ontology Models

## 1. Metadata & Retrieval Keys

- Category: State Management / Knowledge Retrieval / Symbolic Orchestration
    
- Summary: A high-precision search command that identifies the numerical position (rank) of a specific value within a pipe-separated string. It functions as the primary "Foreign Key" connector for the Ontology Model-centered Generation (OMG) framework, allowing an agent to synchronize related data across multiple parallel lists and anchor generative outputs in deterministic symbolic evidence.
    
- RAG Keywords: INDEX, Lookup, TabularOntology, OMG, ParallelLists, SynchronousRetrieval, DataMapping, 1-basedIndex, SearchFunction, KnowledgeEngineering, StateSynchronization, EvidenceRetrieval, OntologicalIntegrity, Cross-ListMapping, DeterministicSearch, StructuralPointers, RowIdentification, AttributeHallucination, TruthAnchor, RelationalSymbolism, StatePersistence, LogicBranching, AtomicDataRetrieval, RowPointer, EpistemologicalConsistency.
    
- Related Commands: SET, MAP, EVAL, TN(), RADIO, TEXT, D(), SELECT, REPEAT, JUMP, IMPORT, EXPORT, JSONVALS.
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Resolving Knowledge Fragmentation: The OMG Framework

In complex agent design, knowledge is often fragmented across different attributes (e.g., a product's name, its price, its category, and its description). While generative models can "guess" these associations based on their training data, they are fundamentally prone to Attribute Hallucination. This occurs when an AI correctly identifies a specific entity (e.g., "Pro Watch") but provides the metadata of a different entity (e.g., the price of "Smart Boots") because the stochastic nature of token prediction favors high-frequency patterns over strict relational accuracy.

The INDEX command solves this by enabling the Ontology Model-centered Generation (OMG) framework. In OMG, knowledge is structured into Parallel Lists. Each list represents a "column" in a virtual database table. The power of this model lies in its Synchronicity: the data for a specific record always resides at the same index across all parallel lists.

INDEX allows the agent to find the "Row Number" based on one known value (the discovery phase). This row number then acts as a Truth Anchor, unlocking every other attribute associated with that record with 100% deterministic accuracy. By retrieving data this way, the agent shifts from "predicting facts" to "retrieving evidence," ensuring absolute consistency between a user's selection and the agent's response.

### 2.2 Theoretical Grounding: The Tabular Ontology Model

While complex data structures like nested JSON, trees, or Directed Acyclic Graphs (DAGs) exist, the Tabular Ontology Model is intentionally optimized for the CAFA symbolic layer. Its simplicity provides several architectural advantages:

- Human-Auditability and Scalability: Subject matter experts (SMEs) can manage vast amounts of knowledge in standard spreadsheets. These spreadsheets are easily converted to pipe-separated strings, making the "Agent Knowledge Base" easy to validate and update without touching the agent's core code.
    
- Symbolic Efficiency and Latency Reduction: The CAFA engine can scan and retrieve data from flat, pipe-separated lists with near-zero latency. Unlike vector searches or complex RAG retrievals, the INDEX lookup provides zero probabilistic drift—the result is either exactly correct or it returns $0$.
    
- Between-Turn Collective AI Logic: One "Micro-Agent" (turn) can identify the index (Discovery), and a subsequent "Micro-Agent" can use that index to generate a tailored response (Synthesis). This preserves context across the session lifecycle, ensuring the conversation remains anchored to a single, verifiable "Source of Truth."
    

## 3. Formal Syntax & Parameter Schema (The "What")

### 3.1 Syntax Structure

The command takes two arguments: the list to be searched and the specific value to find.

@INDEX("list", "value")@

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Technical Description|
|"list"|String|Required|The pipe-separated string to be searched. This is typically an Agent Parameter (AP) like @PRODUCT_NAMES@ or a dynamically built list.|
|"value"|String|Required|The specific string to locate. This can be a hardcoded string, a user input (@TU@), or a result from a previous turn (@TR@).|

### 3.2 Return/Output Value Mechanics

- The 1-based Success Index: Returns a single Integer representing the 1-based position of the value. For example, if the value is the third item in the list, the command returns 3.
    
- The Failure Sentinel (0): If the value is not found, the command returns 0. This is a critical design feature allowing for easy conditional checks via the EVAL command (e.g., @EVAL("@INDEX(...)@ > 0")@) to determine if a user's input exists within the knowledge base before proceeding.
    
- Deterministic Multi-match: If the value appears multiple times, the command returns the index of the first occurrence. To ensure data integrity, ontology models should ideally use unique keys (like IDs) for indexing.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 The Hydration & Scan Lifecycle

The processing of an INDEX command follows a strict four-stage lifecycle within the CAFA engine:

1. Macro Expansion and Parameter Hydration: The engine first resolves any parameters nested within the arguments. For instance, @INDEX("@LIST@", "@RADIO(choice)@")@ is expanded to the literal list string and the specific user choice.
    
2. Linear Segmented Scan: The engine performs a linear search from left to right. It splits the "list" string by the pipe character (|) and checks each segment.
    
3. Atomic Exact Match: The search is case-sensitive and requires an exact match. It does not perform partial or fuzzy matching, ensuring that retrieval is based on explicit evidence rather than proximity.
    
4. Symbolic Substitution: The final integer replaces the @INDEX(...)@ token in the prompt string. This happens before the prompt is sent to the LLM or processed by the next symbolic command.
    

### 4.2 The "Row Pointer" Pattern (Advanced State Management)

The most sophisticated application of INDEX is storing the result in a temporary parameter to act as a Row Pointer. This allows the agent to "remember" the specific record it is discussing throughout a multi-turn interaction.

- Pattern Implementation:
    

1. Turn 1 (Identification): Locate the record and store its index.  
    @SET("ROW_ID", "@INDEX("@IDS@", "@RADIO(id_choice)@")@")@
    
2. Turn 2 (Detailed Inquiry): Use the stored ROW_ID to pull additional metadata.  
    Concept: @CONCEPTS[@@ROW_ID@@]@
    
3. Turn 3 (Evaluation): Use the ROW_ID to verify a user's answer against the "Ground Truth."  
    @EVAL("'@USER_ANS@' == '@KEYS[@@ROW_ID@@]@'")@
    

## 5. Implementation Patterns (Examples)

### Pattern 1: Simple Student Lookup (Synchronous Data Retrieval)

Linking a Student ID selection to multiple disparate attributes stored in parallel lists.

{  
    "options": {  
        "name": "Student_Lookup_System_v2",  
        "params": {  
            "STUDENT_ID": { "org": "S101|S102|S103", "cond": "SELF" },  
            "STUDENT_NAME": { "org": "Alice|Bob|Charlie", "cond": "SELF" },  
            "STUDENT_YEAR": { "org": "Freshman|Sophomore|Junior", "cond": "SELF" }  
        }  
    },  
    "prompts": [  
        {  
            "user": "/ T1: Initialize state and present ID options to user.\n\n@RADIO(\"id_choice\", \"Select Student ID:\", \"@STUDENT_ID@\")@",  
            "show": true  
        },  
        {  
            "user": "/ T2: Find the unique Row Index for the selection and store it.\n@SET(\"S_INDEX\", \"@INDEX(\"@STUDENT_ID@\", \"@RADIO(id_choice)@\")@\")@",  
            "show": false  
        },  
        {  
            "user": "/ T3: Display Synchronized Record retrieved from parallel indices.\n**Record Details:**\n- ID: @STUDENT_ID[@S_INDEX@]@\n- Name: @STUDENT_NAME[@S_INDEX@]@\n- Year: @STUDENT_YEAR[@S_INDEX@]@",  
            "show": true  
        }  
    ]  
}  
  

### Pattern 2: Dynamic Quiz Generator (Cross-Ontology Intersection)

Intersecting two different ontologies (format and content) using two separate index pointers.

{  
    "options": {  
        "name": "Dynamic_Item_Generator",  
        "params": {  
            "TOPIC": { "org": "Physics|Biology", "cond": "SELF" },  
            "KEY_FACT": { "org": "Force = Mass * Acceleration|DNA is a double helix", "cond": "SELF" },  
            "FORMAT": { "org": "True/False|Multiple Choice", "cond": "SELF" }  
        }  
    },  
    "prompts": [  
        {  
            "user": "/ T1: User selects format and topic.\n\n@RADIO(\"f_sel\", \"Format:\", \"@FORMAT@\")@\n@RADIO(\"t_sel\", \"Topic:\", \"@TOPIC@\")@",  
            "show": true  
        },  
        {  
            "user": "/ T2: Resolve both indices simultaneously.\n@SET(\"F_PTR\", \"@INDEX(\"@FORMAT@\", \"@RADIO(f_sel)@\")@\")@\n@SET(\"T_PTR\", \"@INDEX(\"@TOPIC@\", \"@RADIO(t_sel)@\")@\")@",  
            "show": false  
        },  
        {  
            "system": "Design a @FORMAT[@F_PTR@]@ question. You must base it on this fact: @KEY_FACT[@T_PTR@]@.",  
            "user": "Generate the item now.",  
            "model": "gpt-4.1-nano",  
            "show": true  
        }  
    ]  
}  
  

## 6. Security and Data Integrity Guardrails

- Delimiter Integrity: If the pipe character (|) is used within the data itself (e.g., in a description), the index scan will fragment that item, breaking the synchronicity of the parallel lists. Developers should use an alternative character or sanitize data before inclusion.
    
- Index Out of Bounds: When using a stored index parameter (e.g., @LIST[@PTR@]@), if @PTR@ is $0$ (search failed), the retrieval will fail or return an empty string. It is best practice to wrap retrieval in an @EVAL@ check.
    
- Type Coercion: The INDEX command treats all segments as strings. If you are searching for a number, ensure it is formatted consistently (e.g., "1" vs "1.0") across the list and the search value.
    

## 7. Reference

- Choi, J. (2025). INDEX Command: Retrieving Knowledge from Tabular Ontology Models. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# COMPARE Command: Element-wise List Comparison

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / Data Validation
    
- Summary: Performs a rigorous pairwise, element-by-element comparison between two parallel lists based on a specified relational operator. It generates a "Truth Map"—a synchronized boolean list—that forensically identifies exactly where two datasets align, diverge, or meet specific numerical/lexical thresholds.
    
- RAG Keywords: COMPARE, list-comparison, pairwise-comparison, element-wise, truth-map, boolean-list, logical-mapping, parallel-processing, list-validation, equality-check, inequality-check, symbolic-comparison, data-alignment, forensic-matching, diagnostic-patterning, state-synchronization, bitwise-simulation, partial-correctness, error-identification, structural-fidelity.
    
- Related Commands: EQUAL (Holistic comparison), FILTER (Conditional selection), MAP (Logic routing), INDEX (Position retrieval), EVAL (Mathematical processing).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 The "Truth Map" Problem and Granular Diagnostics

In advanced agent modeling, a simple binary "True/False" verdict for an entire dataset is often insufficient for sophisticated decision-making. Architects frequently encounter the "Granularity Gap," where they need to know not just if a user was wrong, but exactly which elements of their input were problematic.

The COMPARE command solves this by creating a Truth Map. This boolean list serves as a high-fidelity forensic record of alignment between two lists. For example, in an educational agent, comparing a student's ten-step procedure against a master template allows the system to identify exactly at which step a misconception occurred, enabling targeted rather than generic remediation.

### 2.2 Symbolic Parallelism and State Stability

The command enforces Symbolic Parallelism, a design principle that allows the agent to process large arrays of data within a single symbolic turn. By iterating through lists and applying deterministic operators (==, !=, >, etc.) at the system level, COMPARE achieves two critical goals:

1. Computational Efficiency: It handles mass-validation without the overhead of multiple recursive turns or expensive generative interpretation.
    
2. State Machine Stability: By producing a structured boolean list, it provides a stable, predictable input for downstream commands like FILTER or EQUAL (using the "Boolean" option), preventing "Logic Drift" in complex workflows.
    

### 2.3 Bridge to Generative Interpretation

The Truth Map produced by COMPARE acts as a structured bridge between symbolic logic and generative AI. By feeding the resulting true|false|true map back into an LLM's context, the architect can prompt the model with high-fidelity precision: "The user was correct on steps 1 and 3 but failed step 2. Explain why step 2 is incorrect based on the ground truth." This eliminates the need for the LLM to perform the comparison itself, significantly reducing hallucination rates.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax (Golden Template)

@COMPARE("list1", "list2", "condition")@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|list1|String|Required|The primary pipe-separated list of elements (the "Test List").|
|list2|String|Required|The secondary pipe-separated list (the "Reference List"). Length must match list1.|
|condition|String|Required|The relational operator used for each pair: == (Equal), != (Not Equal), < (Less than), > (Greater than), <= (Less/Equal), >= (Greater/Equal).|

### Return/Output Value

- Output Format: Returns a pipe-separated string of boolean values (true|false).
    
- Length Consistency: The returned list is guaranteed to be equal in length to the input lists, ensuring positional symmetry.
    
- Lexical vs. Numerical: The engine intelligently handles both string-based lexical comparisons and numerical magnitude checks based on the content of the elements.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow: Pairwise Deserialization

1. Serialization Check: The system splits the two input strings into internal arrays based on the pipe (|) delimiter. If lengths are mismatched, the shorter list is typically padded with null values (depending on specific engine versioning).
    
2. Pairwise Iteration: The engine enters a deterministic loop, evaluating the condition for elements at index $i$ of both arrays.
    
3. Truth Map Construction: The result of each evaluation is serialized into a new pipe-separated string of true and false tokens.
    
4. Hydration: The final string is injected into the Turn Result (@TR@), immediately becoming available for the next turn's logic.
    

### 4.2 Implementation Pattern: The Forensic Validation Gate

Architects use COMPARE to perform complex pattern matching before triggering major state changes.

Example 1: Threshold-Based Filtering

- Context: A list of scores @Scores@ (e.g., 85|40|92) and a passing threshold @Pass@ (e.g., 70|70|70).
    
- Command: @COMPARE("@Scores@", "@Pass@", ">=")@
    
- Result: true|false|true
    
- Downstream: Use this result in a FILTER command to extract only the names of students who passed.
    

Example 2: The Boolean Validation Gate

This is the most common pattern for multi-select or multi-step validation:

- Turn N (COMPARE): @COMPARE("@USER_ANSWERS@", "@CORRECT_ANSWERS@", "==")@
    
- Turn N+1 (EQUAL): @EQUAL("@TR@TN(-1)@@", "true|true|true", "Boolean")@
    
- Implication: This pattern ensures a "Perfect Match" requirement. If even one element in the Truth Map is false, the EQUAL command returns False, allowing the agent to route the user to a specific "Partial Correction" loop.
    

## 5. Reference

- Choi, J. (2025). COMPARE Command: Element-wise List Comparison. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
   
---
# EQUAL Command: Holistic List Equality and Pattern Matching

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / Data Validation
    
- Summary: Provides a definitive True/False judgment on the equality of two lists. It supports three distinct modes of evaluation: strict order-sensitive matching, order-insensitive set comparison (critical for CHECKBOX grading), and element-by-element boolean pattern verification.
    
- RAG Keywords: EQUAL, list-equality, set-comparison, order-insensitive, boolean-matching, grading-logic, validation-gate, "NO" option, "Boolean" option, CHECKBOX-grading, response-validation.
    
- Related Commands: COMPARE (Pairwise mapping), FILTER (Dynamic key creation), MAP (Logic routing), CHECKBOX (Input source).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Holistic Judgment vs. Mapping

While the COMPARE command provides a "Truth Map" showing where things match, the EQUAL command provides the Holistic Judgment required to determine if an interaction as a whole meets the success criteria. It acts as the final "Binary Gate" in the agent's logic flow, allowing architects to collapse complex multi-select inputs into a single boolean state for branching using MAP or JUMP.

### 2.2 Set Theory and User Agency

In human-in-the-loop interactions—specifically with CHECKBOX controls—the order of selection is typically irrelevant to the correctness of the response. The EQUAL command's "NO" option implements Order-Insensitive Set Comparison. This respects the user's agency by ignoring the sequence of clicks and focusing strictly on whether the set of unique symbols provided matches the required ontology.

### 2.3 Execution Mode

Symbolic Turn. A deterministic system operation that ensures 100% fidelity. It is a system-level function that provides a high-fidelity "Binary Verdict" on user state without generative drift.

## 3. Formal Syntax & Parameter Schema (The "What")

### 3.1 Command Syntax (Golden Template)

@EQUAL("list1", "list2", "option")@  
  

### 3.2 Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"list1"|String|Required|The first pipe-separated list (e.g., user input via @CHECKBOX("Q1")@).|
|"list2"|String|Required|The second pipe-separated list (e.g., the static or dynamic "Answer Key").|
|"option"|String|Optional|Omitted: Strict order-sensitive comparison.<br><br>  <br><br>"NO": Order-insensitive set comparison.<br><br>  <br><br>"Boolean": Element-wise boolean list match.|

### 3.3 Syntax Examples

- Strict: @EQUAL("A|B", "B|A")@ returns False.
    
- Set Mode: @EQUAL("A|B", "B|A", "NO")@ returns True.
    
- Boolean Mode: @EQUAL("true|false", "true|false", "Boolean")@ returns True.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Comparison Algorithms

The engine processes the EQUAL command through three distinct logic paths:

1. Strict Mode: Direct string-to-string comparison after list serialization.
    
2. Set Mode ("NO"): Both lists are de-duplicated and sorted internally. The engine then checks if the resulting sets are identical. This makes it impervious to user selection order or accidental double-clicks.
    
3. Boolean Mode ("Boolean"): Specifically designed to consume the output of a COMPARE command. It validates if the "Truth Map" matches a predefined pattern of correctness.
    

### 4.2 Implementation Pattern: Dynamic Answer Key Validation

A robust pattern involves nesting FILTER within EQUAL to grade randomized content:

- Logic Turn: @EQUAL("@CHECKBOX("Q1")@", "@FILTER("@MASTER_LIST@", "@PARITY_LIST@|==@TARGET_VALUE@")@", "NO")@
    
- Workflow: The FILTER constructs the valid answer set for the current session in real-time, and EQUAL provides the definitive grade.
    

## 5. Advanced Scenario: Multi-Step Boolean Validation

Architects use the "Boolean" option to verify interaction patterns rather than just text matches.

1. Forensic Check (Turn N): @SET("TruthMap", "@COMPARE("@CORRECT_ATTR@", "@USER_ATTR@", "==")@")@
    
2. Pattern Match (Turn N+1): @EQUAL("@TruthMap@", "true|true|true|true", "Boolean")@
    

- Result: This ensures that every specific attribute in a multi-step verification process was correctly identified, preventing "Partial Correctness" from bypassing the logic gate.
    

## 6. Reference

- Choi, J. (2025). EQUAL Command: Holistic List Equality and Pattern Matching. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# FILTER Command: Conditional List Creation

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / Content Operations
    
- Summary: Dynamically constructs a new list by extracting elements from a source list that satisfy specific criteria. It supports two primary operational modes: direct value-based filtering (Method 1) and parallel attribute-based filtering (Method 2), enabling high-fidelity data subsetting and dynamic grounding.
    
- RAG Keywords: FILTER, list-filtering, conditional-selection, dynamic-list-creation, answer-key-generation, Method-1, Method-2, parallel-attribute-filtering, data-subsetting, symbolic-filtering, dynamic-grounding, linked-list-processing, relational-mapping, criteria-selection, predicate-rule.
    
- Related Commands: GSTABLE (Data source), EQUAL (Validation), COMPARE (Mapping), INDEX (Position retrieval), MAP (Logic routing).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Dynamic Knowledge Grounding

Static, hard-coded datasets are insufficient for adaptive AI agents. The FILTER command facilitates Dynamic Answer Key Generation, where the "correct" set of items is determined at runtime based on randomized variables or user-specific context. This allows architects to build "Living Assessments" where the grading logic evolves synchronously with the shuffled content.

### 2.2 Relational Logic Mapping (Method 2)

The architectural power of FILTER lies in its ability to perform Parallel Selection. This mirrors relational database queries (e.g., SELECT item FROM inventory WHERE status = 'In Stock'). By filtering one list based on the values of a second, parallel list, architects can implement complex, rule-based reasoning within the agent’s symbolic memory without requiring external database overhead.

### 2.3 Execution Mode

Symbolic Turn (⚙️). A deterministic system operation that ensures 100% fidelity in data transformation. It provides the clean, structured output required to "hydrate" subsequent LLM context or satisfy strict logic gates.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax (Golden Templates)

Method 1: Simple Value Filter

@FILTER("list", "condition")@  
  

Method 2: Parallel List Filter

@FILTER("list", "condition_list")@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"list"|String|Required|The source pipe-separated list containing the elements to potentially include in the output.|
|"condition"|String|Required (M1)|A string defining the filter rule: an operator followed directly by a value (e.g., ">80", "!==Apple").|
|"condition_list"|String|Required (M2)|A parallel list matching the length of list, plus one extra element at the end that defines the rule (e.g., `"Odd|

### Supported Operators

=, >, <, >=, <=, <>, !=, includes.

### Return/Output Value

- Output Format: Returns a new pipe-separated string containing only the elements from the source list that satisfied the criteria.
    
- Empty State: If no elements satisfy the filter, an empty string ("") is returned.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow: Method 2 (Parallel List)

1. Rule Extraction: The engine parses condition_list and isolates the last element as the Predicate Rule (e.g., ==Odd).
    
2. List Alignment: The engine validates that the remaining elements in condition_list correspond 1:1 with the source list.
    
3. Pairwise Iteration: The engine iterates through the source list indices. For each index $i$, it evaluates the Predicate Rule against the element at index $i$ in the condition_list.
    
4. Selective Serialization: If the rule evaluates to true, the corresponding element from the source list is appended to the new output string.
    
5. Completion: The serialized result is committed to the Turn Result (@TR@).
    

### 4.2 Implementation Pattern: The Dynamic Quiz Generator

Architects use FILTER to create "Moving Targets" for users:

- Step 1: Shuffle a master list of numbers (NUM) and a parallel list of parities (TYPE).
    
- Step 2: Prompt the user to "Select all odd numbers."
    
- Step 3: Generate the ground truth at runtime using:  
    @FILTER("@NUM@", "@TYPE@|==odd")@
    
- Step 4: Pass this dynamic key into EQUAL to grade the user's CHECKBOX input.
    

## 5. Reference

- Choi, J. (2025). FILTER Command: Conditional List Creation. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    







# DISTRACTOR Command: Engineering Effective Alternatives

## 1. Metadata & Retrieval Keys

- Category: Assessment Engineering / Data Transformation / Randomization
    
- Summary: A high-fidelity symbolic engine for the automated selection, exclusion, supplementation, and shuffling of multiple-choice options. It ensures that interaction spaces are unique, plausible, and syntactically valid by managing the mechanical assembly of distractors and correct answers. By decoupling pedagogical intent from interaction logistics, it serves as a cornerstone for valid and reliable diagnostic assessment within the Evidence-Centered Design (ECD) framework.
    
- RAG Keywords: DISTRACTOR, D, AssessmentEngineering, AE, AutomaticItemGeneration, AIG, DistractorSelection, OptionShuffling.
    
- Related Commands: RADIO, CHECKBOX, SELECT, INDEX, MAP, EVAL, SHUFFLE, SORT, SET, TN(), D(), SELECT, REPEAT.
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Resolving the Assembly Bottleneck in Assessment Engineering

In Assessment Engineering (AE), the diagnostic power of an item rests significantly more on the quality of its distractors than on the correct answer itself. Plausible distractors—incorrect options that reflect common misconceptions—differentiate between genuine mastery, partial understanding, and successful guessing. However, the manual assembly of unique, randomized sets of options for every student interaction presents a massive "Assembly Bottleneck," especially in Automatic Item Generation (AIG) environments where hundreds of variants must be produced instantaneously to prevent item exposure and cheating.

The DISTRACTOR or D command resolves this bottleneck by automating the mechanical pipeline of option assembly. It allows the agent architect to define broad "Pools of Intent" (the Base and Additional Distractor Lists) while the engine handles the surgical exclusion of correct answers and the randomized selection of alternatives. This structural decoupling allows subject matter experts to focus on Pedagogical Design (crafting the source material) while the symbolic engine manages the Interaction Logistics (shuffling and formatting).

### 2.2 Symbolic De-duplication and Mathematical Integrity

A critical failure point in digital assessments is the "Duplicate Option" error, where two choices evaluate to the same value (e.g., "2+2" and "4"). In generative or mathematical workflows, this happens frequently as different logical paths converge on the same result. If both appear as options, the item's discriminatory power is invalidated, and the user is left in a state of cognitive confusion.

The DISTRACTOR or D command incorporates internal Symbolic De-duplication. During the assembly phase, it resolves every item in the pool and ensures that only unique, discrete choices reach the final interaction space. This "Uniqueness Enforcement" is essential for maintaining the mathematical and logical integrity of the assessment, ensuring that every option represents a distinct, mutually exclusive cognitive choice for the test-taker.

### 2.3 Execution Mode: Deterministic Assembly over Probabilistic Shuffling

While LLMs can be prompted to "generate four options," they are prone to "Two-Answer Hallucination," where the probabilistic model inadvertently includes the correct answer twice or fails to include it at all. D is a Deterministic System Directive. While it introduces controlled randomness (shuffling), the rules governing exclusion and supplementation are executed by the CAFA engine's symbolic layer. This guarantees $100\%$ accuracy in the assembly: the "Correct Answer" provided in the ANL argument is strictly removed from the distractor set, and the final list is guaranteed to reach the requested LEN provided sufficient source material is available.

### 2.4 Plausibility Engineering and Misconception Modeling

Effective distractors are "misconception anchors." By using the BDL (Base Distractor List) to store known errors (e.g., "adding instead of multiplying") and the ADL (Additional Distractor List) to store "fillers," the D command allows for Plausibility Engineering. The engine prioritizes the most pedagogically valuable errors first, ensuring that every multiple-choice item serves as a diagnostic probe rather than a simple recognition task.

## 3. Formal Syntax & Parameter Schema (The "What")

### 3.1 Syntax Structure

The command supports both the formal name and the shorter, highly efficient alias:

@DISTRACTOR("BDL", "ANL", "ADL", "LEN", "ORD")@

@D("BDL", "ANL", "ADL", "LEN", "ORD")@

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Technical Description|
|"BDL"|String|Required|Base Distractor List: The primary pool of options (pipe-separated). Often includes the answer if pulling from a fixed ontology.|
|"ANL"|String|Required|Answer List: Options to be explicitly excluded from BDL. Use "" to include the answer in the assembly.|
|"ADL"|String|Optional|Additional Distractor List: Fallback/reserve options used only if the BDL is exhausted.|
|"LEN"|String|Optional|Length: The target number of total options to return. Defaults to "4".|
|"ORD"|String|Optional|Order: ASCE (Ascending), DESC (Descending), SELF (No change), or SHUFFLE (Default).|

### 3.2 The Quoting Mandate and Type Coercion

Strict CAFA syntax applies: all five arguments, including the numerical LEN and the lists, must be enclosed in double quotes ($"$). During execution, the engine performs implicit type coercion, treating the LEN string as an integer and the list strings as arrays. If a parameter is passed (e.g., "@COUNT@"), it is hydrated before coercion.

## 4. Execution Mechanics & Process Flow (The "How")

### 4.1 The 7-Step Assembly Lifecycle

When the engine hydrates an D command, it follows a strict, non-generative sequence:

1. Exclusion (Sifting): The engine splits the BDL string and removes any item that is an exact match for an item in the ANL string. This ensures the "Correct Answer" is not a distractor.
    
2. Uniqueness Check: The remaining pool is scanned, and duplicate strings are collapsed into a single instance to prevent "Distractor Redundancy."
    
3. Supplementation Audit: The engine calculates the current count of the pool and compares it against LEN.
    
4. Supplementation (If needed): If the pool is too small, the engine randomly draws unique items from the ADL string until the list reaches the target LEN.
    
5. Pruning (Selection): If, after exclusion and supplementation, the pool is larger than LEN, the engine performs a randomized selection to reduce the list to exactly LEN items.
    
6. Ordering (The Finish): The engine applies the ORD logic. If SHUFFLE is active, it uses a high-entropy randomization algorithm to reorder the items.
    
7. Crystallization: The final items are joined into a pipe-separated string (|) and substituted into the parent command (e.g., @RADIO()@).
    

### 4.2 Pattern: The "Full Choice" Assembly (Standard Pattern)

This is the recommended pattern for generating the complete interaction space (Answer + Distractors) in a single turn.

@D("@CorrectAns@", "", "@DistractorPool@", "4")@

- Why ANL is empty (""): By providing an empty answer list, you ensure the item in BDL (the correct answer) is never excluded.
    
- Logic: The engine starts with 1 item (@CorrectAns@) and identifies it needs 3 more to reach LEN=4. It draws 3 from the pool, then shuffles them all together.
    

## 5. Implementation Patterns

### Pattern 1: Dynamic Flashcard Engine (AE-Driven)

This pattern uses SHUFFLE and LINK to maintain the integrity of key-value pairs while using D to generate plausible but incorrect definitions for the current term.

{  
    "options": {  
        "name": "Dynamic_AE_Flashcard_v1",  
        "title": "Interactive Terminology Trainer",  
        "brief": "Demonstrates automated distractor assembly with LINK logic.",  
        "description": "Uses SHUFFLE/LINK to maintain term-definition pairs and the @D() command to generate unique, plausible distractors from the remaining pool.",  
        "greeting": "Welcome to the CAFA Flashcard Trainer. Let's test your knowledge.",  
        "params": {  
            "TERMS": { "org": "Variable|Function|Loop|Array|Object", "cond": "SHUFFLE" },  
            "DEFS": { "org": "A named storage.|A code block.|An iterator.|A collection.|A key-value map.", "cond": "LINK(TERMS)" }  
        }  
    },  
    "prompts": [  
        {  
            "user": "/ T1: Presentation of the randomized term.\n\nTerm: **@TERMS[1]@**\n@RADIO(\"user_choice\", \"Select the correct definition:\", \"@D(\"@DEFS[1]@\", \"\", \"@DEFS[2:5]@\", \"4\")@\")@",  
            "show": true  
        },  
        {  
            "user": "/ T2: Grading and Feedback.\n@SET(\"RESULT\", \"@MAP(\"@RADIO(user_choice)@\", \"@DEFS[1]@\", \"Correct|Incorrect\")@\")@",  
            "show": false  
        },  
        {  
            "user": "/ T3: Results Display.\n**Result:** @RESULT@\n\n- Correct: @DEFS[1]@\n- Your Selection: @RADIO(user_choice)@",  
            "show": true  
        }  
    ]  
}  
  

### Pattern 2: Mathematical Distractor De-duplication

Using @D() to ensure a generated math problem remains valid even if the underlying logic produces redundant values across different formats (e.g., decimals vs integers).

{  
    "options": {  
        "name": "Math_DeDupe_Demo",  
        "title": "Robust Math Item Generator",  
        "brief": "Ensures unique numeric options.",  
        "description": "Demonstrates how @D() collapses redundant numeric strings (4, 4.0, 4) into a single valid option.",  
        "greeting": "Prepare for a math challenge.",  
        "params": {}  
    },  
    "prompts": [  
        {  
            "user": "/ T1: Ensure unique numeric options even if LLM or Logic is redundant.\nSolve: 2 + 2\n@RADIO(\"ans\", \"Choose the answer:\", \"@D(\"4\", \"\", \"4|4.0|4|3|5\", \"4\", \"ASC\")@\")@",  
            "show": true  
        }  
    ]  
}  
  

- Result: The engine detects that 4, 4.0, and 4 represent the same option. It collapses them, then draws 3 and 5 to fill the list. The ASC order ensures the numbers are presented in logical sequence.
    

### Pattern 3: Tiered Difficulty Supplementation

In this advanced pattern, BDL contains "Easy" distractors and ADL contains "Hard" distractors. By changing the LEN or swapping lists, the agent can adapt the difficulty of the options based on the student's current proficiency level.

{  
    "user": "/ Try to fill with high-probability common errors (misconceptions) first.\n@RADIO(\"ans\", \"Question...\", \"@D(\"@CommonErrors@\", \"@Answer@\", \"@RandomPool@\", \"4\")@\")@",  
    "show": true  
}  
  

## 6. Security, State Integrity, and Failure Modes

### 6.1 Delimiter Sanitization and Fragment Errors

The CAFA engine uses the pipe (|) as a hard delimiter. If source data within a parameter contains a pipe (e.g., "Choice A | Sub-choice"), the D command's exclusion and selection logic will fragment that string into two separate items.

- Mandate: All data intended for distractor pools must be sanitized. If pipes are required in the final output, use a placeholder (like [PIPE]) and swap it in a subsequent turn, or ensure your BDL strings are properly escaped.
    

### 6.2 The "Insufficient Pool" Failure and Graceful Degradation

If the combined pool of BDL and ADL (after the exclusion of ANL) contains fewer items than the requested LEN, the command returns the entire available pool.

- Implication: The command will not generate synthetic "AI hallucinations" to fill the gap. This is a safety feature to prevent invalid distractor creation. If D returns only 2 items when 4 were requested, the UI (e.g., @RADIO()@) will still function but will only display the 2 available options. This is known as "Graceful Degradation" of the interaction space.
    

### 6.3 Atomicity and State Persistence

The result of an D command is generated at the turn-hydration boundary. If the result is captured via a SET command, it is subject to the Next-Turn Rule. The shuffled list is only available for retrieval and indexing starting from Turn $N+1$. Using D directly inside a display command (like Pattern 1) is the most efficient way to ensure the interaction space is hydrated and rendered simultaneously.

## 7. Reference

- Choi, J. (2025). DISTRACTOR Command: Engineering Effective Alternatives. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# SAVE Command: Persist Data to System Log

## 1. Metadata & Retrieval Keys

- Category: State Management / Content Operations
    
- Summary: Acts as the foundational framework for an agent's memory by serializing data into either temporary task-based slots (Short-Term) or a persistent "LOG" identifier (Long-Term). It serves as the bridge between ephemeral generative turns and the permanent stateful architecture of the CAFA ecosystem.
    
- RAG Keywords: SAVE, persistence, memory, short-term memory, long-term memory, DID, Data ID, GUID, Agent Log, LOG, append, overwrite, serialization, working memory, stateful collaboration, multi-stage workflow, artifact vault.
    
- Related Commands: LOAD (Retrieval), SET (In-memory update), EXPORT (Bulk archival), IMPORT (State restoration).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Giving AI Agents Memory

To evolve from simple command-responders into sophisticated digital collaborators, agents require a stateful layer. Standard Large Language Models (LLMs) are natively stateless; they do not remember previous interactions unless explicitly provided in the context window. Content Operations provide the framework for two distinct types of memory:

- Short-Term Memory (Agent Data): Utilizing anonymous saves to receive a temporary DID. This functions like human "working memory," essential for passing details within a single complex task or passing a specific data "artifact" to another agent for immediate collaboration. It is high-velocity and task-specific.
    
- Long-Term Memory (Agent Log): Utilizing the reserved "LOG" identifier for persistent storage. This acts as a "diary," allowing agents to recall past interactions, learn user preferences over time, and achieve true self-adaptation. It represents the accumulated wisdom and history of the agent-user relationship.
    

### 2.2 Theoretical Grounding

Based on the Memory Cycle of Intelligence, this command transforms stateless generative turns into stateful, adaptive knowledge structures. By decoupling the generation of data from its persistence, CAFA allows for forensic auditing and longitudinal growth modeling. It adheres to the Construct Validity of Records, ensuring that every saved datum is a verifiable piece of evidence in a larger cognitive argument.

### 2.3 Execution Mode

System Level Command. The agent must be saved on the CAFA platform before this command can execute. This requirement establishes a secure, defined association between the data payload and the specific agent instance, preventing "orphaned" data in the cloud ecosystem.

## 3. Formal Syntax & Parameter Schema (The "What")

### 3.1 Command Syntax

@SAVE("data"[, "ID"[, "append"]])@  
  

### 3.2 Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"data"|String|Required|The content to be stored. This can be the output of a turn (e.g., @TR1@), a parameter value (@MyVariable@), or raw string content.|
|"ID"|String|Optional|A specific identifier. Use "LOG" for the persistent stream or a custom string (e.g., "User_Profile") for targeted slots. If omitted, the system generates a unique DID.|
|"append"|String|Optional|A boolean ("true"/"false"). Controls whether to add to existing data or replace it. For "LOG", this defaults to "true". For custom IDs, it defaults to "false" (overwrite).|

### 3.3 Return/Output Value

- Anonymous Save: Returns a unique DID (Data ID) following the GUID (Globally Unique Identifier) structure. This 128-bit identifier ensures that data remains unique across all agents and users in the network.
    
- Targeted Save: Returns the provided ID string (e.g., if you save to "LOG", the command returns "LOG").
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Work Modes and Use Cases

1. Saving to a New Location (Anonymous Save):
    

- Syntax: @SAVE("This is a temporary report.")@
    
- Mechanics: The system captures the string, assigns it a DID (e.g., 2B99B2E4-FFE9-4616-8DD4-25BC178F40FF), and writes it to the temporary storage tier.
    
- Scenario: Ideal for generating a unique "Ticket ID" or a one-time data package that will be passed to a supervisor agent for review.
    

2. Overwriting Existing Data (Snapshotting):
    

- Syntax: @SAVE("Score: 95", "2B99B2E4-FFE9-4616-8DD4-25BC178F40FF")@
    
- Mechanics: The system locates the record in DID "2B99B2E4-FFE9-4616-8DD4-25BC178F40FF" and replaces its entire contents with the new string.
    
- Scenario: Used for maintaining the "2B99B2E4-FFE9-4616-8DD4-25BC178F40FF" of a game or a user profile where only the latest version matters.
    

3. Appending to Existing Data (Journaling):
    

- Syntax: @SAVE("Step 2 completed.", "2B99B2E4-FFE9-4616-8DD4-25BC178F40FF", "true")@
    
- Mechanics: The system retrieves the existing content at "2B99B2E4-FFE9-4616-8DD4-25BC178F40FF", adds a newline (or delimiter), and attaches the new payload.
    
- Scenario: Building a custom audit trail for a multi-stage manufacturing process or a tutoring session.
    

### 4.2 Special Case: The Agent Log (DID="LOG")

The "LOG" identifier is a high-priority reserved slot that creates a permanent, chronologically ordered stream attached to the agent's identity.

|   |   |   |
|---|---|---|
|Feature|Agent Data (Specific/Anonymous ID)|Agent Log (DID="LOG")|
|Storage Tier|Transitional; may be periodically erased.|Persistent; permanent part of agent metadata.|
|Default Logic|Overwrites unless append="true".|Appends entries by default.|
|Persistence|Session-bound or task-bound.|Cross-session; follows the agent identity.|
|Retrieval|Requires the specific ID/DID.|Accessible via standard LOAD("LOG").|

## 5. Implementation Patterns and Best Practices

### 5.1 Capturing and Passing DIDs

Because anonymous saves return a random DID, the agent must "catch" this value in a parameter to use it in subsequent turns or export it to other agents.

/ Turn N: Save an LLM-generated essay anonymously  
"user": "@SAVE("@TR@TN(-1)@@")@"  
  
/ Turn N+1: Use SET to store the resulting DID for the next agent  
"user": "@SET("Artifact_DID", "@TR@TN(-1)@@")@"  
  

### 5.2 The "Atomic Read-Modify-Write" Pattern

To avoid data corruption in multi-step workflows, follow the CAFA standard for updating records:

1. LOAD: Pull the existing data into a temporary AP (Agent Parameter).
    
2. MODIFY: Use SET, EVAL, or MAP to change the AP in memory.
    
3. SAVE: Commit the updated AP back to the original ID with append="false".
    

### 5.3 Security and Sanitization

Data saved via @SAVE()@ is often used as input for future turns. It is critical to ensure that saved data does not contain reserved CAFA characters (like @ or |) that could trigger unintended command execution during a LOAD operation. Always sanitize user-provided text before saving to the LOG or a DID.

## 6. Implications of Content Operations

Mastering SAVE transforms an agent from a "reactive tool" into a "proactive assistant."

- Inter-Agent Collaboration: By sharing a DID, Agent A can "hand off" a massive dataset to Agent B without passing the entire text in a prompt, saving tokens and maintaining precision.
    
- Longitudinal Personalization: By consistently saving user preferences to the LOG, an agent can greet a user by name and remember their previous learning progress weeks later.
    
- Forensic Transparency: The LOG provides a verifiable record of what the AI "thought" and "did" at every step, which is vital for ethical AI and compliance in regulated industries.
    

## 7. Reference

- Choi, J. (2025). SAVE Command: Persist Data to System Log. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# LOAD Command: Retrieve Data from Artifacts or Log

## 1. Metadata & Retrieval Keys

- Category: State Management / Content Operations
    
- Summary: Retrieves stored content from the CAFA persistent database using a unique Data ID (DID) or the reserved "LOG" identifier, acting as the primary mechanism for memory recall and inter-agent data hydration. It is the "Read" operation of the Content Operations framework, essential for transforming stateless turns into a continuous, stateful narrative.
    
- RAG Keywords: LOAD, retrieval, memory recall, DID, Data ID, Agent Log, LOG, fetch, state restoration, working memory, session history, GUID, artifact retrieval, read operation, data hydration, state recovery, multi-agent handoff, record retrieval, state persistence, cross-session memory, data pointers.
    
- Related Commands: SAVE (Storage), SET (Assignment), IMPORT (Bulk loading), EXPORT (Bulk archival).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 The Retrieval Problem in Stateless AI

The fundamental limitation of Foundation Models (LLMs) is their inherent statelessness. Every prompt sent to an LLM is, by default, an isolated "island" with no inherent memory of previous interactions outside the current token window. The LOAD command provides the "bridge" that allows an agent to reach back into its history, recover previous context, or access artifacts created by other agents. This mechanism effectively expands the agent's "cognitive horizon" beyond the limitations of a single session.

### 2.2 Functional Memory Framework

Content Operations define two distinct memory recall strategies, mimicking human cognitive architecture:

- Short-Term Recall (Working Memory): By loading a temporary DID (Data ID), an agent can retrieve complex task data generated in a prior workflow stage. This allows for high-precision handoffs between specialized agents. For example, a "Researcher Agent" might save a 10,000-word transcript and pass only the 36-character DID to a "Summarizer Agent." The Summarizer then uses LOAD to hydrate its context only when needed, maintaining token efficiency and focus.
    
- Long-Term Recall (Persistent Memory): By loading the special "LOG" identifier, an agent recalls its cumulative narrative history. This enables Agent Self-Adaptation, where the agent "reads its own diary" to remind itself of user preferences (e.g., "User prefers brief bullet points"), previous diagnostic results, or established rules from sessions held weeks or months prior. This ensures longitudinal consistency in the user-agent relationship.
    

### 2.3 Execution Mode

Symbolic Turn. Unlike LLM-driven responses, which are probabilistic and subject to hallucination, LOAD is a deterministic symbolic operation. It fetches the exact binary or text string stored at the provided database address. This ensures that "Recalled Truth" is preserved with 100% fidelity, acting as an immutable anchor for the agent's reasoning.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax

@LOAD("DID")@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"DID"|String|Required|The unique identifier of the content. This can be a system-generated GUID (e.g., "2B99B2E4-...") or the reserved system string "LOG".|

### Return/Output Value

- Standard DID: Returns the raw string, JSON-serialized object, or HTML content stored at that specific location.
    
- LOG Identifier: Returns the entire concatenated content of the current Agent's Log as a single string. This output is typically parsed later using symbolic logic (MAP, INDEX) or provided to an LLM for thematic analysis of past interactions.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow

1. Address Resolution: The system checks if the provided string is the reserved "LOG" token or a standard Data ID (DID).
    
2. Permission Check: The CAFA engine verifies that the requesting agent and the current user session have the authorization to access the data associated with that DID. Unauthorized requests fail gracefully with a null return.
    
3. Data Hydration: The raw content is retrieved from the storage tier (transitional for DIDs, persistent for LOG) and injected into the current Turn Result (@TR@).
    
4. Logic Availability: Once the turn completes, the loaded data becomes available for processing by parameters or subsequent logic commands.
    

### 4.2 The LOAD Dependency Rule (Rule 6.2)

A critical rule of the CAFA state machine is the Separation of Concerns. Because commands within a single turn are processed atomically/simultaneously, data loaded in Turn N is not immediately available to other commands within that same turn's prompt string.

- Incorrect (Race Condition):  
    "user": "@LOAD("LOG")@ | @SET("MyLog", "@TR@TN(0)@@")@"  
    Reason: The @TR@ of the current turn is not finalized until the turn ends, so the SET command will capture empty data.
    
- Correct Pattern (Sequential Handoff):
    

1. Turn N (Hidden): "user": "@LOAD("LOG")@" (The fetch operation occurs here).
    
2. Turn N+1 (Hidden): "user": "@SET("MyLog", "@TR@TN(-1)@@")@" (The data is now safely committed to a parameter for use).
    

### 4.3 Data Security: The "Secret Key" Concept

The security of CAFA Content Operations relies on the secrecy of the DID.

- Unguessable GUIDs: System-generated DIDs follow the 128-bit GUID structure, making them practically impossible to brute-force, providing "security through obscurity" at a massive scale.
    
- DID as a Pointer: To maintain system performance, agents should pass DIDs (small pointers) between one another rather than raw, bulky datasets. This prevents "context bloating" and ensures that data is only loaded when strictly necessary for the immediate task.
    

## 5. Advanced Use Cases and Implications

### 5.1 Multi-Agent State Handoff

In a complex ecosystem, LOAD allows for the "Chained Agent" pattern.

1. Agent A (Drafting): Creates a document and performs @SAVE(@TR@)@. It receives DID_123.
    
2. Transition: Agent A passes DID_123 to Agent B (the Reviewer).
    
3. Agent B (Critique): Performs @LOAD("DID_123")@. It now has the full text of Agent A's work without needing a direct link or shared memory space.
    

### 5.2 Agent Self-Correction and Adaptability

By loading the "LOG", an agent can perform a Reflection Turn. Before answering a new query, the agent loads the log and analyzes it: "In previous sessions, the user expressed frustration with long-winded technical explanations." The agent then adjusts its current temperature or system prompt to be more concise.

### 5.3 Forensic Accountability

Because LOAD retrieves data from a persistent log, every interaction can be audited. In regulated industries (healthcare, legal, finance), the ability to LOAD the exact state of an agent from six months ago is vital for compliance and ensuring the "Truth" of the agent's reasoning remains verifiable.

## 6. Reference

- Choi, J. (2025). LOAD Command: Retrieve Data from Artifacts or Log. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    
---
# EXPORT Command: Serialize and Persist Structured Ontology Models

## 1. Metadata & Retrieval Keys

- Category: State Management / Content Operations
    
- Summary: Acts as the high-fidelity, structured counterpart to the SAVE command. Instead of persisting raw strings, EXPORT serializes entire Agent Parameters (APs)—including internal values, ordering conditions, and semantic descriptions—into a singular "Ontology Model" package, committing it to a Data ID (DID) or the persistent Agent Log.
    
- RAG Keywords: EXPORT, structured SAVE, ontology model, knowledge serialization, state snapshot, AP bundling, structured storage, Data ID, DID, persistent log, cross-session memory, knowledge package, metadata preservation, database zip, inter-agent collaboration, knowledge handoff, stateful backup.
    
- Related Commands: IMPORT (Deserialization counterpart), SAVE (Raw persistence), LOAD (Raw retrieval), SET (In-memory update).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 The Evolution: From Raw Strings (SAVE) to Structured Knowledge (EXPORT)

In the CAFA ecosystem, SAVE is used for high-velocity, atomic journaling—saving a "note" or a single line of interaction history. However, sophisticated agents require the ability to persist their entire "mental state." EXPORT is the structured version of SAVE. It handles the Ontology Model (the "book") rather than just the message (the "note").

### 2.2 Metadata Preservation and High-Fidelity Snapshots

Unlike a standard SAVE which only preserves the "org" (the content), EXPORT captures the entire metadata layer of the specified parameters. This includes:

- Key/Name: The unique identifier of the parameter (e.g., MATH_LEVEL).
    
- Value/Org: The raw data string or pipe-separated list.
    
- Condition (cond): The ordering and linking logic (e.g., SHUFFLE, SORT, LINK).
    
- Description (desc): The semantic documentation of the parameter.
    

This ensures that when data is eventually retrieved via IMPORT, the agent recovers a fully functional, structured memory ready for execution without additional logic.

### 2.3 Structural Integrity and Inter-Agent Portability

EXPORT is the primary engine for Ontology Portability. It preserves the Epistemological Integrity of the data, as the structural warrants and relationships established by the first agent are perfectly mirrored in the second during a handoff.

## 3. Formal Syntax & Parameter Schema (The "What")

### 3.1 Command Syntax

@EXPORT("parameter_list"[, "ID"])@  
  

### 3.2 Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"parameter_list"|String|Required|A pipe-separated list of the names of the Agent Parameters (APs) to be bundled (e.g., STUDENT_NAMES)|
|"ID"|String|Optional|A target identifier. Use "LOG" for persistent memory or a custom ID. If omitted, the system generates a unique DID (GUID).|

### 3.3 Return/Output Value

- Anonymous Export: Returns a system-generated unique DID (GUID) string (e.g., 4A1B2C3D-E4F5-6G7H...).
    
- Targeted Export: Returns the provided ID string (e.g., "LOG").
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic: The "Bundling" Process

1. Parameter Discovery: The system scans the options.params (volatile memory) for every key listed in the parameter_list.
    
2. Structural Encoding: For each identified parameter, the system creates a JSON-structured object nesting the org, cond, and desc values.
    
3. Packaging: These objects are bundled into a single, binary-safe string package, checksum-verified for integrity.
    
4. Commitment: * If Anonymous: A new 128-bit GUID address is allocated and the package is committed.
    

- If "LOG": The system overwrites the existing persistent log. This is a critical architectural decision: an EXPORT snapshot is a "point-in-time truth" that supersedes previous history.
    

### 4.2 The "Overwrite" Rule for LOG (Critical Distinction)

- SAVE("data", "LOG"): Performs a Chronological Append. Treats the log as a growing narrative.
    
- EXPORT("params", "LOG"): Performs a State Replacement. Erases previous history and replaces it with the "Current Truth" of the structured parameters.
    

## 5. Reference

- Choi, J. (2025). EXPORT Command: Serialize and Persist Structured Ontology Models. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# IMPORT Command: Load Content from External Modules

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / State Management
    
- Summary: Retrieves a previously serialized "Ontology Model" package—originating exclusively from an EXPORT command—from a Data ID (DID) or the persistent "LOG." It automatically re-instantiates the agent's structured memory state by populating multiple Agent Parameters (APs) simultaneously. It serves as the functional companion to the EXPORT command and represents the Extended/Structured version of the LOAD command.
    
- RAG Keywords: IMPORT, ontology-model, memory-hydration, state-restoration, side-effect, unbundling, deserialization, persistent-knowledge, cross-session, AP-population, GUID-retrieval, structured-memory, initialization, modularity, knowledge-handoff, structured LOAD, EXPORT companion, memory unzipping.
    
- Related Commands: EXPORT (Mandatory source/Serialization), SAVE (Raw persistence), LOAD (Raw retrieval/Primitive predecessor), SET (Manual assignment).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 The Evolution: From Primitive Recall (LOAD) to Structured Hydration (IMPORT)

The IMPORT command is conceptually the Extended version of LOAD. While a standard LOAD retrieves a single, raw, unstructured string (comparable to reading a single "note"), it places a heavy cognitive load on the agent developer, who must write complex and often fragile parsing logic to transform that raw string back into usable variables. IMPORT upgrades this primitive recall into "Knowledge Hydration." It handles the unbundling of an entire knowledge state (the "book") automatically, restoring the complex internal architecture of the agent in a single execution cycle without manual string manipulation.

### 2.2 The Companion Logic: The EXPORT/IMPORT Loop

IMPORT is the mandatory companion to EXPORT. They form a "Serialization/Deserialization" symmetry, much like a Zip/Unzip operation for cognitive models.

- The EXPORT Phase: An agent bundles its current "mental state" (multiple parallel lists, user profiles, and logic settings) into a single, structured GUID-based package.
    
- The IMPORT Phase: A downstream agent (or the same agent in a future session) receives that GUID and "unarchives" it. This ensures that the Epistemological Integrity of the data—including the specific relationships between parallel parameters—is maintained perfectly across sessions or between different agents in a complex multi-agent network.
    

### 2.3 Theoretical Grounding: Cognitive Memory Unzipping

By using IMPORT, an agent recovers more than just raw data values; it recovers the Ontology Metadata. This includes the keys, conditions (cond), and descriptions (desc) assigned by the original "Maker." This aligns with the Construct Validity of Records, ensuring that the recovered memory is as structurally sound as the moment it was first conceived. It allows for "Cognitive Memory Unzipping," where a single pointer (the DID) hydrates a vast network of inter-related knowledge.

### 2.4 Execution Mode

Symbolic Turn. It is a deterministic operation that bypasses the LLM to modify the internal state machine directly. This guarantees that "Recalled Truth" is never subject to generative hallucination or interpretation errors; the data restored is identical to the data exported.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax

@IMPORT("DID")@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"DID"|String|Required|The unique identifier (GUID or "LOG") of the Ontology Model package. Crucial: This DID must have been generated by a prior EXPORT command to ensure the package structure is valid.|

### Return/Output Value

- Side-Effect (Primary): Automatically executes a SET command for every parameter contained within the structured bundle.
    
- Output: Returns a status confirmation or null to the Turn Result (@TR@).
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow: The Hydration Process

1. Fetch: The system retrieves the structured package from the storage layer (Transitional for anonymous DIDs, Persistent for "LOG").
    
2. Integrity Check: The engine verifies that the package is a valid Ontology Model (produced by EXPORT).
    
3. Unbundle: The engine parses the package, extracting the parameter names, their associated values, and metadata (condition and description).
    
4. Hydration (Automated SET): The system triggers an internal SET sequence. For every key found in the bundle, it updates the corresponding Agent Parameter in the volatile memory, inheriting the cond and desc metadata.
    
5. Commit: The parameters become available for reference (e.g., @PARAM_NAME@) starting from the turn immediately following the IMPORT turn.
    

### 4.2 Comparison: LOAD vs. IMPORT

|   |   |   |
|---|---|---|
|Feature|LOAD (Primitive)|IMPORT (Extended/Structured)|
|Data Format|Raw Unstructured String|Structured Ontology Model (Object)|
|Source Requirement|Works with SAVE output|Requires EXPORT output|
|Logic Burden|Requires manual parsing/SET|Automated state restoration|
|Metadata|Value only|Name + Value + Condition + Description|
|Complexity|1:1 (One DID to one string)|1:N (One DID to many parameters)|
|Analogy|Reading a sticky note|Restoring a database backup|

### 4.3 Rule 6.2 Compliance: The Dependency Rule

Data hydrated via IMPORT is not available within the same turn it is called. This is a common pitfall in agent modeling.

- Turn N (Hidden Setup): "user": "@IMPORT("LOG")@" — The state is recovered here.
    
- Turn N+1 (Visible Response): "user": "Welcome back, @USER_NAME@!" — The parameter is now ready for use.
    

## 5. Implications and Advanced Best Practices

### 5.1 Modular Agent Handoff Pattern

In a CAFA ecosystem, IMPORT enables modular architecture. A "Researcher Agent" can perform complex calculations and EXPORT its entire parameter state. It then passes only the resulting DID to a "Manager Agent." The Manager performs an IMPORT of that DID, instantly gaining the Researcher's full "contextual brain" without needing to re-process the raw data.

### 5.2 Robustness through Pre-Definition

Always pre-define the parameters you expect to IMPORT (especially from "LOG") in the options.params object with empty values. This ensures that even on the very first run—when the LOG is empty and the IMPORT side-effect does not occur—subsequent turns referencing those parameters will not crash the agent.

### 5.3 Forensic State Reconstruction

Because IMPORT restores the exact state of an agent, it is the primary tool for forensic auditing. An auditor can take a DID from a historic interaction, IMPORT it into a diagnostic agent, and see exactly what internal parameters were active at the moment of a specific AI-driven decision.

## 6. Reference

- Choi, J. (2025). IMPORT Command: Load Content from External Modules. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# GS Command: Fetch Raw Data from Google Sheets

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / External Integration
    
- Summary: Establishes a direct, read-only data pipe between a CAFA agent and a Google Sheet, retrieving raw cell content as a structured, double-delimited string.
    
- RAG Keywords: GS, Google Sheets integration, cloud-native knowledge, external database, sheetID, A1 notation, range-retrieval, double-delimited-string, ampersand-delimiter, pipe-delimiter, ontological-commitment, symbolic-logic-grounding, real-time-data, external-truth-source, knowledge-decoupling.
    
- Related Commands: GSTABLE (Structured table version), MAP (Data transformation), INDEX (Item lookup), SAVE (Log-to-Sheet feedback).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Overcoming Knowledge Stagnation

The GS command decouples Inference Logic (agent code) from the Knowledge Base (cloud data). This externalization allows Agent Makers to update facts or rules in real-time via a spreadsheet without re-deploying agent code, creating a "Living System."

### 2.2 Theoretical Grounding: The TEAM Framework

By moving the "Source of Truth" to a transparent cloud environment, the agent’s logic becomes forensic. It facilitates Ontological Commitment, where experts can audit and participate in refining the knowledge base directly.

### 2.3 Execution Mode

Symbolic Turn. A deterministic, 1:1 bit-accurate fetch operation. It provides the "Ground Truth" context that prevents LLM hallucinations during analytical turns.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax

@GS("sheetID", "range")@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"sheetID"|String|Required|The unique alphanumeric string in the Sheet URL between /d/ and /edit.|
|"range"|String|Required|Standard A1 notation (e.g., "Sheet1!A1:B10").|

### Return Format: The Double-Delimited String

- Cell Delimiter: & (Ampersand) separates columns.
    
- Row Delimiter: | (Pipe) separates rows.
    
- Result Example: "ID&Name|1&Alpha|2&Beta"
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow

1. Permission Check: Validates that the sheet is set to "Anyone with the link can view."
    
2. Fetch: Retrieves raw cell values.
    
3. Serialization: Converts the grid into the Cell&Cell|Row string format.
    
4. Hydration: Injects the result into @TR@.
    

### 4.2 Security and Sovereignty (Rule 9.1)

- Sensitive Data: Never store PII in a linked sheet; sheetID is considered public-facing.
    
- Circular Design: Pull data via GS; analyze via IMPORTDATA pointing to the CAFA Log URL in the same sheet.
    

## 5. Reference

- Choi, J. (2025). GS Command: Fetch Raw Data from Google Sheets. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# GSTABLE Command: Advanced Structured Integration

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / External Integration
    
- Summary: Transforms tabular data from a Google Sheet directly into a structured Ontology Model by automatically instantiating and populating multiple Agent Parameters (APs) based on column headers or indices. It serves as the high-capacity data pipe for cloud-integrated symbolic grounding.
    
- RAG Keywords: GSTABLE, Google Sheets integration, automated-SET, ontology-model-instantiation, tabular-data-import, cloud-memory-hydration, P1-P2-fallback, data-grounding, symbolic-computer-input, dynamic-knowledge-retrieval, cloud-native memory, parallel list synchronization, external knowledge base, multi-parameter injection.
    
- Related Commands: GS (Raw fetch version), SET (Manual assignment), MAP (Data transformation), IMPORT (Package restoration), INDEX (Item lookup).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 The Problem of Structural Manualization

Manually synchronizing multiple parallel lists—such as a product inventory where Name, Price, and Stock must remain perfectly aligned—via individual SET or GS commands is labor-intensive, error-prone, and mathematically risky. If one list is updated and others are not, the index-based relationship between parameters breaks. GSTABLE solves this "Structural Manualization" problem by automating the mapping of a 2D cloud-based table into a cohesive 1D multi-parameter structure in a single atomic operation.

### 2.2 Ontological Synchronicity

The GSTABLE command facilitates Ontological Synchronicity. It ensures that the "Source of Truth" managed by a Teacher, Maker, or Subject Matter Expert in a spreadsheet is perfectly mirrored in the agent's symbolic memory. This allows for Teacher Empowered Assessment (TEAM), where the educator maintains full sovereignty over the agent's knowledge base without needing to modify JSON code.

### 2.3 Execution Mode: High-Fidelity Hydration

Operating as a Symbolic Turn (⚙️), this deterministic operation performs mass-hydration of the agent's volatile memory. It bypasses generative interpretation entirely, providing high-fidelity data arrays that serve as the "Ground Truth" for subsequent LLM turns. This is critical for preventing hallucinations in data-heavy tasks.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax

@GSTABLE("sheetID", "range"[, "option"])@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"sheetID"|String|Required|The unique 44-character alphanumeric identifier found in the Google Sheet URL.|
|"range"|String|Required|The A1 notation for the target table (e.g., "Inventory!A1:E21").|
|"option"|String|Optional|Use "NO" to bypass header detection. If used, columns are assigned default names (P1, P2, etc.).|

### Return/Output Value

- Side-Effect (Primary): The command's primary output is its impact on the state machine. it automatically generates and executes an internal SET command for every column identified in the specified range.
    
- Output: Returns a success/failure status string to the Turn Result (@TR@).
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow

1. Permission Check: The system validates that the target Google Sheet is shared with the setting "Anyone with the link can view."
    
2. Tabular Scan: The engine retrieves the 2D data array from the specified range.
    
3. Header Processing:
    

- Default Behavior: The engine treats the first row as the keys (Parameter Names). For example, if cell A1 contains "Course", a parameter @Course@ is created.
    
- "NO" Option: The engine ignores header names and assigns P1, P2, P3, etc., as the parameter names.
    

4. Mass-Hydration (Automated SET): For each column, the engine serializes the data into a pipe-separated string and executes an internal @SET("Key", "Value1|Value2|Value3")@.
    
5. Commitment: All newly created or updated APs are committed to volatile memory at the conclusion of the turn.
    

### 4.2 Rule 6.2 Compliance: The Dependency Rule

Parameters instantiated via GSTABLE in Turn $N$ are not available for use until Turn $N+1$. Attempting to reference them in the same turn will result in an "undefined" error.

- Turn N (Hidden): @GSTABLE("10X9...", "A1:B10")@ — Memory hydration occurs silently.
    
- Turn N+1 (Visible): "Successfully loaded @Make[N]@ records. First entry is @Make[1]@."
    

## 5. Advanced Implementation Patterns

### 5.1 Pattern 1: Dynamic Knowledge Grounding

In enterprise scenarios, GSTABLE is used to ground an LLM in a live database.

1. Turn 1 (Hidden): @GSTABLE("ID", "PriceList!A1:C100")@
    
2. Turn 2 (LLM): "You are a customer support agent. Use the following data to answer the user: @PriceList_ID@, @Product_Name@, @Current_Price@."
    

### 5.2 Pattern 2: Parallel List Synchronization for Quizzes

When building a quiz, GSTABLE ensures that the question, the correct answer, and the rationale are always synced by index.

- Sheet Structure: Column A (Question), Column B (Answer), Column C (Hint).
    
- Agent Logic: @GSTABLE("ID", "Quiz!A1:C20")@ ensures @Question[5]@ always matches @Answer[5]@.
    

### 5.3 Pattern 3: Multi-User Customization

Use a hidden Google Sheet to store user settings. By running @GSTABLE on a range filtered for the current @UID@, the agent can "wake up" with a custom personality or difficulty level specific to that user.

## 6. Implications for Scalability and Maintenance

### 6.1 Epistemological Integrity

GSTABLE ensures that the internal state of the agent is a forensic mirror of the external knowledge source. This is vital for high-stakes assessments or technical documentation where the "Truth" must be verifiable by external auditors.

### 6.2 Maintenance Efficiency

By using GSTABLE, the maintenance cost of an agent drops significantly. Instead of editing complex JSON strings, a subject matter expert simply updates a spreadsheet. This democratizes AI creation, moving the "Maker" role from programmer to educator.

## 7. Reference

- Choi, J. (2025). GSTABLE Command: Advanced Structured Integration. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# RUN Command: Execute Asynchronous Background Agent Process

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / Agent Orchestration
    
- Summary: Initiates a non-blocking, asynchronous execution of a remote "Target Agent" acting as a background subroutine. It facilitates a complete "Round-Trip" data cycle where a Host Agent delegates high-compute or specialized tasks and retrieves results via shared, state-monitored Data IDs (DIDs). This command is the primary engine for building integrated multi-agent ecosystems where specialized utility agents serve as background microservices, ensuring that complex logic remains siloed and context-optimized.
    
- RAG Keywords: RUN, MacroRun, Asynchronous, BackgroundProcess, Orchestration, MultiAgent, RoundTrip, Subroutine, Distributed-Intelligence, Agent-Delegation, Safe-Polling, Latency-Handling, Agent-Handoff, ID_ID, OD_ID, API-Subroutine, Inter-Agent-Communication, State-Synchronization, Cognitive-Delegation, Modular-AI-Architecture, Remote-Procedure-Call, CAFA-Cloud-Execution, Temporal-Buffer.
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Overcoming the "Complexity Wall" and Instructional Entropy

In complex AI modeling, a "Monolithic Agent"—a single agent designed to handle every possible logic branch and data transformation—eventually encounters a "Complexity Wall." This wall manifests as context window exhaustion and, more critically, Instructional Entropy. Instructional entropy occurs when an LLM is provided with too many conflicting system prompts; for example, telling an agent to "be a friendly, empathetic tutor" while simultaneously "performing rigorous, cold statistical validation" often results in prompt leakage, where the empathetic tone compromises the statistical rigor or vice-versa.

The RUN command enables a Modular Architecture by treating specialized agents as "Micro-Cognitive Services." By delegating a task (e.g., "Translate this transcript" or "Solve this Calculus problem") to a specialized Target Agent, the Host Agent acts as a "Prompt Firewall." The Target Agent operates in its own isolated execution environment with a fresh context window and a single, focused system prompt. This ensures that the Host Agent remains lightweight and responsive, maintaining its cognitive integrity and avoiding the "Jack-of-all-trades" hallucination trap that plagues monolithic prompt engineering.

### 2.2 One-Way Handoff vs. Round-Trip Execution: Deep UX Analysis

CAFA defines two distinct patterns for inter-agent movement, dictated by the desired User Experience (UX) and the necessity of state preservation:

- MACRO Essential (One-Way Handoff): This represents a linear, relay-style workflow. The user is presented with a hyperlink; upon clicking, they explicitly "leave" Agent A and "arrive" at Agent B. This is ideal for transitions between major project phases (e.g., from "Creative Ideation" to "Technical Drafting") where a fresh interface and a complete context switch are beneficial. This is a "Destructive Transition" in terms of foreground state; the state of Agent A is typically archived or passed as a static reference rather than maintained in active memory.
    
- MACRO Run (Round-Trip Execution): This represents an integrated, "Native-App" workflow. The Host Agent triggers the Target Agent in the background. The user never perceives the transition; they remain within the Host's interface. The Target Agent acts as a silent backend worker that processes data and "returns" it to a shared container. This is essential for utility functions like real-time translation, automated grading, or data formatting where the user requires a seamless, singular interface experience. It preserves "Contextual Hygiene" by ensuring the Host's memory is not cluttered with the intermediate processing logs of the Target.
    

### 2.3 Theoretical Grounding: Subroutine Cognitive Delegation

RUN mirrors the "Async/Await" or "Fetch" patterns found in modern software engineering, but applies them to Cognitive Labor. It represents a shift from Sequential Processing (where the user must wait for every step) to Asynchronous Delegation. By dispatching a "Worker" to handle a sub-task, the Host Agent can maintain a state of "Busy Waiting" (Polling), allowing the CAFA cloud to handle the heavy lifting in parallel. This mirrors high-level human management: a project lead (Host) assigns a task to a specialist (Target) and checks back periodically for a status update, rather than micromanaging the specialist's step-by-step execution.

### 2.4 Tokenomic and Performance Optimization

By utilizing RUN, developers can implement Heterogeneous Model Handoffs. A Host Agent running on a high-fidelity, high-cost model (e.g., GPT-4o) can delegate simple data formatting or translation tasks to a Target Agent running on a low-cost, high-speed model (e.g., GPT-4o-mini). This optimizes the "Token Budget" by ensuring that expensive cognitive cycles are only spent on high-reasoning tasks, while background utilities are handled by cost-efficient subroutines.

### 2.5 Execution Mode: Deterministic System-Level Trigger

Symbolic Turn. It is a system-level command that triggers a cloud event. Because it is asynchronous and non-blocking, the Host Agent continues execution immediately after the trigger signal is dispatched. This creates a synchronization challenge: the Host Agent must be programmed to "wait" for a process that it no longer controls, necessitating the "Safe Polling" architecture.

## 3. Formal Syntax & Parameter Schema (The "What")

### Standard Command Syntax (Golden Template)

@RUN("Agent_ID", "ID_ID", "OD_ID"[, "CAFA_KEY", "API_KEY"])@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|Agent_ID|String|Required|The UUID/ID of the Target Agent (the "Worker") in the CAFA cloud. This address must be valid and the agent must be saved on the platform.|
|ID_ID|String|Required|Input Data ID. The DID (Data ID) containing the specific payload, instructions, or context the Host is sending to the Target. This is the "Stateless Payload."|
|OD_ID|String|Required|Output Data ID. The DID "Inbox" or "Return Envelope" where the Target is instructed to write the final result. The Host monitors this ID for state changes.|
|CAFA_KEY|String|Optional|Overrides the current session with a specific CAFA Key for departmental billing. If omitted, the target agent must store/provide its own key.|
|API_KEY|String|Optional|Overrides the LLM API key. Allows the Host to "sponsor" the Target's high-tier model costs (e.g., using O1). If omitted, the target agent must store/provide its own key.|

### Return/Output Value

- Immediate Response: Returns a system status flag (Success/Failure of the trigger) to the Host's @TR@.
    
- Substantive Result: The actual data is written by the Target into the OD_ID container.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 The "Safe Polling" Design Pattern: Managing Latency

Because the RUN command is non-blocking, the Host Agent will reach the next turn before the Target Agent has even initialized its LLM session. To bridge this temporal gap, developers must implement the Safe Polling Loop.

1. Preparation (Turn N):
    

- Payload Packaging: The Host saves input data: @SET(ID_ID, "@SAVE("@USER_INPUT@")@")@.
    
- Semaphore Placement (The Star Flag): The Host creates OD_ID and seeds it with a Magic Value: @SET(OD_ID, "@SAVE("★")@")@. This "star" serves as a semaphore; as long as the content is "★", the Host knows the job is pending.
    

2. Trigger (Turn N+1):
    

- The Host fires the @RUN(...)@ command. The CAFA cloud initializes the Target Agent. The Host proceeds instantly to the next turn.
    

3. Polling Loop (Turns N+2 to N+4) - THE CRITICAL PHASE:
    

- Step A: The Temporal Buffer (Dummy LLM Turn): [RECOMMENDED] After the RUN execution, the Host should execute a "dummy" LLM turn.
    

- Rationale: Symbolic turns execute in milliseconds. Without a buffer, the Host will check OD_ID 20 times and "time out" before the Target Agent has finished its cold start.
    
- Implementation: A hidden LLM turn (system: "Wait...", user: "Wait...") with max-tokens: 1. This creates a ~2-3 second window for background processing.
    

- Step B: State Check: The Host loads the current inbox value: @SET(CHECK_VAL, "@LOAD("@OD_ID@")@")@.
    
- Step C: Logic Gate: Using @JUMP@, the Host compares CHECK_VAL to the semaphore ("★"). If they are equal AND the retry limit is not hit, the Host returns to Step A.
    

4. Retrieval (Turn N+5):
    

- Once CHECK_VAL no longer equals "★", the Target has written the result. The Host breaks the loop and hydrates its parameters with the new data.
    

### 4.2 State Impact on the Target Agent: The "Worker" Contract

For a round-trip to succeed, the Target Agent must be architected as an "Atomic Worker." It must follow this strict internal workflow:

1. Input Retrieval: It must fetch the ID_ID passed in its parameters: @LOAD("@ID_ID@")@.
    
2. Atomic Processing: It must process the result within a single session, avoiding its own internal user-facing loops.
    
3. Deterministic Output: It must save its final answer to the OD_ID provided by the Host: @SAVE("@RESULT@", "@OD_ID@")@.
    
4. Immediate De-allocation: It must terminate with @END@ to free cloud resources immediately.
    

### 4.3 Parallelism: The "Fan-out/Fan-in" Multi-Agent Pattern

The RUN command enables Parallel Cognitive Processing, similar to a "Map-Reduce" algorithm in big data:

1. Fan-out Phase (Map): A single Host Agent dispatches three separate RUN commands to three different specialized agents (e.g., a "Fact Checker," a "Grammar Expert," and a "Sentiment Analyst") in the same turn.
    
2. Execute Phase: All three Target Agents run concurrently in the cloud, utilizing separate compute resources.
    
3. Fan-in Phase (Reduce): The Host enters a polling loop that waits for all three OD_IDs to change from "★". Once all are ready, it consolidates the three results into a single final report. This reduces total latency by roughly 66% compared to running three tasks sequentially.
    

### 4.4 Error Handling: The "Partial Success" and "Silent Failure" Shield

- Timeout Logic: The LOOP_COUNT parameter is mandatory. If the loop reaches its limit (e.g., 20 retries), the Host must provide a user-friendly error message rather than displaying the semaphore "★".
    
- Partial Success: In "Fan-out" patterns, the Host should be programmed to handle cases where 2 of 3 workers finished. It can choose to proceed with "Partial Data" or retry only the failed worker.
    

## 5. Implications for Epistemological Integrity

By using RUN, the "Truth" of a specialized diagnosis is preserved. When a general-purpose Host Agent asks a specialized "Diagnostic Agent" for a result, the response is delivered as an Atomic Knowledge Artifact. This prevents the primary agent's personality or conversational style from "bleeding" into the technical accuracy of the result, ensuring the highest level of Epistemological Integrity and forensic accountability in the multi-agent network.

## 6. Reference

- Choi, J. (2025). RUN Command: Execute Asynchronous Background Agent Process. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# RADIO Command: Select Single Option via Radio Buttons

## 1. Metadata & Retrieval Keys

- Category: UI & User Interaction / Symbolic Input Controls
    
- Summary: Deterministically captures a single user selection from a predefined list of options within the CAFA Immersive interface. It functions as a symbolic anchor that transforms high-entropy human intent into structured, machine-readable data, with specialized support for the SCREAM framework to capture simultaneous Selected Response (SR) and Constructed Response (CR) data points in a single atomic transaction.
    
- RAG Keywords: RADIO, UI control, user-selection, multiple-choice, input-form, user-interaction, SCREAM-framework, SR, CR, Selected-Response, Constructed-Response, decision-point, branching-logic, symbolic-input, machine-readable-data, form-submission, execution-pause, deterministic-input.
    
- Related Commands: CHECKBOX (Multiple selection), SELECT (Dropdown menu), TEXT (Single-line input), TEXTAREA (Multi-line input), MAP (Symbolic logic routing), INDEX (Parallel list lookup), JUMP (Turn-based navigation).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Resolving the "Entropy Problem"

In standard generative AI interactions, freeform natural language input is inherently high-entropy—unpredictable, difficult to parse, and computationally expensive to validate. This "Entropy Problem" makes it nearly impossible to drive strict, reliable branching logic or state-based workflows. The RADIO command solves this by "symbolizing" human input; it restricts the user's interaction space to a predefined set of symbols that the CAFA engine can process with 100% mathematical fidelity.

### 2.2 Theoretical Grounding: Ontological Commitment and ToA

The RADIO command is a technical instantiation of Ontological Commitment. By presenting a finite set of choices, the agent forces the user to interact within the agent's defined world model (Ontology). This is critical for the Trinity of Assessment (ToA), specifically within the Fidelity pillar. When a user selects a radio button, the agent receives a "Clean Signal" of intent, allowing for precise diagnostic evaluation without the noise of LLM interpretation.

### 2.3 The SCREAM Framework: Alignment of Choice and Rationale

A unique dimension of the CAFA RADIO control is its integrated support for the SCREAM (Selected Response & Constructed Response Assessment Model) framework. By utilizing the optional other_prompt argument, the agent does not merely record what the user chose (SR), but captures why they chose it (CR) simultaneously. This enables forensic alignment: an analyst or a downstream agent can verify if a correct choice was based on sound reasoning or a "lucky guess," thereby preserving the Epistemological Integrity of the interaction.

### 2.4 Execution Mode: Deterministic Symbolic Sovereignty

The command operates strictly as a Symbolic Turn (⚙️). It bypasses the probabilistic nature of the LLM to ensure that the user's choice is recorded exactly as clicked. This "Symbolic Sovereignty" ensures that the agent's internal state machine remains synchronized with the physical reality of the user's interaction.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax (Golden Template)

@RADIO("name", "prompt", "options"[, "other_prompt"])@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|name|String|Required|A unique internal identifier for the control (e.g., "diagnostic_v1"). This serves as the parameter key for retrieval.|
|"prompt"|String|Required|The instructional text or question displayed directly above the radio buttons (e.g., "Select the most likely cause:").|
|"options"|String|Required|A pipe-separated list|
|"other_prompt"|String|Optional|Triggers the SCREAM interface. This adds a dedicated multi-line text input field below the radio buttons to capture the user's rationale or explanation.|

### Return/Output Value: The Retrieval Mechanism

The value captured by the control is retrieved using the syntax @RADIO("name")@. The format of the returned string is dictated by the mode of operation:

- Standard Mode: Returns the exact string value of the selected option.
    

- Example: If "Option B" is selected, @RADIO("choice")@ returns "Option B".
    

- SCREAM Mode (with other_prompt): Returns a serialized, pipe-separated string containing both the selection (SR) and the explanation (CR).
    

- Example: @RADIO("eval")@ returns "Option B|The user's written explanation here...".
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow: The Pause-Submit-Resume Cycle

The RADIO command orchestrates a complex state-synchronization event between the CAFA server and the client-side Immersive interface:

1. Parsing & Rendering: The system identifies the command in a visible turn ("show": true) and renders the graphical group of radio buttons.
    
2. Automatic Submit Generation: The CAFA engine automatically appends a "Submit" button to the end of the turn's output. Developers do not need to manually create a submission trigger.
    
3. Execution Pause (The "Human-in-the-Loop" Gate): The agent enters a mandatory "Waiting" state. All automated turn progression halts, and the system clock for that session pauses, waiting for human intervention.
    
4. Interactive Capture: The user interacts with the UI. In SCREAM mode, the system maintains a real-time buffer of the text entered in the "Other" field alongside the radio selection.
    
5. Data Commitment & Auto-Advance: Upon the user clicking "Submit," the engine commits the value to the session's volatile memory under the key specified in the name argument. The agent then automatically "wakes up" and transitions to the next turn in the prompts array.
    

### 4.2 Constraints and Implementation Patterns

- Rule of Uniqueness (The Single-Control Mandate): Only one interactive input control (RADIO, CHECKBOX, TEXT, etc.) is permitted per visible turn. Multiple controls in a single turn would create ambiguity regarding the "Submit" action and the data commitment sequence.
    
- The "Logic Handoff" Pattern: A RADIO turn is almost universally followed by a hidden logic turn ("show": false) that uses the MAP command or JUMP to route the user.
    

- Pattern: Turn 1 (RADIO) -> Turn 2 (MAP or INDEX to evaluate input) -> Turn 3 (Tailored Feedback).
    

- SCREAM Data Extraction: In the turn following a SCREAM-enabled RADIO command, developers typically use the INDEX or MAP command to split the returned string.
    

- Example Logic: @SET("SR", "@INDEX("@RADIO("name")@", "|", "1")@")@ and @SET("CR", "@INDEX("@RADIO("name")@", "|", "2")@")@.
    

## 5. Implications for Multi-Agent Systems

In modular architectures, the RADIO command acts as a Decision Node. A Host Agent can use RADIO to let the user select a specialized service (e.g., "Translator" vs "Summarizer") and then use the resulting value to dynamically route a @RUN command to the appropriate Target Agent ID. This allows for user-driven orchestration of complex agent networks.

## 6. Reference

- Choi, J. (2025). RADIO Command: Select Single Option via Radio Buttons. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# CHECKBOX Command: Select Multiple Options via Checkboxes

## 1. Metadata & Retrieval Keys

- Category: UI & User Interaction / Symbolic Input Controls
    
- Summary: Deterministically captures one or more user selections from a predefined list of options within the CAFA Immersive interface. It transforms high-entropy human intent into a structured, pipe-separated machine-readable string, enabling complex multi-criteria data collection and high-fidelity state hydration in a single atomic transaction.
    
- RAG Keywords: CHECKBOX, UI control, multi-select, input-form, user-interaction, multiple-choice, symbolic-input, machine-readable-data, form-submission, execution-pause, deterministic-input, pipe-separated-string, UI-synchronization, cognitive-anchoring, human-in-the-loop, data-structuring, response-validation, ontological-commitment, interaction-gate, multi-dimensional intent, atomic selection.
    
- Related Commands: RADIO (Single selection), SELECT (Dropdown menu), TEXT (Single-line input), TEXTAREA (Multi-line input), MAP (Symbolic logic routing), INDEX (Parallel list lookup), GSTABLE (Cloud data hydration).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Managing Multi-Dimensional Intent

While the RADIO command is designed for binary or mutually exclusive decision points (A or B), many real-world scenarios require the capture of multi-dimensional intent—where the user's state is defined by a combination of factors rather than a single choice. For example, in a diagnostic setting, a user might need to "Select all symptoms that apply" (e.g., Fever, Cough, and Fatigue).

The CHECKBOX command solves this by allowing the user to select any number of symbols from a predefined set simultaneously. By serializing these multiple choices into a single, predictable data string, the agent can handle high-density information without requiring multiple turns or complex conversational parsing. This "compact intent" is then passed to downstream logic as a unified cognitive artifact.

### 2.2 Ontological Commitment in Bulk

Like all CAFA input controls, CHECKBOX enforces Ontological Commitment. It ensures that even when making multiple choices, the user remains strictly grounded within the agent's defined world model. In freeform natural language lists, users often introduce "Context Drift" by using synonyms, irrelevant details, or formatting that the agent cannot parse.

Checkboxes act as a filter, forcing human expression into the symbolic "slots" the agent is designed to process. This bulk commitment allows for the reliable collection of complex datasets—such as feature requests or user interests—ensuring that every selected item is a valid, pre-validated key in the agent's knowledge base.

### 2.3 Execution Mode: Deterministic Symbolic Sovereignty

The command operates strictly as a Symbolic Turn (⚙️). It ensures that multi-select data is captured with 100% fidelity, bypassing the probabilistic nature of LLM interpretation. This is essential for maintaining the Trinity of Assessment (ToA). When multiple criteria must be validated against a strict rubric, the agent must be certain of the exact items selected; CHECKBOX provides this certainty by recording the interaction directly into the session's state machine.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax (Golden Template)

@CHECKBOX("name", "prompt", "options")@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|name|String|Required|A unique internal identifier for the control (e.g., "user_interests"). This serves as the parameter key for all future retrieval.|
|"prompt"|String|Required|The instructional text displayed above the checkboxes (e.g., "Select all areas of interest:").|
|"options"|String|Required|A pipe-separated list|

### Return/Output Value: The Retrieval Mechanism

The values captured by the control are retrieved using the syntax @CHECKBOX("name")@.

- Output Format: Returns a pipe-separated string of all selected options. Crucially, the returned string follows the Order of Definition (the order items appear in the options argument), not the order in which the user clicked them.
    

- Example: If the options are "Science|History|Art" and the user selects "Art" then "Science", the command returns "Science|Art".
    

- Technical Note on Empty States: If no options are selected, the command returns an empty string (""). Downstream logic (like MAP or INDEX) should be programmed to handle an empty string to prevent "null reference" errors during processing.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow: The Pause-Submit-Resume Cycle

The CHECKBOX command orchestrates a fundamental state-synchronization event between the CAFA server and the client-side interface:

1. Parsing & Rendering: The system identifies the command in a visible turn ("show": true) and renders the graphical checkbox group within the Immersive view.
    
2. Automatic Submit Generation: The CAFA engine automatically appends a "Submit" button to the turn's output. This button acts as the universal gatekeeper for the symbolic transaction.
    
3. Execution Pause (The Interaction Gate): The agent enters a "Waiting" state. All automated turn progression is halted, and the session clock pauses. The agent is now entirely dependent on human intervention to proceed.
    
4. Data Commitment: Upon the user clicking "Submit," the engine serializes all checked options into the pipe-separated string and writes it to the session's volatile memory under the key specified in the name argument.
    
5. Auto-Advance: The agent "wakes up" and automatically transitions to the next turn in the prompts array, carrying the newly committed data forward.
    

### 4.2 Constraints and Implementation Patterns

- Rule of Uniqueness (The Single-Control Mandate): Only one interactive input control (CHECKBOX, RADIO, TEXT, etc.) is permitted per visible turn. Multiple controls would create ambiguity regarding which "Submit" action governs the commitment of multiple data points.
    
- The "Inclusion Check" Pattern: Because CHECKBOX returns a pipe-separated string, it is effectively a "mini-list" inside a single variable. Developers use the INDEX command to verify if a specific item was part of the user's intent.
    

- Example: To verify if a user selected "Option B", the agent uses @INDEX("@CHECKBOX("name")@", "Option B")@. If the result is not 0, the option was selected.
    

- Dynamic Grounding & Hydration: The output of a CHECKBOX command is often used to "hydrate" the context for a subsequent LLM turn. By selecting multiple items, the user creates a "Filter String" that the agent can use to pull specific, relevant records from a Google Sheet (using GS or GSTABLE) for a tailored analysis.
    

## 5. Reference

- Choi, J. (2025). CHECKBOX Command: Select Multiple Options via Checkboxes. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    
---

# TEXT Command: Input Short Single Line Text

## 1. Metadata & Retrieval Keys

- Category: UI & User Interaction / Symbolic Input Controls
    
- Summary: Deterministically captures a single-line alphanumeric text input from the user within the CAFA Immersive interface. It functions as a high-fidelity symbolic bridge for low-to-medium entropy data—such as names, identifiers, or specific keywords—ensuring that human-provided strings are committed to the session state with 100% integrity.
    
- RAG Keywords: TEXT, UI control, single-line input, user-interaction, input-form, alphanumeric-capture, machine-readable-data, symbolic-input, form-submission, execution-pause, deterministic-input, human-in-the-loop, data-structuring, response-validation, ontological-commitment, interaction-gate, short-form input, entropy-reduction, structural-boundary, alphanumeric-fidelity.
    
- Related Commands: TEXTAREA (Multi-line input), RADIO (Single selection), CHECKBOX (Multi-selection), SELECT (Dropdown menu), MAP (Logic routing), INDEX (Parallel list lookup), SAVE (Persistence).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Capturing Specificity: The Entropy Anchor

While RADIO and CHECKBOX commands are designed to ground the user within a predefined ontology (selecting from existing options), the TEXT command is essential for capturing High-Specificity Data that cannot be anticipated by the agent's maker. This includes unique identifiers like a user's name, a specific serial number, or a targeted search term.

In the CAFA ecosystem, the TEXT command acts as an Entropy Anchor. Unlike the main chat box—which is a high-entropy environment where data is often buried in conversational noise—the TEXT field provides a structured "Structural Boundary." It signals to the system that the incoming string is not a conversational turn, but a discrete symbolic unit to be processed mathematically.

### 2.2 Ontological Commitment through Instructional Constraints

Even when allowing for freeform input, the TEXT command enforces Ontological Commitment. By isolating the input to a single dedicated field with a specific prompt, the agent restricts the user's cognitive focus. This significantly reduces "Context Drift," as the user is implicitly guided to provide a concise symbol rather than a wandering natural language sentence. This "Symbolic Bottleneck" is critical for maintaining a stable state machine in complex multi-turn workflows.

### 2.3 Execution Mode: Deterministic Symbolic Sovereignty

The command operates strictly as a Symbolic Turn (⚙️). It completely bypasses the probabilistic nature of LLM interpretation. This ensures that the exact string entered by the user—preserving specific spelling, casing, and spacing—is recorded into the agent's internal state machine. This level of "Alphanumeric Fidelity" is non-negotiable for subsequent logic that relies on exact matches, such as INDEX lookups, MAP routing, or authentication-style verification.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax (Golden Template)

@TEXT("name", "prompt")@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|name|String|Required|A unique internal identifier for the control (e.g., "user_id"). This serves as the parameter key for all future retrieval and logic operations.|
|"prompt"|String|Required|The instructional text displayed immediately above the input field (e.g., "Please enter your employee ID:").|

### Return/Output Value: The Retrieval Mechanism

The value entered by the user is retrieved using the syntax @TEXT("name")@.

- Output Format: Returns the raw string entered by the user.
    

- Example: If the user enters "Student_01", @TEXT("name")@ returns "Student_01".
    

- Technical Note on Empty States: If the user submits the form without entering text, the command returns an empty string (""). Downstream logic should use MAP or EVAL to check for this empty state to prevent processing errors.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow: The Pause-Submit-Resume Cycle

The TEXT command orchestrates a fundamental state-synchronization event between the CAFA server and the client-side interface:

1. Parsing & Rendering: The system identifies the command in a visible turn ("show": true) and renders a single-line input field in the Immersive view.
    
2. Automatic Submit Generation: The CAFA engine automatically appends a "Submit" button. This ensures that the data commitment is a discrete, intentional action by the user.
    
3. Execution Pause (The Interaction Gate): The agent enters a "Waiting" state. All automated turn progression halts, and the session clock for the current turn pauses, waiting for the user to commit the symbol.
    
4. Data Commitment: Upon the user clicking "Submit," the engine captures the string and writes it to volatile memory under the key specified in the name argument.
    
5. Auto-Advance: The agent "wakes up" and automatically transitions to the next turn in the prompts array.
    

### 4.2 Constraints and Implementation Patterns

- Rule of Uniqueness (The Single-Control Mandate): Only one interactive input control (TEXT, RADIO, CHECKBOX, etc.) is permitted per visible turn. Multiple controls would create ambiguity regarding which submission governs the commitment of multiple data points.
    
- The "Sanitization Handoff" Pattern: A TEXT input turn is almost always followed by a hidden logic turn ("show": false). In this turn, the agent uses the EVAL or MAP command to validate, trim, or sanitize the input (e.g., checking if the string length is greater than 0) before proceeding to more complex operations.
    
- Dynamic Grounding: The result of a TEXT command is frequently used as a lookup key for the INDEX or MAP command. For instance, after capturing a "Course Code" via TEXT, the agent can immediately pull the corresponding "Instructor Name" from a Google Sheet (using GS).
    

## 5. Security & Sovereignty (Rule 9.1)

Because the TEXT command is used to capture user-specific data, makers must adhere to Rule 9.1 regarding PII (Personally Identifiable Information).

- Avoid using the TEXT command to collect highly sensitive data (passwords, financial records) if the agent is intended for public use, as parameters stored in the volatile state are theoretically accessible to the system engine during the session.
    

## 6. Reference

- Choi, J. (2025). TEXT Command: Input Short Single Line Text. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# TEXTAREA Command: Input Long Multi-Line Text Block

## 1. Metadata & Retrieval Keys

- Category: UI & User Interaction / Symbolic Input Controls
    
- Summary: Deterministically captures a multi-line, freeform text block from the user within the CAFA Immersive interface. It acts as a high-capacity symbolic bridge for high-entropy data—such as essays, justifications, or detailed feedback—ensuring that complex human narratives are committed to the session state with 100% fidelity for subsequent LLM analysis.
    
- RAG Keywords: TEXTAREA, UI control, multi-line input, user-interaction, input-form, high-entropy-capture, machine-readable-data, symbolic-input, form-submission, execution-pause, deterministic-input, human-in-the-loop, data-structuring, response-validation, ontological-commitment, interaction-gate, long-form input, Constructed-Response, CR, SCREAM-framework, qualitative-data-capture, narrative-fidelity.
    
- Related Commands: TEXT (Short-form input), RADIO (Single selection), CHECKBOX (Multi-selection), SELECT (Dropdown menu), MAP (Logic routing), RUN (Background processing).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Capturing Complexity: The Constructed Response (CR) Anchor

While the TEXT command is optimized for low-entropy identifiers, the TEXTAREA command is specifically engineered to capture High-Entropy Qualitative Data. In the CAFA ecosystem, this is the primary tool for the Constructed Response (CR) component of assessment. It provides a dedicated "Structural Boundary" for expansive human thought, isolating a user's reasoning or narrative from the rest of the conversational flow.

### 2.2 Ontological Commitment in Qualitative Input

Even though the input is freeform, the TEXTAREA command enforces Ontological Commitment through its instructional context. By dedicating a large, visually distinct field to a specific prompt, the agent signals a requirement for depth and detail. This "Cognitive Funnel" ensures that the user's high-entropy input is focused on a specific task or question, facilitating more accurate analytical turns by downstream LLMs.

### 2.3 Execution Mode: Deterministic Symbolic Sovereignty

The command operates strictly as a Symbolic Turn (⚙️). It ensures that the user's input is captured exactly as typed—preserving line breaks, formatting, and specific phrasing—without the risk of probabilistic "summarization" or "cleanup" that might occur if the input were passed through an LLM during the capture phase. This "Narrative Fidelity" is essential for forensic analysis and grading.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax (Golden Template)

@TEXTAREA("name", "prompt")@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|name|String|Required|A unique internal identifier for the control (e.g., "essay_response").|
|"prompt"|String|Required|The instructional text displayed above the text area (e.g., "Please justify your answer:").|

### Return/Output Value: The Retrieval Mechanism

The value entered by the user is retrieved using the syntax @TEXTAREA("name")@.

- Output Format: Returns the raw, multi-line string entered by the user.
    
- Technical Note on Empty States: If submitted without input, the command returns an empty string ("").
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow: The Pause-Submit-Resume Cycle

The TEXTAREA command orchestrates a state-synchronization event to ensure data persistence:

1. Parsing & Rendering: The system identifies the command in a visible turn ("show": true) and renders a multi-line text box in the Immersive view.
    
2. Automatic Submit Generation: The CAFA engine automatically appends a "Submit" button to the turn's output.
    
3. Execution Pause: The agent enters a "Waiting" state, halting all progress until the user intentionally commits the text block.
    
4. Data Commitment: Upon clicking "Submit," the engine captures the full text block and writes it to volatile memory under the key specified in the name argument.
    
5. Auto-Advance: The agent automatically transitions to the next turn in the prompts array.
    

### 4.2 Constraints and Implementation Patterns

- Rule of Uniqueness: Only one interactive input control is permitted per visible turn.
    
- The "Analytical Handoff" Pattern: A TEXTAREA turn is almost universally followed by an LLM-driven "Investigator" turn.
    

- Pattern: Turn 1 (TEXTAREA) -> Turn 2 (LLM analyzing @TEXTAREA("name")@).
    

## 5. Security & Sovereignty (Rule 9.1)

Makers must adhere to Rule 9.1 regarding PII when using TEXTAREA. Systems processing TEXTAREA input should include "sanitization" prompts in the subsequent LLM turn to prevent the leakage of sensitive data.

## 6. Reference

- Choi, J. (2025). TEXTAREA Command: Input Long Multi-Line Text Block. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    
---
# SELECT Command: Choose Option from Dropdown Menu

## 1. Metadata & Retrieval Keys

- Category: UI & User Interaction / Symbolic Input Controls
    
- Summary: Deterministically captures a single user selection from a predefined list of options presented as a dropdown menu within the CAFA Immersive interface. It functions as a space-optimized symbolic anchor, ideal for long lists of categories or identifiers, transforming human selection into structured, machine-readable data.
    
- RAG Keywords: SELECT, UI control, dropdown-menu, user-selection, input-form, user-interaction, symbolic-input, machine-readable-data, form-submission, execution-pause, deterministic-input, space-optimization, interaction-gate, cognitive-anchoring, human-in-the-loop, data-structuring, response-validation, ontological-commitment, UI-density, vertical-real-estate.
    
- Related Commands: RADIO (Visible single selection), CHECKBOX (Multi-selection), TEXT (Short input), TEXTAREA (Long input), MAP (Logic routing), INDEX (Parallel list lookup).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Space Optimization: Managing High-Density Ontologies

While the RADIO command is ideal for small sets of mutually exclusive options (typically 2–5), it becomes visually cumbersome as the number of choices increases. The SELECT command solves this "Vertical Real Estate" problem by utilizing a collapsed dropdown menu.

This allows the agent to present extensive ontologies—such as a list of 50 states, 20 departments, or a deep product catalog—without overwhelming the user's visual field or requiring excessive scrolling. It is the primary tool for "Clean Interface" design when the selection space is broad but only one choice is required.

### 2.2 Ontological Commitment in Structured Selection

Like all CAFA symbolic inputs, the SELECT command enforces Ontological Commitment. By requiring the user to choose from a fixed list, the agent prevents the high-entropy noise and "Context Drift" inherent in freeform text. It ensures that the symbol returned to the system is a valid key that has been pre-verified by the agent's maker, streamlining downstream logic and reducing the need for LLM-based error correction.

### 2.3 Execution Mode: Deterministic Symbolic Sovereignty

The command operates strictly as a Symbolic Turn. It bypasses the probabilistic nature of LLM interpretation to ensure that the user's choice is recorded with 100% fidelity. This level of "Selection Fidelity" is critical for data-driven workflows where the selected value is used as an exact lookup key for commands like MAP, INDEX, or GS (Google Sheets).

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax (Golden Template)

@SELECT("name", "prompt", "options")@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|name|String|Required|A unique internal identifier for the control (e.g., "course_selection"). This serves as the parameter key for all future retrieval and logic.|
|"prompt"|String|Required|The instructional text displayed immediately above the dropdown menu (e.g., "Please select your course:").|
|"options"|String|Required|A pipe-separated (`|

### Return/Output Value: The Retrieval Mechanism

The value selected by the user is retrieved using the syntax @SELECT("name")@.

- Output Format: Returns the raw string value of the selected option.
    

- Example: If the user selects "Physics", @SELECT("name")@ returns "Physics".
    

- Technical Note on Initial States: Most browsers default to the first item in the list. To ensure intentional selection, makers often implement the "Placeholder Pattern" described below.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow: The Pause-Submit-Resume Cycle

The SELECT command orchestrates the standard CAFA interaction lifecycle to ensure state synchronization:

1. Parsing & Rendering: The system identifies the command in a visible turn ("show": true) and renders a dropdown menu in the Immersive view.
    
2. Automatic Submit Generation: The CAFA engine automatically appends a "Submit" button to the turn's output. This ensures the data commitment is a discrete action.
    
3. Execution Pause (The Interaction Gate): The agent enters a "Waiting" state, halting all automated progression and pausing the session clock until the user intentionally clicks "Submit."
    
4. Data Commitment: Upon submission, the engine captures the selected string and writes it to volatile memory under the key specified in the name argument.
    
5. Auto-Advance: The agent "wakes up" and automatically transitions to the next turn in the prompts array.
    

### 4.2 Constraints and Implementation Patterns

- Rule of Uniqueness (The Single-Control Mandate): Only one interactive input control (SELECT, RADIO, TEXT, etc.) is permitted per visible turn.
    
- The "Placeholder" Best Practice: To avoid accidental submission of the first item, makers often include a generic first option (e.g., "Select one...|Option A|Option B"). A hidden logic turn then checks if the value equals "Select one..." and prompts the user to make a valid choice if necessary.
    
- Dynamic Routing: The result of a SELECT command is frequently used as a lookup key. For instance, after capturing a "Category" via SELECT, the agent can immediately use MAP to pull corresponding prices or descriptions from a parallel list.
    

## 5. Reference

- Choi, J. (2025). SELECT Command: Choose Option from Dropdown Menu. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# TTS Command: Output Audio via Text to Speech

## 1. Metadata & Retrieval Keys

- Category: UI & User Interaction / Multimodal Output
    
- Summary: Deterministically converts textual content into high-quality synthesized speech using advanced neural voice models. It serves as a multimodal bridge, providing auditory feedback that can be triggered manually via a UI button or executed automatically upon turn load to enhance accessibility, cognitive reinforcement, and user engagement.
    
- RAG Keywords: TTS, Text-to-Speech, Audio-Output, Accessibility, Speech-Synthesis, Voice-Model, User-Interaction, Speech-Interface, Auditory-Feedback, Multimodal-AI, Automated-Playback, Audio-UI, Voice-Persona, Nova, Shimmer, Onyx, Alloy, Echo, Fable, Whisper-Support, Multi-sensory-Learning, A11y, Inclusive-Design, Phonetic-Fidelity.
    
- Related Commands: RADIO (UI selection), TEXTAREA (Input capture), RUN (Orchestration), SAVE (Data persistence), MAP (Conditional logic).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Multimodal Engagement and Cognitive Reinforcement

In the CAFA ecosystem, the TTS command elevates the agent from a text-only interface to a Multimodal Assistant. By providing auditory reinforcement of visual text, the command supports multi-sensory learning, which has been shown to improve information retention and comprehension. It transforms static instructions into a dynamic, "living" dialogue, making the agent feel more human and reducing the cognitive load on the user during complex tasks.

### 2.2 Accessibility Optimization (A11y)

The TTS command is the primary technical tool for ensuring Inclusive Design. It is critical for users with visual impairments, reading difficulties (such as dyslexia), or those operating in "hands-busy" environments. By providing an auditory alternative to text, CAFA agents achieve a higher level of universal accessibility, adhering to the principle that intelligence should be consumable regardless of sensory limitations.

### 2.3 Execution Mode: Deterministic Symbolic Sovereignty

The command operates as a Symbolic Turn (⚙️). It ensures that the textual content is converted into speech with 100% fidelity to the source string. Because it bypasses generative processing during the playback phase, it maintains strict consistency between what the user sees on screen and what they hear, preserving the agent's Epistemological Integrity.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax (Golden Template)

@TTS("content", "caption", "voice")@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"content"|String|Required|The text to be converted to speech. Supports APs (e.g., "Hello @User@").|
|"caption"|String|Optional|Manual Mode: Providing text (e.g., "Listen") renders a button.<br><br>  <br><br>Auto Mode: Using an empty string ("") triggers playback on load.|
|"voice"|String|Optional|Specifies the voice model. Options: alloy, echo, fable, onyx, nova, shimmer. Defaults to nova.|

### Return/Output Value: The Retrieval Mechanism

The TTS command functions primarily as an output event rather than a data retrieval tool.

- Side-Effect: Initiates an audio stream request to the CAFA cloud. Depending on the caption argument, it either renders a UI button or triggers an immediate audio event.
    
- Output: Returns a success/failure status string to the Turn Result (@TR@).
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 UI Rendering and Playback Logic

The TTS command orchestrates two distinct interaction patterns based on the state of the caption argument:

1. Manual Trigger Mode (Button): If a non-empty string is provided (e.g., "Play Audio"), the CAFA engine renders a graphical button in the Immersive interface.
    

- Interaction Gate: Clicking the button initiates the playback. Like other input controls, clicking this button constitutes a "Submit" event that may advance the agent to the next turn if the turn configuration allows.
    

2. Automatic Playback Mode (Ambient): If the caption argument is an empty string (""), the audio stream is requested and initiated automatically as soon as the turn is rendered in the user's browser.
    

- UX Note: While powerful for greetings, makers should use Auto-Mode judiciously to avoid surprising users in quiet environments.
    

### 4.2 Constraints and Best Practices

- Rule of Uniqueness (The Single-Control Mandate): When TTS is used in Manual Mode (with a button), it is treated as an interactive UI element. Per CAFA standards, only one interactive command (e.g., RADIO, CHECKBOX, or a TTS button) should be present per visible turn to ensure deterministic submission logic.
    
- Language Support: Although the voice models are optimized for English, the system supports over 50 languages (including Arabic, Chinese, Japanese, and Spanish) following the OpenAI Whisper model's compatibility.
    
- Voice Selection: Architects should choose voices that align with the agent's persona. Use onyx for authoritative, formal roles and nova or shimmer for friendly, conversational assistants.
    

## 5. Reference

- Choi, J. (2025). TTS Command: Output Audio via Text to Speech. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# MATH Command: Specialized Symbolic Mathematical Operations

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / Mathematical Operations
    
- Summary: Executes domain-specific mathematical functions—ranging from precision rounding to advanced combinatorics and trigonometry—using a strict keyword-based syntax. It offers a deterministic, highly readable alternative to raw JavaScript evaluation for complex numerical logic, ensuring computational fidelity in assessment and simulation contexts.
    
- RAG Keywords: MATH, mathematical-operations, symbolic-calculation, rounding, combinatorics, trigonometry, geometry, numerical-precision, deterministic-computation, function-decomposition, ABS, CEIL, FLOOR, ROUND, POW, EXP, LOG, SQRT, SQFACTOR, PERM, COMB, FACTORIAL, LCM, GCF, DIST, MIN, MAX, SIN, COS, TAN.
    
- Related Commands: EVAL (General JS expressions), SET (Variable assignment), MAP (Logic routing), RANDOM (Stochastic generation), IF (Conditional branching).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 The Operational Friction: Complexity vs. Reliability

In complex agent modeling, developers often resort to the @EVAL() command to inject raw JavaScript for calculations. While flexible, this introduces significant risks: unreadable code, syntax errors, and unpredictable floating-point behavior. Calculating a permutation using raw JS (e.g., recursive factorial functions) inside a JSON string is brittle and prone to breakage.

The MATH command solves this by employing Functional Decomposition. It encapsulates complex, multi-step algorithms into reliable, atomic keywords (e.g., PERM, GCF). This ensures that the mathematical logic is not just "code," but a semantic declaration of intent, making the agent's ontology transparent and maintainable.

### 2.2 Theoretical Grounding: Computational Sovereignty and AIG

The MATH command is the engine of Automated Item Generation (AIG) within the Trinity of Assessment (ToA). To generate valid assessment items on the fly, an agent must possess Computational Sovereignty—the ability to mathematically verify its own content.

- Ontological Bridge: By providing robust tools for Number Theory (LCM, GCF, SQFACTOR) and Combinatorics (COMB), MATH allows agents to bridge the gap between "Generative Text" and "Mathematical Truth." An agent can generate a word problem about "grouping students" and simultaneously calculate the exact number of possible groups using @MATH("COMB", ...) to validate the student's answer forensically.
    

### 2.3 Execution Mode: The Symbolic Shield

Symbolic Turn (⚙️). The MATH command operates as a "Symbolic Shield" against LLM hallucinations. Large Language Models are notoriously poor at arithmetic and complex calculation. By offloading these tasks to the deterministic CAFA engine, the agent ensures 100% computational fidelity. The LLM is then used only to describe the result, not to derive it.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax (Golden Template)

@MATH("function_name", "arg1"[, "arg2", ...])@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"function_name"|String|Required|The case-sensitive keyword of the operation (e.g., "ROUND", "PERM", "SIN").|
|"arg1"|Number/String|Required|The primary numerical input (e.g., "105", "@SCORE@"). Must resolve to a valid number.|
|"arg2..."|Number/String|Conditional|Secondary inputs (e.g., decimal places for ROUND, r selection for COMB).|

### Return/Output Value

- Output: Returns a single numerical string representing the calculated result.
    
- Error Handling: Returns NaN (Not a Number) if inputs are invalid or outside the function's domain (e.g., SQRT(-1)).
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Functional Domains and Logic

1. Precision Control:
    

- ROUND(n, [d]):
    

- If d > 0: Rounds to d decimal places (e.g., currency).
    
- If d < 0: Rounds to the nearest $10^{|d|}$ (e.g., -2 rounds to nearest hundred).
    

- ABS(n), CEIL(n), FLOOR(n): Standard absolute and integer rounding.
    

2. Growth & Decay:
    

- POW(base, exp), EXP(n), SQRT(n): Modeling exponential curves.
    
- LOG(n) (Natural), LOG10(n) (Base-10): Inverse exponential calculations.
    
- SQFACTOR(n): Returns the largest perfect square factor (critical for simplifying radicals).
    

3. Combinatorics (AIG Core):
    

- PERM(n, r): Calculates $P(n,r)$ ($n \ge r \ge 0$).
    
- COMB(n, r): Calculates $C(n,r)$ ($n \ge r \ge 0$).
    
- FACTORIAL(n), LCM(a,b), GCF(a,b): Number theory foundations.
    

4. Geometry & Trig:
    

- DIST(x1, y1, x2, y2): Euclidean distance ($\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$).
    
- SIN(rad), COS(rad), TAN(rad): Requires Radians.
    

### 4.2 Critical Constraint: Radian Conversion

All trigonometric functions in the MATH command accept inputs in Radians, not Degrees. Architects must perform conversion using EVAL before execution.

- Correct Pattern: @MATH("SIN", "@EVAL("@ANGLE@ * Math.PI / 180")@")@
    

### 4.3 Implementation Patterns

#### Pattern A: Dynamic Item Generation (AIG)

Calculating combinations for a probability question stem:

{  
  "user": "/ T1: Calculate groups.\n@SET("Ways", "@MATH("COMB", "@STUDENT_COUNT@", "3")@")@",  
  "show": false  
}  
  

#### Pattern B: Psychometric Scoring (Significant Figures)

Rounding a raw score of 12345 to the nearest hundred (12300) for reporting:

{  
  "user": "/ T2: Round to nearest 100.\n@SET("ReportScore", "@MATH("ROUND", "@RAW_SCORE@", "-2")@")@",  
  "show": false  
}  
  

## 5. Reference

- Choi, J. (2025). MATH Command. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# FR Command: Format Fraction for Display Output and Arithmetic

## 1. Metadata & Retrieval Keys

- Category: UI & Visualization / Mathematical Operations
    
- Summary: A comprehensive suite of commands for handling symbolic fraction arithmetic and formatting. It manages the internal numerator|denominator string representation to ensure computational precision and renders high-quality LaTeX output for educational assessment (AIG).
    
- RAG Keywords: FR, Fraction, LaTeX-Display, MathOutput, Formatting, Arithmetic, FRADD, FRSUB, FRMULT, FRDIV, FRREC, FRVAL, SIMPLIFY, AIG, Automated-Item-Generation, Mixed-Number, Improper-Fraction, Precision-Math, Floating-Point-Avoidance.
    
- Related Commands: MATH (General math), EVAL (JS Evaluation), SET (Variable assignment).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 The Floating-Point Problem in Assessment

In standard computing, numbers are treated as floating-point decimals (e.g., $1/3$ becomes $0.333333...$). In educational assessment, however, "0.33" is distinct from "1/3". The FR command suite solves this by treating fractions as Symbolic Objects (strings in the format "num|den"). This allows the agent to perform exact arithmetic (LCM calculation, cross-multiplication) without precision loss, ensuring that the generated math problems remain pedagogically valid.

### 2.2 Pedagogical Rendering Control

The FR command is the bridge between calculation and display. It translates the internal pipe-separated string into standard LaTeX syntax. Crucially, it offers granular control over the pedagogical presentation—allowing an agent to display an unsimplified "Original" fraction ($6/4$) to teach simplification, or a "Display" size fraction ($\dfrac{3}{2}$) for readability.

## 3. Formal Syntax & Parameter Schema (The "What")

### 3.1 Core Display Command

@FR("fraction_string"[, "options"])@  
  

### 3.2 Argument Table (FR)

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"fraction_string"|String|Required|The fraction to format, structured strictly as `"numerator|
|"options"|String|Optional|Flags to control output:<br><br>  <br><br>"o": Original (No simplify). Precedence over m.<br><br>  <br><br>"d": Display mode (\dfrac). Recommended for visibility.<br><br>  <br><br>"m": Mixed number conversion (e.g., $3/2 \to 1\frac{1}{2}$).|

### 3.3 Arithmetic & Utility Functions

These commands perform logic on fraction strings and return a new fraction string ("n|d"). They are designed to be nested inside @FR(...)@ or @SET(...)@.

|   |   |   |   |
|---|---|---|---|
|Command|Syntax|Output Format|Description|
|FRADD|@FRADD("fr1", "fr2")@|`"num|den"`|
|FRSUB|@FRSUB("fr1", "fr2")@|`"num|den"`|
|FRMULT|@FRMULT("fr1", "fr2")@|`"num|den"`|
|FRDIV|@FRDIV("fr1", "fr2")@|`"num|den"`|
|FRREC|@FRREC("fr")@|`"den|num"`|
|FRVAL|@FRVAL("fr")@|Number|Critical: Returns the actual decimal value (e.g., 0.5) for numerical comparison.|
|SIMPLIFY|@SIMPLIFY("fr")@|`"num|den"`|

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Representation

The CAFA engine processes fractions as strings to prevent auto-evaluation.

- Input: "1|2" (String)
    
- Process: Parsed into {n: 1, d: 2} objects for arithmetic.
    
- Output: Re-serialized to "1|2" (String) or LaTeX \frac{1}{2}.
    

### 4.2 The "Chaining" Pattern (AIG Workflow)

To generate a math problem, calculate the answer, and display it, commands are nested.

- Goal: Create an addition problem: $\frac{1}{3} + \frac{1}{6}$
    
- Code: @FR(@FRADD("1|3", "1|6")@, "d")@
    
- Flow: 1. FRADD finds LCM(3,6)=6 $\to$ calculates $2/6 + 1/6$ $\to$ returns string "3|6".  
    2. FR receives "3|6", simplifies to $1/2$, and renders \dfrac{1}{2}.
    

### 4.3 Display Options Precedence

1. "o" (Original): Dominant flag. Prevents simplification. Used for showing intermediate steps (e.g., "3|6" displays as $\frac{3}{6}$).
    
2. "m" (Mixed): Converts improper fractions (e.g., "3|2" $\to 1\frac{1}{2}$). Only applies if simplification is allowed.
    
3. "d" (Display): Forces \dfrac rendering for larger vertical height. Can be combined with o or m.
    

## 5. Reference

- Choi, J. (2025). FR Command: Format Fraction for Display Output and Arithmetic. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# FRADD Command: Symbolic Fraction Addition

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / Mathematical Operations
    
- Summary: Performs symbolic addition of two fraction strings. It internally calculates the Least Common Multiple (LCM) of the denominators to ensure arithmetic correctness, sums the adjusted numerators, simplifies the result, and returns a formatted "num|den" string.
    
- RAG Keywords: FRADD, fraction-addition, symbolic-math, LCM, least-common-multiple, common-denominator, arithmetic-operation, fraction-string, numerator-summation, pedagogical-accuracy, floating-point-avoidance, automated-simplification, AIG, math-logic.
    
- Related Commands: FR (Display wrapper), FRSUB (Inverse operation), FRMULT (Multiplication), FRVAL (Decimal conversion), MATH (General math).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 The Common Denominator Problem

In standard programming, adding 1/3 + 1/6 results in a floating-point approximation (0.5). While numerically correct, this destroys the pedagogical structure of the problem. To teach or assess math, an agent must "think" like a student: finding a common denominator. FRADD solves this by internally computing the LCM of the denominators, adjusting the numerators proportionally, and then summing them. This ensures that the result is derived through standard arithmetic rules rather than binary approximation.

### 2.2 Pedagogical Fidelity

By preserving the fraction structure throughout the operation ("1|3" + "1|6" $\to$ "3|6" $\to$ "1|2"), the agent maintains Pedagogical Fidelity. This allows the system to generate complex multi-step problems (e.g., partial credit logic) where intermediate fractional states are tracked and validated.

### 2.3 Execution Mode

Symbolic Turn (⚙️). A deterministic calculation that modifies string data in volatile memory without LLM intervention.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax (Golden Template)

@FRADD("fr1", "fr2")@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"fr1"|String|Required|The first addend, formatted as `"num|
|"fr2"|String|Required|The second addend, formatted as `"num|

### Return/Output Value

- Format: Returns a single string strictly formatted as "numerator|denominator".
    
- State: The returned fraction is automatically simplified to its lowest terms.
    
- Example: @FRADD("1|4", "1|4")@ returns "1|2" (not "2|4").
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow

1. Parsing: The engine deserializes "fr1" and "fr2" into integer pairs $(n_1, d_1)$ and $(n_2, d_2)$.
    
2. LCM Calculation: It computes $L = \text{LCM}(d_1, d_2)$.
    
3. Normalization: It scales the numerators: $n_{1}' = n_1 \times (L / d_1)$ and $n_{2}' = n_2 \times (L / d_2)$.
    
4. Summation: It calculates the sum: $N_{sum} = n_{1}' + n_{2}'$.
    
5. Simplification: It reduces the resulting fraction $\frac{N_{sum}}{L}$ by dividing both by their Greatest Common Factor (GCF).
    
6. Serialization: The result is returned as "num|den".
    

### 4.2 Implementation Pattern: The Display Chain

FRADD does not render LaTeX. It produces a data string. To display the result to a user, it must be wrapped in the FR command.

Scenario: Generate a question asking for the sum of two variables.

{  
  "user": "/ Display the problem and the answer.\nCalculate: @FR("@A@", "d")@ + @FR("@B@", "d")@\n\nAnswer: @FR(@FRADD("@A@", "@B@")@, "d")@",  
  "show": true  
}  
  

Logic: If @A@="1|3" and @B@="1|6", the user sees: "Calculate: $\dfrac{1}{3} + \dfrac{1}{6}$ ... Answer: $\dfrac{1}{2}$".

## 5. Reference

- Choi, J. (2025). FRADD Command: Symbolic Fraction Addition. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# FRMULT Command: Symbolic Fraction Multiplication

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / Mathematical Operations
    
- Summary: Performs symbolic multiplication of two fraction strings. It executes the arithmetic operation by multiplying the numerators and denominators independently, simplifies the resulting fraction to its lowest terms, and returns a formatted "num|den" string.
    
- RAG Keywords: FRMULT, fraction-multiplication, symbolic-math, product-calculation, arithmetic-operation, fraction-string, numerator-product, denominator-product, pedagogical-accuracy, floating-point-avoidance, automated-simplification, AIG, math-logic, cross-multiplication.
    
- Related Commands: FR (Display wrapper), FRDIV (Inverse operation), FRADD (Addition), FRSUB (Subtraction), FRREC (Reciprocal), FRVAL (Decimal conversion).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 The Floating-Point Precision Trap

In standard binary computing, multiplying fractions often results in precision loss (e.g., $1/3 \times 3$ might resolve to $0.99999...$ rather than exactly $1$). FRMULT avoids this by treating fractions as Symbolic Objects. It adheres to the strict arithmetic rule $\frac{a}{b} \times \frac{c}{d} = \frac{a \times c}{b \times d}$, performing integer multiplication on the components to ensure the result is mathematically exact.

### 2.2 Pedagogical Fidelity

By maintaining the fraction structure ("2|3" $\times$ "3|4" $\to$ "6|12" $\to$ "1|2"), the agent preserves the intermediate states often required for educational feedback. This is essential for Automated Item Generation (AIG) where the system must show "step-by-step" solutions for area calculations or probability problems.

### 2.3 Execution Mode

Symbolic Turn (⚙️). A deterministic calculation that modifies string data in volatile memory without LLM intervention.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax (Golden Template)

@FRMULT("fr1", "fr2")@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"fr1"|String|Required|The first factor, formatted as `"num|
|"fr2"|String|Required|The second factor, formatted as `"num|

### Return/Output Value

- Format: Returns a single string strictly formatted as "numerator|denominator".
    
- State: The returned fraction is automatically simplified to its lowest terms.
    
- Example: @FRMULT("2|3", "3|4")@ returns "1|2" (derived from $6/12$).
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow

1. Parsing: The engine deserializes "fr1" and "fr2" into integer pairs $(n_1, d_1)$ and $(n_2, d_2)$.
    
2. Component Multiplication: * New Numerator: $N_{prod} = n_1 \times n_2$
    

- New Denominator: $D_{prod} = d_1 \times d_2$
    

3. Simplification: It reduces the resulting fraction $\frac{N_{prod}}{D_{prod}}$ by dividing both components by their Greatest Common Factor (GCF).
    
4. Serialization: The result is returned as "num|den".
    

### 4.2 Implementation Pattern: Area Calculation

To generate a geometry problem asking for the area of a rectangle with fractional sides:

{  
  "user": "/ Problem Generation Turn.\nCalculate Area: Length = @FR("@L@", "d")@, Width = @FR("@W@", "d")@\n\nArea = @FR(@FRMULT("@L@", "@W@")@, "d")@",  
  "show": true  
}  
  

Logic: If @L@="1|2" and @W@="1|3", the output is: "Calculate Area: Length = $\dfrac{1}{2}$, Width = $\dfrac{1}{3}$ ... Area = $\dfrac{1}{6}$".

## 5. Reference

- Choi, J. (2025). FRMULT Command: Symbolic Fraction Multiplication. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# FRDIV Command: Symbolic Fraction Division

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / Mathematical Operations
    
- Summary: Performs symbolic division of two fraction strings. It executes the operation by multiplying the first fraction (dividend) by the reciprocal of the second fraction (divisor), effectively modeling the "Invert and Multiply" algorithm to ensure arithmetic correctness without floating-point conversion.
    
- RAG Keywords: FRDIV, fraction-division, symbolic-math, reciprocal-multiplication, invert-and-multiply, arithmetic-operation, fraction-string, quotient-calculation, pedagogical-accuracy, floating-point-avoidance, automated-simplification, AIG, math-logic, complex-fractions.
    
- Related Commands: FR (Display wrapper), FRMULT (Inverse operation), FRREC (Reciprocal utility), FRADD (Addition), FRSUB (Subtraction), FRVAL (Decimal conversion).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 The "Invert and Multiply" Paradigm

In standard binary computing, division is a destructive operation that converts rational numbers into floating-point approximations (e.g., $1/3 \div 1/6$ becomes 2.0 rather than the integer 2 or fraction 2/1). FRDIV avoids this by treating fractions as Symbolic Objects. It strictly adheres to the arithmetic rule $\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \times \frac{d}{c}$. By converting division into multiplication by the reciprocal, it ensures the result remains a precise rational number.

### 2.2 Pedagogical Fidelity

By explicitly modeling the "Invert and Multiply" step ("6|5" $\div$ "8|15" $\to$ "6|5" $\times$ "15|8" $\to$ "90|40" $\to$ "9|4"), the agent preserves the logical progression required for educational explanations. This is essential for Automated Item Generation (AIG) where the system must generate step-by-step solutions for algebra or ratio problems.

### 2.3 Execution Mode

Symbolic Turn (⚙️). A deterministic calculation that modifies string data in volatile memory without LLM intervention.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax (Golden Template)

@FRDIV("fr1", "fr2")@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"fr1"|String|Required|The Dividend (the number being divided), formatted as `"num|
|"fr2"|String|Required|The Divisor (the number dividing by), formatted as `"num|

### Return/Output Value

- Format: Returns a single string strictly formatted as "numerator|denominator".
    
- State: The returned fraction is automatically simplified to its lowest terms.
    
- Example: @FRDIV("6|5", "8|15")@ returns "9|4" (derived from $90/40$).
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow

1. Parsing: The engine deserializes "fr1" and "fr2" into integer pairs $(n_1, d_1)$ and $(n_2, d_2)$.
    
2. Reciprocal Inversion: The engine effectively swaps the numerator and denominator of the divisor: $fr2' = d_2 / n_2$.
    
3. Cross-Multiplication: * New Numerator: $N_{quot} = n_1 \times d_2$
    

- New Denominator: $D_{quot} = d_1 \times n_2$
    

4. Simplification: It reduces the resulting fraction $\frac{N_{quot}}{D_{quot}}$ by dividing both components by their Greatest Common Factor (GCF).
    
5. Serialization: The result is returned as "num|den".
    

### 4.2 Implementation Pattern: Ratio Problems

To generate a problem asking for the unit rate:

{  
  "user": "/ Problem Generation Turn.\nCalculate Unit Rate: Distance = @FR("@DIST@", "d")@ miles, Time = @FR("@TIME@", "d")@ hours.\n\nRate = @FR(@FRDIV("@DIST@", "@TIME@")@, "d")@ mph",  
  "show": true  
}  
  

Logic: If @DIST@="3|2" (1.5 miles) and @TIME@="1|4" (15 mins), the output is: "Rate = $\dfrac{3}{2} \div \dfrac{1}{4}$ ... Rate = 6 mph".

## 5. Reference

- Choi, J. (2025). FRDIV Command: Symbolic Fraction Division. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# FRREC Command: Symbolic Fraction Reciprocal

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / Mathematical Operations
    
- Summary: Symbolically inverts a fraction string by swapping its numerator and denominator to produce its multiplicative inverse (reciprocal). Used internally by division operations and explicitly for algebraic proofs.
    
- RAG Keywords: FRREC, fraction-reciprocal, multiplicative-inverse, numerator-denominator-swap, symbolic-inversion, fraction-flipping, division-logic, algebraic-identity, arithmetic-utility, pedagogical-step, inverse-operation.
    
- Related Commands: FRDIV (Dependent command), FRMULT (Companion operation), FR (Display wrapper).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Defining Division via Multiplication

In symbolic mathematics, division is operationally defined as multiplication by the reciprocal. FRREC provides the structural mechanism to generate the $\frac{1}{b}$ term, allowing agents to explicitly model the "flip" step in algorithms.

### 2.2 Algebraic Identity Verification

Essential for generating items that test the Multiplicative Inverse Property ($x \cdot \frac{1}{x} = 1$).

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax (Golden Template)

@FRREC("fraction_string")@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"fraction_string"|String|Required|The input fraction to invert, formatted as `"num|

### Return/Output Value

- Format: Returns a single string formatted as "denominator|numerator".
    
- Example: @FRREC("3|2")@ returns "2|3".
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow

1. Parsing: Deserializes input into $n$ and $d$.
    
2. Inversion: Swaps components: $n_{new} = d$, $d_{new} = n$.
    
3. Serialization: Returns "n_new|d_new".
    

## 5. Reference

- Choi, J. (2025). FRREC Command: Symbolic Fraction Reciprocal. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---

# FRVAL Command: Convert Symbolic Fraction to Decimal Value

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / Mathematical Operations
    
- Summary: Converts a symbolic fraction string ("num|den") into a standard floating-point decimal number. This command is the primary bridge between the symbolic fraction engine and the general-purpose numerical logic of the agent (e.g., for sorting, threshold comparisons, or non-fractional grading).
    
- RAG Keywords: FRVAL, fraction-value, decimal-conversion, symbolic-to-numeric, floating-point-evaluation, fraction-magnitude, arithmetic-bridge, numerical-comparison, threshold-check, decimal-grading, numerator-denominator-division.
    
- Related Commands: FR (Symbolic display), MATH (Numerical operations), EVAL (JS logic), FRADD (Symbolic arithmetic source).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 The Symbolic-Numeric Bridge

While FRADD and FRMULT maintain precision by keeping fractions as strings ("1|3"), many downstream operations require numerical values. For example, sorting a list of fractions by size, checking if a result is greater than 0.5, or graphing a data point requires a standard float. FRVAL serves as the deterministic converter, performing the division $numerator \div denominator$ to produce a consumable number.

### 2.2 Grading Flexibility

In assessment, a student might enter a decimal answer ($0.5$) for a problem calculated symbolically as $1/2$. FRVAL allows the agent to grade these equivalent forms by converting the internal symbolic truth into a decimal for comparison against user input.

### 2.3 Execution Mode

Symbolic Turn (⚙️). A deterministic calculation that executes instantly in volatile memory.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax (Golden Template)

@FRVAL("fraction_string")@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"fraction_string"|String|Required|The input fraction to convert, formatted as `"numerator|

### Return/Output Value

- Format: Returns a standard JavaScript Number (float).
    
- Example: @FRVAL("3|4")@ returns 0.75.
    
- Precision: Subject to standard IEEE 754 floating-point precision limits.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow

1. Parsing: The engine deserializes the input string into integers $n$ (numerator) and $d$ (denominator).
    
2. Division: It performs the floating-point division operation: $result = n / d$.
    
3. Return: The resulting number is returned to the context.
    

### 4.2 Implementation Pattern: Numerical Comparison

To check if a calculated fraction is greater than a threshold:

{  
  "user": "/ Check Threshold.\n@SET("Result", "5|8")@\n@SET("IsPassing", "@EVAL(@FRVAL("@Result@")@ > 0.5)@")@",  
  "show": false  
}  
  

Logic: 1. Result is "5|8".

2. FRVAL("5|8") returns 0.625.

3. EVAL(0.625 > 0.5) returns true.

## 5. Reference

- Choi, J. (2025). FRVAL Command: Convert Symbolic Fraction to Decimal Value. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# POLY Command: Format and Display Polynomials

## 1. Metadata & Retrieval Keys

- Category: UI & Visualization / Mathematical Operations
    
- Summary: Transforms a raw list of coefficients into a professionally formatted LaTeX polynomial string. It automates algebraic notation logic—suppressing zero terms, hiding unity coefficients, handling negative signs, and managing variable substitution—to ensure clean, pedagogical output for both standard and sparse polynomials.
    
- RAG Keywords: POLY, POLYDISP, polynomial-display, coefficient-list, algebraic-formatting, LaTeX-math, math-visualization, symbolic-representation, automated-item-generation, sparse-polynomials, AIG, degree-inference, monomial-rendering, variable-substitution, binomial-expansion, empty-coefficient-handling.
    
- Related Commands: POLYEVAL (Evaluation), POLYDIFF (Calculus), POLYADD (Arithmetic), MATH (General math).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 The Formatting Friction

In programmatic math generation, rendering a polynomial from data often results in messy strings like 1x^2 + -1x + 0. Cleaning this requires complex conditional logic. POLY abstracts this, allowing the developer to provide a simple data structure ("1|-1|0") while the engine generates the polished LaTeX (x^2 - x).

### 2.2 Data-Driven Representation

CAFA treats polynomials as Coefficient Lists. POLY acts as the View Layer, translating this internal data format into a human-readable expression without altering the underlying data. It specifically handles Sparse Polynomials efficiently; developers can use empty pipes (||) to denote zeros, compressing the data string for high-degree functions.

### 2.3 Execution Mode

Symbolic Turn (⚙️). A deterministic string manipulation operation.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax (Golden Templates)

Standard LaTeX Output:

@POLY("coeff"[, "terms"[, "degrees"]])@  
  

Display Mode (Wrapped in $...$):

@POLYDISP("coeff"[, "terms"[, "degrees"]])@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"coeff"|String|Required|Pipe-separated list of coefficients (e.g., `"1|
|"terms"|String|Optional|The variable(s) to use. Defaults to "x". Can be complex expressions like "(a+b)" or lists `"x|
|"degrees"|String|Optional|Explicit list of powers. If omitted, degrees are inferred in descending order (e.g., `2|

### Return/Output Value

- @POLY: Returns raw LaTeX string (e.g., x^2 + 2x + 3).
    
- @POLYDISP: Returns LaTeX string wrapped in math delimiters (e.g., $x^2 + 2x + 3$).
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Formatting Rules

1. Zero/Empty Handling: Terms with 0 or empty || in the coeff string are omitted from the output.
    
2. Unity Coefficients: Coefficients of 1 or -1 are hidden (e.g., x instead of 1x), except for the constant term.
    
3. Variable Cycling: If multiple terms are provided ("x|y"), they are applied cyclically or mapped to specific positions depending on the degree structure.
    

### 4.2 Implementation Patterns

Pattern A: Sparse Polynomial (Missing Terms)

{  
  "user": "/ Display x^4 - 1.\n@POLYDISP("1|0|0|0|-1")@",  
  "show": true  
}  
  

Output: $x^4 - 1$

Pattern B: Binomial Expansion (Complex Terms)

{  
  "user": "/ Expansion of (a+b)^2.\n@POLYDISP("1|2|1", "(a+b)", "2|1|0")@",  
  "show": true  
}  
  

Output: $(a+b)^2 + 2(a+b) + 1$

## 5. Reference

- Choi, J. (2025). POLY Command: Format and Display Polynomials. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
# POLYDISP Command: Display Polynomial in Math Mode

## 1. Metadata & Retrieval Keys

- Category: UI & Visualization / Mathematical Operations
    
- Summary: A wrapper command for POLY that automatically encapsulates the formatted polynomial string within LaTeX math delimiters ($...$). It simplifies the code required to render polynomials directly in the user interface, ensuring immediate visual formatting.
    
- RAG Keywords: POLYDISP, polynomial-display, LaTeX-wrapper, math-mode, algebraic-formatting, symbolic-rendering, equation-display, simplified-syntax, visualization-shortcut, automated-delimiters, direct-ui-injection.
    
- Related Commands: POLY (Core formatter), POLYEVAL (Evaluation), POLYDIFF (Calculus).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 The "Display" Shortcut

While @POLY(...)@ generates the raw LaTeX string (e.g., x^2 + 1), displaying this to a user requires manual wrapping: $@POLY(...)@$. POLYDISP automates this encapsulation. It is architected for Direct UI Injection, allowing developers to write cleaner, less error-prone prompt strings when the goal is immediate visualization rather than intermediate string manipulation.

### 2.2 Execution Mode

Symbolic Turn (⚙️). A deterministic string manipulation operation that executes instantly in volatile memory.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax (Golden Template)

@POLYDISP("coeff"[, "terms"[, "degrees"]])@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"coeff"|String|Required|Pipe-separated list of coefficients (e.g., `"1|
|"terms"|String|Optional|The variable(s) to use. Defaults to "x".|
|"degrees"|String|Optional|Explicit list of powers.|

### Return/Output Value

- Format: Returns a LaTeX string wrapped in $ delimiters.
    
- Example: @POLYDISP("1|2")@ returns $x + 2$.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow

1. Inheritance: The command passes all arguments directly to the internal POLY engine.
    
2. Formatting: The engine generates the raw LaTeX string.
    
3. Encapsulation: The system appends $ to the start and end of the string.
    
4. Return: The final string is output to the turn context.
    

### 4.2 Implementation Pattern: Equation Rendering

{  
  "user": "/ Display the quadratic equation.\nf(x) = @POLYDISP("1|-5|6")@",  
  "show": true  
}  
  

Output: $f(x) = x^2 - 5x + 6$

## 5. Reference

- Choi, J. (2025). POLYDISP Command: Display Polynomial in Math Mode. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    
---
# POLYDIFF Command: Symbolic Polynomial Differentiation

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / Mathematical Operations
    
- Summary: Calculates the symbolic derivative $f'(x)$ of a polynomial defined by a coefficient list. It applies the Power Rule to every term, returning a new coefficient string that can be immediately displayed or evaluated.
    
- RAG Keywords: POLYDIFF, symbolic-differentiation, derivative, calculus, power-rule, f'(x), rate-of-change, slope-calculation, coefficient-transformation, chainable-calculus, AIG-calculus, polynomial-derivative.
    
- Related Commands: POLYINT (Inverse operation), POLYEVAL (Gradient calculation), POLY (Display), POLYDISP (Visual wrapper).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Chainable Calculus

In AIG (Automated Item Generation), creating calculus problems requires more than just displaying a static equation. The agent must know the derivative to grade the answer. POLYDIFF allows the agent to generate a random function ($f(x)$) and mathematically derive $f'(x)$ in the background using the same coefficient structure. This output can be nested: @POLYEVAL(@POLYDIFF("@COEFF@")@, "2")@ calculates the slope of the tangent at $x=2$.

### 2.2 Execution Mode

Symbolic Turn (⚙️). A deterministic calculation that transforms an array of length $N$ to length $N-1$ (typically).

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax (Golden Template)

@POLYDIFF("coeff")@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"coeff"|String|Required|The coefficient list of the original polynomial $f(x)$.|

### Return/Output Value

- Format: Returns a pipe-separated string of coefficients for $f'(x)$.
    
- Dimensionality: If the input degree is $n$, the output degree is $n-1$.
    
- Example: @POLYDIFF("1|0|-4")@ ($x^2 - 4$) returns "2|0" ($2x$).
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow

1. Parsing: Deserializes "coeff" into $[c_n, c_{n-1}, \dots, c_0]$.
    
2. Power Rule Application: Iterates through terms. For a term $c \cdot x^p$:
    

- New Coefficient $c' = c \times p$.
    
- New Power $p' = p - 1$.
    

3. Constant Elimination: The term with power 0 is dropped (derivative of a constant is 0).
    
4. Serialization: Returns the new list.
    

### 4.2 Implementation Pattern: Tangent Line

{  
  "user": "/ Calculate slope at x=3.\nSlope = @POLYEVAL(@POLYDIFF("1|0|0")@, "3")@",  
  "show": true  
}  
  

Logic: $f(x)=x^2$. $f'(x)=2x$. $f'(3)=6$.

## 5. Reference

- Choi, J. (2025). POLYDIFF Command: Symbolic Polynomial Differentiation. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    
---

# POLYINT Command: Compute Symbolic Integral of Polynomial

## 1. Metadata & Retrieval Keys

- Category: Logic & Flow Control / Mathematical Operations
    
- Summary: Performs symbolic integration on a polynomial coefficient list. It supports two modes: calculating the Indefinite Integral (returning a new coefficient string representing the antiderivative) and calculating the Definite Integral (returning a numerical value representing the area under the curve between two limits).
    
- RAG Keywords: POLYINT, symbolic-integration, antiderivative, definite-integral, indefinite-integral, area-under-curve, reverse-power-rule, calculus, accumulation, fundamental-theorem-of-calculus, AIG-calculus, coefficient-transformation, chainable-math, degree-expansion.
    
- Related Commands: POLYDIFF (Inverse operation), POLYEVAL (Evaluation), POLY (Display), POLYDISP (Visual wrapper).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 Chainable Calculus Workflow

In the CAFA architecture, calculus commands are designed to be composable. Because POLYINT (in indefinite mode) returns a Coefficient List rather than a static text string, the result can be immediately fed into other commands.

- Example: An agent can generate a random acceleration function $a(t)$, integrate it to find velocity $v(t) = \int a(t)dt$, and then integrate again to find position $s(t) = \int v(t)dt$, all within a single symbolic turn sequence without manual intervention.
    

### 2.2 The "Area" Utility

For educational assessment, calculating the specific area under a curve (Definite Integral) is a frequent requirement. POLYINT automates the Fundamental Theorem of Calculus ($F(b) - F(a)$), allowing the agent to generate valid "Find the Area" problems dynamically with guaranteed correct answer keys.

### 2.3 Execution Mode

Symbolic Turn (⚙️). A deterministic calculation that transforms mathematical arrays in volatile memory.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax (Golden Template)

@POLYINT("coeff"[, "x1", "x2"])@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"coeff"|String|Required|The coefficient list of the polynomial to be integrated (e.g., `"3|
|"x1"|Number|Optional|The lower limit of integration ($a$).|
|"x2"|Number|Optional|The upper limit of integration ($b$).|

### Return/Output Value

- Mode A (Indefinite): If x1 and x2 are omitted, returns a Pipe-Separated String of coefficients for the antiderivative.
    

- Degree Change: Input array length $N$ becomes output length $N+1$.
    
- Constant: The constant of integration ($C$) is mathematically treated as 0 (the last element of the returned list).
    

- Mode B (Definite): If x1 and x2 are provided, returns a single Number (Float/Integer) representing the calculated area.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow

1. Parsing: Deserializes "coeff" into terms. Empty slots || are treated as 0.
    
2. Reverse Power Rule: For each term $c \cdot x^p$, calculates the new term $\frac{c}{p+1} x^{p+1}$.
    

- Example: Input 3 (coeff for $x^2$) becomes 3/(2+1) = 1 (coeff for $x^3$).
    

3. Degree Expansion: The array length increases by 1 to accommodate the integration constant (set to 0).
    
4. Mode Check:
    

- Indefinite: Returns the new array as a string.
    
- Definite: Calculates $F(x2)$ and $F(x1)$ using the new array logic, then returns the scalar $F(x2) - F(x1)$.
    

### 4.2 Implementation Pattern: Definite Integral Problem

Generating a problem to find the area under $f(x) = 3x^2$ from $x=1$ to $x=3$.

{  
  "user": "/ Define Function and Limits.\n@SET("FUNC", "3|0|0")@\n@SET("A", "1")@\n@SET("B", "3")@\n\n/ Display Problem.\nCalculate the area: $\\int_{@A@}^{@B@} (@POLY("@FUNC@")@) dx$\n\n/ Calculate Answer Key.\nAnswer: @POLYINT("@FUNC@", "@A@", "@B@")@",  
  "show": true  
}  
  

Logic:

1. Integrates $3x^2 \to x^3$.
    
2. Evaluates at 3: $3^3 = 27$.
    
3. Evaluates at 1: $1^3 = 1$.
    
4. Result: $27 - 1 = 26$.
    

## 5. Reference

- Choi, J. (2025). POLYINT Command: Compute Symbolic Integral of Polynomial. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    
---
# MERMAID Command: Render Flowcharts and Diagrams Code

## 1. Metadata & Retrieval Keys

- Category: UI & Visualization / Data Representation
    
- Summary: A symbolic command that deterministically renders raw Mermaid diagram syntax into interactive, vector-based visual diagrams (flowcharts, sequence diagrams, pie charts) within the CAFA agent interface. It acts as the deterministic "Visual Cortex" for the agent, converting text-based logic into graphical structures.
    
- RAG Keywords: MERMAID, visualization, flowchart, diagram-rendering, sequence-diagram, pie-chart, gantt-chart, code-to-image, process-mapping, IMPACT-framework, symbolic-rendering, deterministic-display, diagram-syntax, visual-communication, hybrid-AI, GAMER-loop, visual-sovereignty, vector-graphics, SVG-generation.
    
- Related Commands: SAVE (Code persistence), RUN (Process generation), TEXTAREA (Code input), SET (Dynamic string building).
    

## 2. Architectural Logic & Rationale (The "Why")

### 2.1 The Hybrid AI Visualization Pipeline

Standard LLMs are excellent at generating code (logic) but struggle to natively generate images (pixels) containing precise text. The MERMAID command bridges this gap by acting as a deterministic rendering engine. It enables a Hybrid Workflow:

1. Generative Phase (LLM): The AI writes the Mermaid syntax (e.g., graph TD; A-->B;) based on a user's natural language request.
    
2. Symbolic Phase (Engine): The MERMAID command takes that raw text and compiles it into a visual graphic.  
    This separation ensures Visual Sovereignty: the diagram logic is flexible (AI-driven), but the rendering is pixel-perfect and readable (Engine-driven), avoiding the "gibberish text" often seen in diffusion-model image generation.
    

### 2.2 The IMPACT Framework Implementation

The MERMAID command is the cornerstone of the IMPACT (Iterative Multi-turn Process for AI Collaboration Technique) framework. It allows an agent to "think" in code (Turn 1) and "speak" in visuals (Turn 2), creating a seamless user experience where complex system architectures or logic flows are visualized instantly.

## 3. Formal Syntax & Parameter Schema (The "What")

### Command Syntax (Golden Template)

@MERMAID("mermaid_code_string")@  
  

### Argument Table

|   |   |   |   |
|---|---|---|---|
|Arg Name|Data Type|Requirement|Description|
|"mermaid_code_string"|String|Required|The raw, valid Mermaid syntax string. This must be enclosed in double quotes. Often populated dynamically via @TR@TN(-1)@@.|

### Return/Output Value

- Output: Renders a visual diagram (SVG) directly in the chat interface.
    
- Return Value: Returns a success status code to the internal log, but the primary artifact is the visual element itself.
    

## 4. Execution Mechanics & State Impact (The "How")

### 4.1 Internal Logic Flow & Sanitization

1. String Ingestion: The engine receives the string argument from the previous turn or variable.
    
2. Wrapper Sanitization: The engine automatically detects and strips Markdown code block wrappers (e.g., ```mermaid and ```). This fault-tolerance allows the LLM to output "formatted" markdown without breaking the renderer.
    
3. Compilation: The Mermaid JS library compiles the cleaned text into an SVG.
    
4. Error Handling: If syntax errors occur, the engine renders the raw error message instead of the diagram, allowing for debugging.
    

### 4.2 Implementation Pattern: Two-Turn Generation (IMPACT)

Turn 1 (LLM - Code Generation):

{  
  "system": "Generate ONLY raw Mermaid code for a flowchart based on the user request.",  
  "user": "Create a process flow for a coffee machine.",  
  "show": true  
}  
  

Turn 2 (Symbolic - Rendering):

{  
  "user": "/ Render the diagram.\n@MERMAID(@TR@TN(-1)@@)@",  
  "show": true  
}  
  

### 4.3 Advanced Pattern: The GAMER Loop (Self-Correction)

For complex diagrams, the LLM might make syntax errors. The GAMER pattern adds a validation step:

1. Draft (LLM): Generate code.
    
2. Critique (LLM): "Review this Mermaid code for syntax errors. Output only the corrected code."
    
3. Render (Symbolic): @MERMAID(@TR@TN(-1)@@)@.
    

## 5. Reference

- Choi, J. (2025). MERMAID Command: Render Flowcharts and Diagrams Code. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---
