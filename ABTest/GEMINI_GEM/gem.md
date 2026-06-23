# Gemini Gem ver 0.1
## Setup
1. Name: `CAFA_Coding_Agent_Prototype_ver 0.1`
2. instruction: refer `AGENTS.md` file.
3. Knowledge Base (KB files): 
```
1. prompts/
coding-agent.md
reviewer.md
validator.md

2. wiki/
index.md
linter.md
protocol.md

2.1 wiki/examples
code-bank.md
```
Files are uploaded without directory information in this version. `fix-log` not updated.



## Coding Test: gemini-3.1 flash standard thinking level
### Simple Quiz Agent
Prompt: 
```markdown
Create a Quiz Agent using the AoA (Architecture of Alignment / Assessment) framework. 

1. Target Mechanism: An iterative critique/scoring loop where the agent presents a question, captures user input via a TEXTAREA, evaluates the answer against a rigid rubric, updates a dynamic score variable, and routes the user to the next question or a final score report.
2. Structure: Ensure a strict "Sandwich" architecture (Symbolic Input → LLM Evaluation → Hidden Control/Routing). 
3. Rules: Follow all CAFA Protocol rules, including model: null for symbolic turns, standalone hidden logic turns, and strict double-quote string formatting.
```

Code output:
```json
{
    "options": {
        "title": "AoA Framework: Iterative Rubric Quiz",
        "brief": "An adaptive open-ended quiz agent driven by the Architecture of Alignment (AoA) framework.",
        "name": "AoA Rubric Quiz Scorer",
        "description": "This agent administers an open-ended quiz using an iterative critique and scoring loop. It features a strict Sandwich architecture to safely capture free-text inputs, grade them dynamically with an LLM against a rigid rubric, and update score parameters symbolically.",
        "greeting": "Welcome to the Alignment Assessment! You will be asked 3 open-ended questions. Please answer them in detail.",
        "params": {
            "TOTAL_QUESTIONS": {
                "org": "3",
                "cond": "SELF",
                "desc": "The total number of questions administered during the loop."
            },
            "QUESTIONS": {
                "org": "Explain the primary function of a database index.|What is the difference between synchronous and asynchronous processing?|Define the concept of polymorphism in object-oriented programming.",
                "cond": "SELF",
                "desc": "The item bank consisting of open-ended question stems."
            },
            "ANSWERS": {
                "org": "An index accelerates data retrieval speeds on a table at the cost of additional storage and write overhead.|Synchronous processing blocks execution until a task finishes; asynchronous processing executes in the background non-blockingly.|Polymorphism allows different classes to be treated as instances of a common parent class through a shared interface.",
                "cond": "LINK(QUESTIONS)",
                "desc": "The target evaluation criteria aligned positionally with the question bank."
            },
            "RUBRIC_PROMPT": {
                "org": "You are an expert academic assessor grading open-ended computer science questions. You will be given a Question, the Expected Criteria, and the Student Answer. Evaluate whether the student answer accurately captures the core meaning of the expected criteria. Allow phrasing variance but require conceptual alignment. Your response MUST be EXACTLY one word: Correct or Incorrect. Do not provide commentary, markup, or punctuation.",
                "cond": "SELF",
                "desc": "Strict binary evaluation constraint for the grading micro-agent."
            }
        }
    },
    "prompts": [
        {
            "system": "",
            "user": "/ AoA Loop Setup: Clear score and open multi-turn loop block\n@SET(\"SCORE\", \"0\")@\n@REPEAT(\"@TN(1)@\", \"@TN(3)@\", \"@TOTAL_QUESTIONS@\")@",
            "show": false,
            "model": null
        },
        {
            "system": "",
            "user": "/ AoA Sandwich - Step 1: Symbolic Input (Visible Bread)\nQuestion @R_i@ of @TOTAL_QUESTIONS@:\n\n**@QUESTIONS[@R_i@]@**\n\n@TEXTAREA(\"user_ans_@R_i@\", \"Type your full answer below:\")@",
            "show": true,
            "model": null
        },
        {
            "system": "@RUBRIC_PROMPT@",
            "user": "Question: @QUESTIONS[@R_i@]@\nExpected Criteria: @ANSWERS[@R_i@]@\nStudent Answer: @TEXTAREA(\"user_ans_@R_i@\")@",
            "show": false,
            "model": "gpt-4.1-nano",
            "temperature": "0.1",
            "max-tokens": "50",
            "output-values": "Correct|Incorrect"
        },
        {
            "system": "",
            "user": "/ AoA Sandwich - Step 3: Hidden Control/Routing (Hidden Bread)\n@SET(\"VERDICT_@R_i@\", \"@TR@TN(-1)@[@R_i@]@\")@\n@SET(\"POINTS\", \"@MAP(\"@VERDICT_@R_i@@\", \"Correct\", \"1|0\")@\")@\n@SET(\"SCORE\", \"@EVAL(\"@SCORE@ + @POINTS@\")@\")@",
            "show": false,
            "model": null
        },
        {
            "system": "",
            "user": "/ Final Summary Presentation\n## Assessment Complete!\n\nThank you for participating in this Architecture of Alignment evaluation quiz.\n\n### Performance Scorecard\n- **Total Items Administered**: @TOTAL_QUESTIONS@\n- **Final Score**: @SCORE@ / @TOTAL_QUESTIONS@\n\n### Item Breakdown\n1. Question 1 Verdict: **@VERDICT_1@**\n2. Question 2 Verdict: **@VERDICT_2@**\n3. Question 3 Verdict: **@VERDICT_3@**",
            "show": true,
            "markdown": true,
            "model": null
        }
    ]
}
```

Errors:

    1. Scoring index issue (Turn 3); cannot safely update `@POINTS@` and therefore corrupt the whole scoring parameters.

### Simple Quiz Generator Agent
Prompt:
```markdown
Create a Quiz Generator Agent using the AoA (Architecture of Alignment / Assessment) framework. 

1. Target Mechanism: An initial configuration stage where the user provides quiz parameters, followed by a dynamic, iterative generation loop. The agent must dynamically track the current question number, generate tailored questions based on user-provided data/topics, accept answers, and route to the next turn.
2. Structure: Ensure a strict "Sandwich" architecture (Symbolic Input for configuration → LLM Generation & Assessment → Hidden Control/Routing/Looping).
3. Configuration Inputs: Use UI controls (e.g., TEXTAREA, RADIO) to capture:
   - Quiz Topic / Inference Data
   - Number of Questions
   - Difficulty Level
4. Rules: Follow all CAFA Protocol rules, including model: null for symbolic configurations, standalone hidden logic turns ("show": false) for loop routing, and strict double-quote string formatting.
```

Code output:
```json
{
  "options": {
    "title": "AoA Dynamic Quiz Generator Agent",
    "brief": "A dynamic quiz generator leveraging the Architecture of Alignment / Assessment framework.",
    "name": "AoA Quiz Generator",
    "description": "This agent captures custom configuration parameters from a user and uses a strict multi-turn Sandwich architecture to generate, collect, and assess open-ended questions iteratively.",
    "greeting": "Welcome to the AoA Quiz Generator. Let's configure your custom test environment.",
    "keep-in-app-cafakey": false,
    "is-template": false,
    "is-public": false,
    "params": {
      "GENERATOR_PERSONA": {
        "org": "You are an elite academic test designer. Your job is to generate exactly ONE open-ended essay question based on the user's target topic and difficulty criteria. Do not output instructions, answers, or meta-commentary. Output only the question text directly.",
        "cond": "SELF",
        "desc": ""
      },
      "EXPERT_GRADER_PERSONA": {
        "org": "You are an expert grading system. Review the question provided and the student's open-ended answer. Provide a constructive evaluation of their answer. End your assessment with a clear performance summary.",
        "cond": "SELF",
        "desc": ""
      },
      "CURRENT_INDEX": {
        "org": "4",
        "cond": "SELF",
        "desc": ""
      },
      "cfg_topic": {
        "org": "{\n  \"id\": \"cfg_topic\",\n  \"label\": \"Enter quiz topic or reference text here...\",\n  \"response\": \"상식\"\n}",
        "cond": "",
        "desc": ""
      },
      "cfg_length": {
        "org": "{\n  \"id\": \"cfg_length\",\n  \"question\": \"Choose length:\",\n  \"choices\": [\n    \"3\",\n    \"5\",\n    \"7\"\n  ],\n  \"textboxLabel\": \"\",\n  \"response\": \"3\",\n  \"userResponse\": \"3\"\n}",
        "cond": "",
        "desc": ""
      },
      "cfg_diff": {
        "org": "{\n  \"id\": \"cfg_diff\",\n  \"question\": \"Choose difficulty:\",\n  \"choices\": [\n    \"Beginner\",\n    \"Intermediate\",\n    \"Advanced\"\n  ],\n  \"textboxLabel\": \"\",\n  \"response\": \"Beginner\",\n  \"userResponse\": \"Beginner\"\n}",
        "cond": "",
        "desc": ""
      },
      "user_reply_1": {
        "org": "{\n  \"id\": \"user_reply_1\",\n  \"label\": \"Type your answer here...\",\n  \"response\": \"비밀번호는 일관되게 설정해서는 안된다. 만약 그렇게 한다면 해킹에 취약해질 수 있다\"\n}",
        "cond": "",
        "desc": ""
      },
      "user_reply_2": {
        "org": "{\n  \"id\": \"user_reply_2\",\n  \"label\": \"Type your answer here...\",\n  \"response\": \"비밀번호는 일관되게 설정해서는 안된다. 만약 그렇게 한다면 해킹에 취약해질 수 있다\\n예를 들어 자신의 생일 및 개인정보와 관련된 정보를 바탕으로 모든 비밀번호를 설정하면 그 정보와 관련된 비밀번호를 가지고있는 모든 계정이 해킹되어 금전적인 피해를 입을 수 있다\"\n}",
        "cond": "",
        "desc": ""
      },
      "user_reply_3": {
        "org": "{\n  \"id\": \"user_reply_3\",\n  \"label\": \"Type your answer here...\",\n  \"response\": \"?\"\n}",
        "cond": "",
        "desc": ""
      }
    }
  },
  "prompts": [
    {
      "system": "",
      "user": "/ Pre-load configuration variables\n@SET(\"CURRENT_INDEX\", \"1\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ Capture Configuration Input 1\n### Step 1: Quiz Topic\nSpecify the domain, skills, or source text you wish to be tested on:\n@TEXTAREA(\"cfg_topic\", \"Enter quiz topic or reference text here...\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ Capture Configuration Input 2\n### Step 2: Quiz Length\nSelect the total number of questions you want to answer:\n@RADIO(\"cfg_length\", \"Choose length:\", \"3|5|7\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ Capture Configuration Input 3\n### Step 3: Difficulty Level\nSelect the target complexity of the generated questions:\n@RADIO(\"cfg_diff\", \"Choose difficulty:\", \"Beginner|Intermediate|Advanced\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ Initialize AoA Assessment Loop Block\n@REPEAT(\"@TN(1)@\", \"@TN(4)@\", \"@RADIO(\"cfg_length\")@\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "@GENERATOR_PERSONA@",
      "user": "Generate Question number @CURRENT_INDEX@ out of @RADIO(\"cfg_length\")@.\nTarget Topic: @TEXTAREA(\"cfg_topic\")@\nDifficulty Setting: @RADIO(\"cfg_diff\")@",
      "temperature": "0.7",
      "max-tokens": "500",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ AoA Sandwich Input - Collect user response to generated item\n## Question @CURRENT_INDEX@ of @RADIO(\"cfg_length\")@\n\n**@TR@TN(-1)@@**\n\n@TEXTAREA(\"user_reply_@R_i@\", \"Type your answer here...\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "@EXPERT_GRADER_PERSONA@",
      "user": "Question: @TR@TN(-2)@@\nStudent Answer: @TEXTAREA(\"user_reply_@R_i@\")@",
      "temperature": "0.2",
      "max-tokens": "1000",
      "send-mail": false,
      "markdown": true,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ AoA Sandwich Control - Hidden index processing and routing block\n@SET(\"CURRENT_INDEX\", \"@EVAL(\"@CURRENT_INDEX@ + 1\")@\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ Assessment Closure Presentation\n## Quiz Session Complete!\n\nYou have completed all @RADIO(\"cfg_length\")@ questions on the topic: **@TEXTAREA(\"cfg_topic\")@**.\n\nReview your individual turn responses and the AI-generated feedback above for a detailed breakdown of your performance.",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": true,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    }
  ]
}
```

Errors:
1. inconsistent question generation index
    - present all the previous questions in an accumulated form
    ```markdown
    ## Question 3 of 3 **일상생활에서 자주 사용하는 기본적인 상식이나 지식을 하나 적어보세요. 그리고 그것이 왜 중요한지 간단하게 설명하세요.|일상생활에서 자주 접하는 상식적인 사실이나 지식을 하나 설명하고, 그것이 왜 중요한지에 대해 서술하세요.|일상생활에서 흔히 접할 수 있는 상식 중 하나를 선택하여, 그것이 왜 중요한지와 일상생활에서 어떻게 활용할 수 있는지에 대해 설명하시오.** Type your answer here...
    ```
2. inconsistent evaluations
    - no explicit matrix that the output refers to as evaluating answers
    ```markdown
    이 학생의 답변은 일상생활에서 자주 접하는 중요한 보안 상식을 잘 설명하고 있습니다. 특히, 비밀번호를 일관되게 사용하는 것이 위험하다는 점과, 생일이나 개인정보를 이용한 비밀번호의 위험성을 구체적인 예를 들어 설명한 점이 좋습니다. 이는 비밀번호 관리의 중요성을 이해하고 있음을 보여줍니다.

    그러나 답변이 조금 더 명확하고 구체적일 수 있습니다. 예를 들어, "일관되게 설정해서는 안 된다"는 표현 대신 "다양한 비밀번호를 사용하는 것이 중요하다"라고 명확 하는 것이 더 좋았을 것 같습니다. 또한, 왜 다양한 비밀번호가 중요한지에 대한 설명이 조금 더 구체적이면 더 완성도 높은 답변이 될 수 있습니다.

    전반적으로, 학생은 일상생활에서 자주 접하는 상식을 잘 파악하고 있으며, 그 중요성도 이해하고 있습니다. 앞으로는 구체적인 예시와 설명을 더 명확하게 하는 연습을 하면 더욱 뛰어난 답변이 될 것입니다.

    성능 평가: **양호** <- no idea how this came out or where it came from or being evaluated on
    ```


### OMG Quiz Agent
Output code:
```json
{
    "options": {
        "title": "Dynamic OMG Assessment Engine",
        "brief": "An automated quiz agent implementing the OMG framework with randomized item alignment and symbolic auto-grading loops.",
        "name": "OMG_Dynamic_Quiz_Agent",
        "description": "This operational engine shuffles quiz questions while preserving option-to-answer integrity through parallel linked parameters, administering items iteratively and tracking state dynamically.",
        "greeting": "Welcome to the Dynamic Quiz Assessment! You will be presented with 3 randomized questions. Let's begin.",
        "params": {
            "QUESTIONS": {
                "org": "What is the capital of France?|Which planet is known as the Red Planet?|What is the largest mammal on Earth?",
                "cond": "SHUFFLE",
                "desc": "Primary array containing the quiz question stems."
            },
            "OPTIONS_A": {
                "org": "Paris|Mars|Blue Whale",
                "cond": "LINK(QUESTIONS)",
                "desc": "Parallel list holding the first multiple-choice option."
            },
            "OPTIONS_B": {
                "org": "London|Venus|Elephant",
                "cond": "LINK(QUESTIONS)",
                "desc": "Parallel list holding the second multiple-choice option."
            },
            "OPTIONS_C": {
                "org": "Berlin|Jupiter|Giraffe",
                "cond": "LINK(QUESTIONS)",
                "desc": "Parallel list holding the third multiple-choice option."
            },
            "ANSWERS": {
                "org": "Paris|Mars|Blue Whale",
                "cond": "LINK(QUESTIONS)",
                "desc": "Parallel ground-truth keys linked to the shuffled question stems."
            },
            "USER_SCORE": {
                "org": "0",
                "cond": "SELF",
                "desc": "Scalar memory parameter used to accumulate student score updates."
            }
        }
    },
    "prompts": [
        {
            "system": "",
            "user": "/ Initialization Turn\n@SET(\"USER_SCORE\", \"0\")@",
            "show": false
        },
        {
            "system": "",
            "user": "/ Dedicated Control Flow Loop Orchestration Turn\n@REPEAT(@TN(1)@, @TN(2)@, \"3\")@",
            "show": false
        },
        {
            "system": "",
            "user": "/ Loop Step 1: Display Interactive Survey Control\nQuestion @R_i@ of 3:\n@RADIO(\"user_ans_@R_i@\", \"@QUESTIONS[@R_i@]@\", \"@OPTIONS_A[@R_i@]@|@OPTIONS_B[@R_i@]@|@OPTIONS_C[@R_i@]@\")@",
            "show": true
        },
        {
            "system": "",
            "user": "/ Loop Step 2: Atomic Evaluation Gate\n@SET(\"USER_SCORE\", \"@EVAL(\"@USER_SCORE@ + @MAP(\"@RADIO(user_ans_@R_i@)@\", \"@ANSWERS[@R_i@]@\", \"1|0\")@\")@\")@",
            "show": false
        },
        {
            "system": "",
            "user": "/ Post-Loop Synthesis State\n# Assessment Complete!\n\nThank you for participating. Your final synchronized score has been processed.\n\n### Final Result: **@USER_SCORE@** out of 3 points.",
            "show": true,
            "markdown": true
        }
    ]
}
```
Notable issues/Errors:
- no linter errors
  - neither unnecessary double quotes nor `\` that causes parsing errors without any fix turns
- follows OMG Framework well
- performs better than pro models.

### Mock LLM Wiki on CAFA Agents

Output code:
#### 1. Architecture
```json
{
  "options": {
    "title": "LLM Wiki Builder",
    "brief": "Authoring tool for generating structured, interlinked wiki pages from raw documents.",
    "name": "wiki_builder",
    "description": "Ingests raw sources, distills them using an LLM, persists them to a structured state, and exports the bundle.",
    "greeting": "Welcome to the LLM Wiki Builder. Select an option from the menu to begin.",
    "raw_curr_idx": { "org": "local", "cond": "SELF", "desc": "Snapshot of the raw source count before editing" },
    "raw": { "org": "local", "cond": "SELF", "desc": "Array containing raw document contents" },
    "raw_name": { "org": "local", "cond": "SELF", "desc": "Array containing raw document titles" },
    "wiki": { "org": "local", "cond": "SELF", "desc": "Nested dictionary structure containing finished wiki pages" },
    "wiki_index": { "org": "local", "cond": "SELF", "desc": "Table of contents/index metadata for the generated wiki" },
    "wiki_log": { "org": "local", "cond": "SELF", "desc": "History and activity log of wiki modification batches" },
    "Agent_Config": { "org": "local", "cond": "SELF", "desc": "System rulebook containing Identity, rules, and citation_rules" },
    "page_format": { "org": "local", "cond": "SELF", "desc": "Template layout specification for generated markdown pages" }
  },
  "prompts": [
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/SET raw_curr_idx = \"@raw_name.length@\""
    },
    {
      "model": null,
      "show": true,
      "system": "Present the administration dashboard menu options to the user.",
      "user": "/RADIO menu \"Select an administrative action:\" [\"Add raw sources\", \"Lint/Audit\", \"Launch the Runnable\", \"End\"]"
    },
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/JUMP @MAP(\"@TR@TN(\"-1\")@\", [\"Add raw sources\", \"Lint/Audit\", \"Launch the Runnable\", \"End\"], \"@TN(\"1\")@\", \"@TN(\"5\")@\", \"@TN(\"11\")@\", \"@TN(\"19\")@\")@"
    },
    {
      "model": null,
      "show": true,
      "system": "Prompt user for the raw source document details.",
      "user": "/TEXT source_title \"Enter document title:\""
    },
    {
      "model": null,
      "show": true,
      "system": "Prompt user for the text content of the raw document.",
      "user": "/TEXTAREA source_body \"Paste the document text content here:\""
    },
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/UPJ raw = \"@TR@TN(\"-1\")@\"\n/UPJ raw_name = \"@TR@TN(\"-2\")@\""
    },
    {
      "model": null,
      "show": true,
      "system": "Ask the user if they wish to ingest another document or commit.",
      "user": "/RADIO add_more \"Would you like to add another source?\" [\"Yes\", \"No\"]"
    },
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/JUMP @MAP(\"@TR@TN(\"-1\")@\", [\"Yes\"], \"@TN(\"-5\")@\", \"@TN(\"1\")@\")@"
    },
    {
      "model": "gpt-4.1",
      "show": true,
      "system": "Rules:\n@Agent_Config.rules@\n\nCitations:\n@Agent_Config.citation_rules@\n\nAnalyze the newly added raw items and extract core atomic takeaways.",
      "user": "Review the following raw elements and provide key insights:\n@raw@"
    },
    {
      "model": null,
      "show": true,
      "system": "Ask the manager how to handle the extracted text insights.",
      "user": "/RADIO post_distill \"Choose the next stage for the extracted insights:\" [\"Continue\", \"Revise\", \"Menu\"]"
    },
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/JUMP @MAP(\"@TR@TN(\"-1\")@\", [\"Continue\", \"Revise\"], \"@TN(\"4\")@\", \"@TN(\"-2\")@\", \"@TN(\"1\")@\")@"
    },
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/REPEAT \"@EVAL(\"@raw_name.length@ - @raw_curr_idx@\")@\" @TN(\"1\")@"
    },
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/DELJ raw_name = \"@EVAL(\"@raw_name.length@ + 1 - @R_i@\")@\"\n/DELJ raw = \"@EVAL(\"@raw.length@ + 1 - @R_i@\")@\""
    },
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/JUMP @TN(\"-12\")@"
    },
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/REPEAT \"@raw.length@\" @TN(\"1\")@"
    },
    {
      "model": "gpt-4.1",
      "show": false,
      "system": "Format requirements:\n@page_format@",
      "user": "Write a clean wiki article markdown document for topic \"@raw_name[@R_i@]@\" given source source text content: \"@raw[@R_i@]@\" and matching takeaways: \"@TR@TN(\"-7\")@\""
    },
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/UPJ wiki = {\"@raw_name[@R_i@]@\": \"@TR@TN(\"-1\")@\"}"
    },
    {
      "model": "gpt-4.1",
      "show": false,
      "system": "You are a master index engineer.",
      "user": "Regenerate the unified `wiki_index` directory using all compiled pages stored here: @wiki@"
    },
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/SET wiki_index = \"@TR@TN(\"-1\")@\"\n/UPJ wiki_log = {\"timestamp\": \"@NOW@\", \"actions\": \"Batch addition of records\"}"
    },
    {
      "model": null,
      "show": true,
      "system": "Inquire if user wants to transition directly to reading or return to control dashboard.",
      "user": "/RADIO target_agent \"Deploy or back to start?\" [\"Chat\", \"Menu\"]"
    },
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/JUMP @MAP(\"@TR@TN(\"-1\")@\", [\"Chat\"], \"@TN(\"1\")@\", \"@TN(\"-20\")@\")@"
    },
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/EXPORT URL \"@EXPORT(Agent_Config, raw, wiki, wiki_index, wiki_log, page_format)@\""
    },
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/END"
    }
  ]
}
```

#### Runner
```json
{
  "options": {
    "title": "LLM Wiki Chat Viewer",
    "brief": "Consumer client serving conversational RAG across loaded knowledge databases.",
    "name": "wiki_runner",
    "description": "Hydrates a pre-built workspace wiki payload via deep-linking and manages interactive context-bounded questioning sessions.",
    "greeting": "Wiki database connected. Type your prompt to consult the indexed documentation sets.",
    "Agent_Config": { "org": "import", "cond": "LINK(\"wiki_builder.Agent_Config\")", "desc": "Imported configuration policies" },
    "raw": { "org": "import", "cond": "LINK(\"wiki_builder.raw\")", "desc": "Imported backup raw texts array" },
    "wiki": { "org": "import", "cond": "LINK(\"wiki_builder.wiki\")", "desc": "Imported complete catalog of wiki pages" },
    "wiki_index": { "org": "import", "cond": "LINK(\"wiki_builder.wiki_index\")", "desc": "Imported active searchable metadata indexes" },
    "wiki_log": { "org": "import", "cond": "LINK(\"wiki_builder.wiki_log\")", "desc": "Imported change logs payload structural array" },
    "page_format": { "org": "import", "cond": "LINK(\"wiki_builder.page_format\")", "desc": "Imported page templates layout formatting metrics" },
    "chat_log": { "org": "local", "cond": "SELF", "desc": "Sequential message thread logs representation" },
    "Q_answer_rule": { "org": "local", "cond": "SELF", "desc": "Strict constraints and procedures for rendering responses strictly using the provided context blocks" }
  },
  "prompts": [
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/IMPORT @ID_ID@"
    },
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/SET chat_log = []"
    },
    {
      "model": null,
      "show": true,
      "system": "Announce safe establishment of operational workspace.",
      "user": "The client has initialized. The database houses @wiki_log.length@ modifications updates."
    },
    {
      "model": "gpt-4.1",
      "show": true,
      "markdown": true,
      "system": "Instructions:\n@Q_answer_rule@\n\nReference Material Index:\n@wiki_index@\n\nFull Reference Body Texts:\n@wiki@\n\nPrior Discourse Timeline:\n@chat_log@",
      "user": ""
    },
    {
      "model": null,
      "show": true,
      "system": "Inquire if another session pass is required.",
      "user": "/RADIO session_gate \"Do you have further follow-up queries?\" [\"Yes\", \"No\"]"
    },
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/JUMP @MAP(\"@TR@TN(\"-1\")@\", [\"Yes\"], \"@TN(\"1\")@\", \"@TN(\"3\")@\")@"
    },
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/UPJ chat_log = {\"query\": \"@TU@TN(\"-3\")@\", \"response\": \"@TR@TN(\"-3\")@\"}"
    },
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/JUMP @TN(\"-4\")@"
    },
    {
      "model": null,
      "show": true,
      "system": "Sign-off process formulation.",
      "user": "Closing active session tunnel. Goodbye!"
    },
    {
      "model": null,
      "show": false,
      "system": "",
      "user": "/END"
    }
  ]
}
```

notable issues/Errors:
- fails to follow basic CAFA coding protocols and linter. cannot run the agent at all.
- fix failed: unknown reason to fail fix
  - due to the issue, I was unable to proceed testing the model's coding performance
- response time: $\approx$ 15 - 30 seconds.

## Coding test: gemini-3.1 pro extended thinking model
### Simple Quiz Agent

Output code:
```json
{
  "options": {
    "title": "AoA Framework Quiz Agent",
    "name": "AoA Rubric Quiz",
    "brief": "Iterative assessment leveraging the AoA Sandwich Architecture for rubric-based grading.",
    "description": "This agent administers a quiz utilizing the Architecture of Alignment (AoA). It utilizes a strict Sandwich Architecture: collecting constructed responses via TEXTAREA, performing LLM-based rubric evaluations, and executing hidden symbolic flow control for dynamic scoring.",
    "greeting": "Welcome to the assessment. Please read each question carefully and provide detailed reasoning.",
    "params": {
      "SCORE": {
        "org": "0",
        "cond": "SELF",
        "desc": "Dynamic numeric tracker for the user's score."
      },
      "QUESTIONS": {
        "org": "Explain the concept of supply and demand.|What is the primary function of mitochondria?",
        "cond": "SELF",
        "desc": "Question stems for the quiz."
      },
      "RUBRICS": {
        "org": "Must describe the relationship between price, availability, and buyer desire.|Must mention energy production or ATP.",
        "cond": "LINK(QUESTIONS)",
        "desc": "Rigid grading rubrics semantically linked to the questions."
      },
      "VERDICTS": {
        "org": "Correct|Incorrect",
        "cond": "SELF",
        "desc": "Output constraints for the evaluation LLM."
      }
    }
  },
  "prompts": [
    {
      "system": "",
      "user": "/ Loop Setup\n@REPEAT(\"@TN(\\\"1\\\")@\", \"@TN(\\\"3\\\")@\", \"2\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Sandwich Stage 1: Symbolic Input\n@TEXTAREA(\"ans_@R_i@\", \"Question @R_i@: @QUESTIONS[@R_i@]@\")@",
      "show": true,
      "model": null
    },
    {
      "system": "You are a strict evaluation assistant. Assess the user's response against the provided rubric. Your output MUST be exactly one word matching the allowed verdicts.",
      "user": "- Question: @QUESTIONS[@R_i@]@\n- Rubric: @RUBRICS[@R_i@]@\n- User Answer: @TEXTAREA(\"ans_@R_i@\")@",
      "show": true,
      "model": "gpt-4.1-nano",
      "temperature": "0.1",
      "max-tokens": "50",
      "output-values": "@VERDICTS@"
    },
    {
      "system": "",
      "user": "/ Sandwich Stage 3: Hidden Control (Scoring and Routing)\n@SET(\"SCORE\", \"@EVAL(\"@SCORE@ + @MAP(\"@TR@TN(\\\"-1\\\")@[@R_i@]@\", \"Correct\", \"1|0\")@\")@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Final Score Report\n## Quiz Complete!\n\nYour final score is **@SCORE@** out of 2.",
      "show": true,
      "markdown": true,
      "model": null
    }
  ]
}
```

Error:
1. linting issue
    - arguments of the some commands (`@REPEAT@`, `@MAP@`) contains double quotes where these should not exist due to CAFA engine parsing issue. Moreover, `\` cannot exist between the arguments but the model keeps generating code with special characters that disrupts linters and validators.

### Simple Quiz Generator Agent
Output code:
```json
{
  "options": {
    "title": "AoA Adaptive Quiz Generator",
    "brief": "A dynamic quiz generator utilizing the Architecture of Alignment (AoA) framework.",
    "name": "AoA_Quiz_Agent",
    "description": "This agent uses a strict Sandwich architecture to capture configuration parameters, generate tailored questions dynamically inside a loop, accept user answers, and provide AI diagnostic feedback turn-by-turn.",
    "greeting": "Welcome to the AoA Quiz Generator. Let's configure your quiz parameters.",
    "keep-in-app-cafakey": false,
    "is-template": false,
    "is-public": false,
    "params": {
      "NUM_QUESTIONS": {
        "org": "1|2|3|4|5",
        "cond": "SELF",
        "desc": "Available options for the total number of quiz questions."
      },
      "DIFFICULTY": {
        "org": "Easy|Medium|Hard",
        "cond": "SELF",
        "desc": "Available options for the quiz difficulty level."
      },
      "quiz_topic": {
        "org": "{\n  \"id\": \"quiz_topic\",\n  \"label\": \"Enter Quiz Topic / Inference Data:\",\n  \"response\": \"machine learning\"\n}",
        "cond": "",
        "desc": ""
      },
      "quiz_num": {
        "org": "{\n  \"id\": \"quiz_num\",\n  \"question\": \"Select Number of Questions:\",\n  \"choices\": [\n    \"1\",\n    \"2\",\n    \"3\",\n    \"4\",\n    \"5\"\n  ],\n  \"textboxLabel\": \"\",\n  \"response\": \"3\",\n  \"userResponse\": \"3\"\n}",
        "cond": "",
        "desc": ""
      },
      "quiz_diff": {
        "org": "{\n  \"id\": \"quiz_diff\",\n  \"question\": \"Select Difficulty Level:\",\n  \"choices\": [\n    \"Easy\",\n    \"Medium\",\n    \"Hard\"\n  ],\n  \"textboxLabel\": \"\",\n  \"response\": \"Easy\",\n  \"userResponse\": \"Easy\"\n}",
        "cond": "",
        "desc": ""
      },
      "user_ans_1": {
        "org": "{\n  \"id\": \"user_ans_1\",\n  \"label\": \"Type your answer here:\",\n  \"response\": \"The primary goal of machine learning is generalization. Instead of simply memorizing training data, a machine learning system is designed to learn underlying patterns so it can autonomously make accurate predictions or decisions when exposed to completely new, unseen data.\"\n}",
        "cond": "",
        "desc": ""
      },
      "Question_Completed_1": {
        "org": "True",
        "cond": "SELF",
        "desc": ""
      },
      "user_ans_2": {
        "org": "{\n  \"id\": \"user_ans_2\",\n  \"label\": \"Type your answer here:\",\n  \"response\": \"The primary goal of machine learning is generalization. Instead of simply memorizing training data, a machine learning system is designed to learn underlying patterns so it can autonomously make accurate predictions or decisions when exposed to completely new, unseen data.\"\n}",
        "cond": "",
        "desc": ""
      },
      "Question_Completed_2": {
        "org": "True",
        "cond": "SELF",
        "desc": ""
      },
      "user_ans_3": {
        "org": "{\n  \"id\": \"user_ans_3\",\n  \"label\": \"Type your answer here:\",\n  \"response\": \"The primary goal of machine learning is generalization. Instead of simply memorizing training data, a machine learning system is designed to learn underlying patterns so it can autonomously make accurate predictions or decisions when exposed to completely new, unseen data.\"\n}",
        "cond": "",
        "desc": ""
      },
      "Question_Completed_3": {
        "org": "True",
        "cond": "SELF",
        "desc": ""
      }
    }
  },
  "prompts": [
    {
      "system": "",
      "user": "/ Configuration 1: Quiz Topic\n@TEXTAREA(\"quiz_topic\", \"Enter Quiz Topic / Inference Data:\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ Configuration 2: Number of Questions\n@RADIO(\"quiz_num\", \"Select Number of Questions:\", \"@NUM_QUESTIONS@\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ Configuration 3: Difficulty Level\n@RADIO(\"quiz_diff\", \"Select Difficulty Level:\", \"@DIFFICULTY@\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "@REPEAT(\"@TN(1)@\", \"@TN(4)@\", \"@RADIO(quiz_num)@\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": false,
      "show": false,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "You are an expert quiz generator. Based on the topic and difficulty, generate one specific question. Output ONLY the question text without any conversational filler or formatting.",
      "user": "Topic: @TEXTAREA(quiz_topic)@\nDifficulty: @RADIO(quiz_diff)@\nQuestion @R_i@ of @RADIO(quiz_num)@\n\nGenerate the question:",
      "temperature": "0.7",
      "max-tokens": "1000",
      "send-mail": false,
      "markdown": false,
      "show": false,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ Present generated question and capture answer\n### Question @R_i@ of @RADIO(quiz_num)@\n\n@TR@TN(-1)@[@R_i@]@\n\n@TEXTAREA(\"user_ans_@R_i@\", \"Type your answer here:\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": true,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "You are an AI diagnostic assessor following the Architecture of Alignment (AoA) framework. Evaluate the user's answer against the generated question. Provide constructive diagnostic feedback.",
      "user": "Question:\n@TR@TN(-2)@[@R_i@]@\n\nUser's Answer:\n@TEXTAREA(user_ans_@R_i@)@",
      "temperature": "0.1",
      "max-tokens": "2000",
      "send-mail": false,
      "markdown": true,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ Hidden Control Turn for loop routing and state maintenance\n@SET(\"Question_Completed_@R_i@\", \"True\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": false,
      "show": false,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ Final summary\n## Quiz Complete\n\nThank you for completing the @TEXTAREA(quiz_topic)@ quiz. You have finished all @RADIO(quiz_num)@ questions.",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": true,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    }
  ]
}
```

Error: no technical error found

However, Grading is skipped and question variance is too low (too low default temperature: `0.1`) and code generation takes as much time as claude code and less quality in overall structures and comments for documentation

Conclusion: This level of code complexity seems to be the upper limit of current Gem's ability as a coding agent. Further experiments with this version seems worthless as it seems to be inefficient, taking too much time and less quality compared to previous claude code version or gemini-3.1 pro standard model.

### OMG Quiz Agent
Prompt:
```markdown
Role & Goal:
You are the CAFA Agent Foundry Agent. Please translate my request into a valid, executable CAFA agent JSON. I need an intermediate-to-expert level Dynamic Quiz Agent with Automatic Scoring that implements the OMG (Ontology Model-centered Generation) framework combined with an iterative REPEAT loop.
Instructions & Constraints:

Workflow & Blueprint: Do not skip stages. Begin with the design stage by providing a comprehensive Blueprint [Design]. This must include the primary goal, framework used, a complete list of commands, the AP/JP ontology specifications, and a turn architecture plan [Symbolic vs. LLM classification].
Ontology & Data Handling:
Define a robust tabular ontology in options.params with parallel lists for Questions (Stems), Options (flattened or dynamically sliced), and Correct Answers.
Use the SHUFFLE condition on the primary list and LINK on the dependent lists to randomize the quiz while preserving semantic pairing.
Initialize a USER_SCORE variable to "0" in an early hidden turn.
Advanced Logic & Loop Administration:
Set up a REPEAT loop using relative turn numbering (@TN()) to administer the quiz.
Inside the loop, present each question using a RADIO control. Use the loop iteration index [@R_i@] to dynamically pull the correct stem and options.
Grade the response deterministically in a hidden symbolic turn. Use @MAP to compare the user's RADIO input against the linked correct answer (returning 1 or 0), and update the USER_SCORE using @EVAL.
Strict Linter Compliance:
Control-flow Isolation: Ensure the REPEAT command is strictly isolated in its own hidden symbolic turn ("show": false).
Dependency Rule: Do not reference the newly updated USER_SCORE within the exact same turn it is modified; wait until a subsequent turn.
UI Constraints: Ensure there is only one input control per visible turn.
Output Packaging: Provide your response in exactly this order: The Blueprint, the full Agent Code (as a single valid JSON block), a minimal verification summary, the standard CAFA import instructions, and exactly two APA references.
```
Output code:
```json
{
  "options": {
    "title": "OMG Dynamic Assessment Agent",
    "name": "OMG Dynamic Quiz with REPEAT",
    "brief": "A dynamic quiz agent leveraging linked ontology models and an automatic scoring loop.",
    "description": "This agent shuffles a set of questions while maintaining the semantic pairing of its options and correct answers. It uses a REPEAT loop to administer the quiz and an EVAL/MAP combination to deterministically score the user.",
    "greeting": "Welcome to the Dynamic Quiz! Let's test your general knowledge.",
    "params": {
      "STEMS": {
        "org": "What is the largest planet in our solar system?|Who painted the Mona Lisa?|What is the chemical symbol for water?",
        "cond": "SHUFFLE",
        "desc": "Primary list of question stems, shuffled dynamically per session."
      },
      "OPT_A": {
        "org": "Earth|Vincent van Gogh|H2O2",
        "cond": "LINK(STEMS)",
        "desc": "First answer option, linked to the stems."
      },
      "OPT_B": {
        "org": "Saturn|Leonardo da Vinci|HO2",
        "cond": "LINK(STEMS)",
        "desc": "Second answer option, linked to the stems."
      },
      "OPT_C": {
        "org": "Jupiter|Pablo Picasso|H2O",
        "cond": "LINK(STEMS)",
        "desc": "Third answer option, linked to the stems."
      },
      "ANSWERS": {
        "org": "Jupiter|Leonardo da Vinci|H2O",
        "cond": "LINK(STEMS)",
        "desc": "Correct answers perfectly aligned with the stems."
      },
      "TOTAL_QUESTIONS": {
        "org": "3",
        "cond": "SELF",
        "desc": "Number of quiz loop iterations."
      }
    }
  },
  "prompts": [
    {
      "user": "/ T1: Initialize the user's score to zero.\n@SET(\"USER_SCORE\", \"0\")@",
      "show": false,
      "model": null
    },
    {
      "user": "/ T2: Setup the REPEAT loop to execute the next three turns for each question.\n@REPEAT(\"@TN(1)@\", \"@TN(3)@\", \"@TOTAL_QUESTIONS@\")@",
      "show": false,
      "model": null
    },
    {
      "user": "/ T3 (Loop 1/3): Display the current question using a RADIO control.\n@RADIO(\"ans_@R_i@\", \"Question @R_i@ of @TOTAL_QUESTIONS@:<br><br>**@STEMS[@R_i@]@**\", \"@OPT_A[@R_i@]@|@OPT_B[@R_i@]@|@OPT_C[@R_i@]@\")@",
      "show": true,
      "model": null
    },
    {
      "user": "/ T4 (Loop 2/3): Evaluate the user's response deterministically and store the increment.\n@SET(\"SCORE_INC_@R_i@\", \"@MAP(\\\"@TR3[@R_i@]@\\\", \\\"@ANSWERS[@R_i@]@\\\", \\\"1|0\\\")@\")@",
      "show": false,
      "model": null
    },
    {
      "user": "/ T5 (Loop 3/3): Update the cumulative score safely in a dedicated turn.\n@SET(\"USER_SCORE\", \"@EVAL(\\\"@USER_SCORE@ + @SCORE_INC_@R_i@@\\\")@\")@",
      "show": false,
      "model": null
    },
    {
      "user": "/ T6: Final summary displaying the completed quiz score.\n## Quiz Complete!\n\nYour final score is **@USER_SCORE@** out of @TOTAL_QUESTIONS@.",
      "show": true,
      "markdown": true,
      "model": null
    }
  ]
}
```
Notable issues/Errors:
- linter issue
  - the model cannot understand the basic linting rules (keeps HTML parsing character `\` in the functions' arguments and unncessary double quotes)
  - incorrect mapping (seems to focus too much on "deterministic"; not using AP dynamically for `@MAP@` and also incorrectly seems to be a minor issue), causing scoring error
  - code fix did not happen after a few turns of fixing prompts.

- It uses Content APs (questions, distractors, answers) dynamically using `SHUFFLE` and `LINK` options.
- Seems to follow OMG framework according to the `protocol.md`


### Mock LLM Wiki on CAFA Agents
Output code:
#### Architecture
```json
{
  "options": {
    "title": "LLM Wiki Builder",
    "name": "mock_wiki_CAFA_builder",
    "brief": "Authoring tool to ingest sources and generate a wiki.",
    "description": "Menu-driven wiki builder agent utilizing LLM distillation and structured state management.",
    "greeting": "Welcome to the LLM Wiki Builder. Select an action to begin.",
    "params": {
      "raw_curr_idx": { "org": "0", "cond": "SELF", "desc": "Snapshot of source count" },
      "raw": { "org": "[]", "cond": "SELF", "desc": "Array of raw {title, content} objects" },
      "raw_name": { "org": "[]", "cond": "SELF", "desc": "Array of raw source titles" },
      "wiki": { "org": "{}", "cond": "SELF", "desc": "Generated wiki pages" },
      "wiki_log": { "org": "[]", "cond": "SELF", "desc": "Audit log for tracking generations" },
      "Agent_Config": { "org": "{\"rules\":\"Strict accuracy\",\"citation_rules\":\"APA format\"}", "cond": "SELF", "desc": "Configuration rules" },
      "page_format": { "org": "Markdown with headers", "cond": "SELF", "desc": "Page format template" },
      "wiki_index": { "org": "", "cond": "SELF", "desc": "Index of wiki pages" }
    }
  },
  "prompts": [
    {
      "system": "",
      "user": "/ Init state\n@SET(\"raw_curr_idx\", \"@EVAL(\\\"@raw_name.length@\\\")@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Main menu\n@RADIO(\"menu\", \"Select an action:\", \"Add raw sources|Lint/Audit|Launch the Runnable|End\")@",
      "show": true,
      "model": null
    },
    {
      "system": "",
      "user": "/ Menu router\n@JUMP(\"@MAP(\\\"@RADIO(menu)@\\\", \\\"Add raw sources|Lint/Audit|Launch the Runnable|End\\\", \\\"@TN(\\\"1\\\")@|@TN(\\\"15\\\")@|@TN(\\\"19\\\")@|@TN(\\\"21\\\")@|@TN(\\\"21\\\")@\\\")@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Source title\n@TEXT(\"title\", \"Enter source title:\")@",
      "show": true,
      "model": null
    },
    {
      "system": "",
      "user": "/ Source body\n@TEXTAREA(\"body\", \"Enter source content:\")@",
      "show": true,
      "model": null
    },
    {
      "system": "",
      "user": "/ Append source\n@UPJ(\"raw\", \"{\\\"title\\\": \\\"@TEXT(title)@\\\", \\\"content\\\": \\\"@TEXTAREA(body)@\\\"}\")@\n@UPJ(\"raw_name\", \"\\\"@TEXT(title)@\\\"\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Add more prompt\n@RADIO(\"add_more\", \"Add another source?\", \"Yes|No\")@",
      "show": true,
      "model": null
    },
    {
      "system": "",
      "user": "/ Route Add Source\n@JUMP(\"@MAP(\\\"@RADIO(add_more)@\\\", \\\"Yes|No\\\", \\\"@TN(\\\"-4\\\")@|@TN(\\\"1\\\")@|@TN(\\\"1\\\")@\\\")@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "Rules: @Agent_Config.rules@\nCitations: @Agent_Config.citation_rules@",
      "user": "List key takeaways from these sources:\n@raw@",
      "show": true,
      "model": "gpt-4.1-nano",
      "temperature": "0.5",
      "max-tokens": "2000"
    },
    {
      "system": "",
      "user": "/ Revise menu\n@RADIO(\"revise_menu\", \"Next step?\", \"Continue|Revise|Menu\")@",
      "show": true,
      "model": null
    },
    {
      "system": "",
      "user": "/ Route revise menu\n@JUMP(\"@MAP(\\\"@RADIO(revise_menu)@\\\", \\\"Continue|Revise|Menu\\\", \\\"@TN(\\\"4\\\")@|@TN(\\\"-2\\\")@|@TN(\\\"1\\\")@|@TN(\\\"4\\\")@\\\")@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Rollback loop setup\n@REPEAT(\"@TN(\\\"1\\\")@\", \"@TN(\\\"1\\\")@\", \"@EVAL(\\\"@raw_name.length@ - @raw_curr_idx@\\\")@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Rollback execution\n@DELJ(\"raw\", \"@EVAL(\\\"@raw_name.length@+1-@R_i@\\\")@\")@\n@DELJ(\"raw_name\", \"@EVAL(\\\"@raw_name.length@+1-@R_i@\\\")@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Return to Main menu\n@JUMP(\"@TN(\\\"-13\\\")@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Generation loop setup\n@REPEAT(\"@TN(\\\"1\\\")@\", \"@TN(\\\"2\\\")@\", \"@raw.length@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "Write a wiki page per: @page_format@",
      "user": "Source material: @raw[@R_i@]@\nKey Takeaways: @TR@TN(\"-7\")@[@R_i@]@",
      "show": true,
      "model": "gpt-4.1-nano",
      "temperature": "0.5",
      "max-tokens": "2000"
    },
    {
      "system": "",
      "user": "/ Save wiki page\n@UPJ(\"wiki\", \"{\\\"@raw_name[@R_i@]@\\\": \\\"@TR@TN(\\\"-1\\\")@[@R_i@]@\\\"}\")@",
      "show": false,
      "model": null
    },
    {
      "system": "You are a wiki indexer.",
      "user": "Regenerate the wiki_index from the current wiki pages:\n@wiki@",
      "show": true,
      "model": "gpt-4.1-nano",
      "temperature": "0.1",
      "max-tokens": "1000"
    },
    {
      "system": "",
      "user": "/ Finalize index and log\n@SET(\"wiki_index\", \"@TR@TN(\\\"-1\\\")@@\")@\n@UPJ(\"wiki_log\", \"{\\\"date\\\": \\\"@NOW@\\\", \\\"sources\\\": \\\"@raw_name@\\\"}\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Handoff menu\n@RADIO(\"handoff\", \"Generation complete. Proceed to:\", \"Chat|Menu\")@",
      "show": true,
      "model": null
    },
    {
      "system": "",
      "user": "/ Route handoff\n@JUMP(\"@MAP(\\\"@RADIO(handoff)@\\\", \\\"Chat|Menu\\\", \\\"@TN(\\\"1\\\")@|@TN(\\\"-19\\\")@|@TN(\\\"1\\\")@\\\")@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Export payload\n@EXPORT(\"Agent_Config|raw|wiki|wiki_index|wiki_log|page_format\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Display launch link\n[Launch Runner Chat](https://ai.cafalab.com/runner?ID_ID=@TR@TN(\"-1\")@@)",
      "show": true,
      "markdown": true,
      "model": null
    },
    {
      "system": "",
      "user": "/ End session\n@END@",
      "show": false,
      "model": null
    }
  ]
}
```

#### Runner
```json
{
  "options": {
    "title": "LLM Wiki Chat Runner",
    "name": "mock_wiki_CAFA_runner",
    "brief": "Serves an interactive RAG chat over the exported wiki.",
    "description": "Consumes the exported wiki bundle and runs a continuous Q&A loop.",
    "greeting": "Welcome! Hydrating wiki data...",
    "params": {
      "Q_answer_rule": { "org": "Read index -> read pages -> synthesize -> cite -> say if absent -> offer to file good answers back", "cond": "SELF", "desc": "System instructions for Q&A" },
      "chat_log": { "org": "[]", "cond": "SELF", "desc": "Conversation accumulator" },
      "Agent_Config": { "org": "", "cond": "SELF", "desc": "Imported configuration placeholder" },
      "raw": { "org": "", "cond": "SELF", "desc": "Imported raw sources placeholder" },
      "wiki": { "org": "", "cond": "SELF", "desc": "Imported wiki placeholder" },
      "wiki_index": { "org": "", "cond": "SELF", "desc": "Imported index placeholder" },
      "wiki_log": { "org": "", "cond": "SELF", "desc": "Imported log placeholder" },
      "page_format": { "org": "", "cond": "SELF", "desc": "Imported format placeholder" }
    }
  },
  "prompts": [
    {
      "system": "",
      "user": "/ Hydrate wiki data\n@IMPORT(\"@ID_ID@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Sanity echo\n@SET(\"sanity_check\", \"@wiki_index@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Greeting\nWiki successfully loaded. You can now chat with the knowledge base.",
      "show": true,
      "markdown": true,
      "model": null
    },
    {
      "system": "Rules:\n@Q_answer_rule@\nWiki pages:\n@wiki@\nWiki index:\n@wiki_index@\nChat Log:\n@chat_log@",
      "user": "",
      "show": true,
      "markdown": true,
      "model": "gpt-4.1-nano",
      "temperature": "0.1",
      "max-tokens": "2000"
    },
    {
      "system": "",
      "user": "/ Continue gate\n@RADIO(\"continue_chat\", \"Continue chatting?\", \"Yes|No\")@",
      "show": true,
      "model": null
    },
    {
      "system": "",
      "user": "/ Route continue\n@JUMP(\"@MAP(\\\"@RADIO(continue_chat)@\\\", \\\"Yes|No\\\", \\\"@TN(\\\"1\\\")@|@TN(\\\"3\\\")@|@TN(\\\"3\\\")@\\\")@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Accumulate chat\n@UPJ(\"chat_log\", \"{\\\"user\\\": \\\"@TU@TN(\\\"-3\\\")@@\\\", \\\"bot\\\": \\\"@TR@TN(\\\"-3\\\")@@\\\"}\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Loop back\n@JUMP(\"@TN(\\\"-4\\\")@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Exit message\nChat session ended. Thank you for using the LLM Wiki Chat.",
      "show": true,
      "markdown": true,
      "model": null
    }
  ]
}
```

notable issues/Error:
- cannot update sources properly.
  - function argument linting issue (keeps adding `\` and unnecessary double quotes in the arguments); seems not following `linter.md` and/or `protocol.md` due to excessive context length (explicitly stated in gemini response.)
- code fix trial worsened the code corruption
  - `@RADIO` arguement errors with unnecessary double quotes and `\` $\rightarrow$ possibly cause: the model keeps following HTML parsing rules, not CAFA-specific linter and protocol.
  - due to this problem, I was not able to proceed with the model's coding performance evaluation.


## Coding test: gemini-3.1 pro standard thinking model
### Simple Quiz Agent
Output code:
```json
{
  "options": {
    "title": "AoA Framework Quiz Agent",
    "name": "AoA Assessment Agent",
    "brief": "An iterative quiz agent utilizing an AoA 'sandwich' architecture for rubric-based grading.",
    "description": "This agent presents open-ended questions, captures responses, evaluates them against a strict rubric using an LLM, and dynamically tracks the user's score.",
    "greeting": "Welcome to the AoA Assessment! Please answer the following questions comprehensively.",
    "params": {
      "QUESTIONS": {
        "org": "Explain the significance of the Turing Test.|What is the primary function of a Large Language Model?",
        "cond": "SELF",
        "desc": "List of open-ended quiz question stems."
      },
      "RUBRICS": {
        "org": "Must mention the imitation game and indistinguishability from human intelligence.|Must mention next-token prediction and generative capabilities.",
        "cond": "LINK(QUESTIONS)",
        "desc": "Evaluation rubrics strictly linked to each question stem."
      },
      "TOTAL_QUESTIONS": {
        "org": "2",
        "cond": "SELF",
        "desc": "Total number of questions to loop through."
      },
      "SCORE": {
        "org": "0",
        "cond": "SELF",
        "desc": "Dynamic score tracker."
      }
    }
  },
  "prompts": [
    {
      "system": "",
      "user": "/ Setup REPEAT loop\n@REPEAT(\"@TN(1)@\", \"@TN(3)@\", \"@TOTAL_QUESTIONS@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Present Question\n@TEXTAREA(\"ans_@R_i@\", \"Question @R_i@ of @TOTAL_QUESTIONS@:\n\n@QUESTIONS[@R_i@]@\")@",
      "show": true,
      "model": null
    },
    {
      "system": "You are a strict rubric grader. Evaluate the user's answer against this rubric: @RUBRICS[@R_i@]@. If the answer adequately meets the criteria, output Correct. Otherwise, output Incorrect.",
      "user": "Question: @QUESTIONS[@R_i@]@\nUser Answer: @TEXTAREA(ans_@R_i@)@",
      "show": true,
      "model": "gpt-4.1-nano",
      "temperature": "0.1",
      "max-tokens": "100",
      "output-values": "Correct|Incorrect"
    },
    {
      "system": "",
      "user": "/ Update Score using indexed loop results\n@SET(\"SCORE\", \"@EVAL(\"@SCORE@ + @MAP(\"@TR@TN(-1)@[@R_i@]@\", \"Correct\", \"1|0\")@\")@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Final Score Report\n## Assessment Complete!\n\nYour final score is **@SCORE@** out of **@TOTAL_QUESTIONS@**.",
      "show": true,
      "markdown": true,
      "model": null
    }
  ]
}
```
Error: no outstanding error; it outputs the fixed version of gemini-3.1 pro extended thinking model's output.

Seems to generate more succinct, clean code when using standard model than thinking model with less error margin.

### Simple Quiz Generator Agent

Code output:
```json
{
  "options": {
    "title": "AoA Generative Quiz Maker (Revised)",
    "brief": "Configurable, AI-generated assessment loop with concurrency-safe scoring.",
    "name": "Dynamic Quiz Agent Safe-State",
    "description": "This agent configures a dynamic quiz based on user topics, generates questions on the fly, evaluates constructed responses, and routes calculations cleanly to respect turn dependencies.",
    "greeting": "Welcome to the Generative Quiz Agent! Let's set up your custom assessment.",
    "keep-in-app-cafakey": false,
    "is-template": false,
    "is-public": false,
    "params": {
      "SCORE": {
        "org": "2",
        "cond": "SELF",
        "desc": ""
      },
      "TEMP_EVAL": {
        "org": "1",
        "cond": "SELF",
        "desc": ""
      },
      "topic": {
        "org": "{\n  \"id\": \"topic\",\n  \"label\": \"Enter the Quiz Topic or Reference Data:\",\n  \"response\": \"상식\"\n}",
        "cond": "",
        "desc": ""
      },
      "diff": {
        "org": "{\n  \"id\": \"diff\",\n  \"question\": \"Select the difficulty level:\",\n  \"choices\": [\n    \"Easy\",\n    \"Medium\",\n    \"Hard\"\n  ],\n  \"textboxLabel\": \"\",\n  \"response\": \"Easy\",\n  \"userResponse\": \"Easy\"\n}",
        "cond": "",
        "desc": ""
      },
      "num_q": {
        "org": "{\n  \"id\": \"num_q\",\n  \"question\": \"Select the number of questions:\",\n  \"choices\": [\n    \"2\",\n    \"3\",\n    \"4\",\n    \"5\"\n  ],\n  \"textboxLabel\": \"\",\n  \"response\": \"2\",\n  \"userResponse\": \"2\"\n}",
        "cond": "",
        "desc": ""
      },
      "ans_1": {
        "org": "{\n  \"id\": \"ans_1\",\n  \"label\": \"Question 1 of 2 (Difficulty: Easy):\\n\\n일상 생활에서 자주 사용하는 일반 상식 중 하나로, 우리가 길을 찾거나 위치를 알려줄 때 사용하는 것이 무엇인지 설명하세요.\\n\\nYour Answer:\",\n  \"response\": \"map\"\n}",
        "cond": "",
        "desc": ""
      },
      "ans_2": {
        "org": "{\n  \"id\": \"ans_2\",\n  \"label\": \"Question 2 of 2 (Difficulty: Easy):\\n\\n일상생활에서 자주 접하는 상식 중 하나인 \\\"지구가 태양을 도는 이유\\\"에 대해 간단히 설명해보세요.\\n\\nYour Answer:\",\n  \"response\": \"공전\"\n}",
        "cond": "",
        "desc": ""
      }
    }
  },
  "prompts": [
    {
      "system": "",
      "user": "/ Configure Topic\n@TEXTAREA(\"topic\", \"Enter the Quiz Topic or Reference Data:\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ Configure Difficulty\n@RADIO(\"diff\", \"Select the difficulty level:\", \"Easy|Medium|Hard\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ Configure Count\n@RADIO(\"num_q\", \"Select the number of questions:\", \"2|3|4|5\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ Setup Loop\n@REPEAT(\"@TN(1)@\", \"@TN(5)@\", \"@RADIO(num_q)@\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": false,
      "show": false,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "You are an expert assessment creator. Generate exactly ONE open-ended question based on the topic. Do not provide the answer. Output only the question text.",
      "user": "Topic: @TEXTAREA(topic)@\nDifficulty: @RADIO(diff)@\nQuestion Number: @R_i@ of @RADIO(num_q)@",
      "temperature": "0.7",
      "max-tokens": "150",
      "send-mail": false,
      "markdown": false,
      "show": false,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ Ask Question\n@TEXTAREA(\"ans_@R_i@\", \"Question @R_i@ of @RADIO(num_q)@ (Difficulty: @RADIO(diff)@):\n\n@TR@TN(-1)@[@R_i@]@\n\nYour Answer:\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "You are a strict quiz grader. Evaluate the user's answer against the provided question. If the user's answer is accurate and sufficient, output exactly Correct. If not, output exactly Incorrect.",
      "user": "Question: @TR@TN(-2)@[@R_i@]@\nUser Answer: @TEXTAREA(ans_@R_i@)@",
      "temperature": "0.1",
      "max-tokens": "50",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": "Correct|Incorrect"
    },
    {
      "system": "",
      "user": "/ Map LLM Evaluation\n@SET(\"TEMP_EVAL\", \"@MAP(\"@TR@TN(-1)@[@R_i@]@\", \"Correct\", \"1|0\")@\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": false,
      "show": false,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ Update Score\n@SET(\"SCORE\", \"@EVAL(\"@SCORE@ + @TEMP_EVAL@\")@\")@",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": false,
      "show": false,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ Final Report\n## Quiz Complete!\n\nYour final score is **@SCORE@** out of **@RADIO(num_q)@**.\n\nThank you for taking the custom @TEXTAREA(topic)@ assessment.",
      "temperature": "",
      "max-tokens": "",
      "send-mail": false,
      "markdown": true,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    }
  ]
}
```
Error:<br>
    1. argument error<br> 
        - `@RADIO@`: concatenated `question` and `answer choice` arguements as one; needed to separate<br>
        - `@REPEAT@`: repeating number argument error; cannot import the result of previous turn but import the `@RADIO@` input.<br>
    2. Input control<br>
        - need inputs directly from the function we used (e.g. `@RADIO(diff)@`, instead of hard-coded turn result `@TR1@`)

Error correction via prompt:
with only 2 turns of conversation with the model (assess the problem and fix the code accordingly), it fixed the exact errors above and function well.

### OMG Quiz Agent
Output Code:
```json
{
  "options": {
    "title": "Dynamic Quiz Agent with Automatic Scoring",
    "name": "OMG Dynamic Quiz Agent",
    "description": "Administers an adaptive quiz by shuffling questions while keeping options linked. Scores are calculated deterministically.",
    "greeting": "Welcome to the Dynamic Quiz! Let's get started.",
    "brief": "An OMG-framework quiz that dynamically scores and evaluates answers.",
    "params": {
      "QUESTIONS": {
        "org": "What is the capital of France?|What is the chemical symbol for water?|What is 5 * 6?",
        "cond": "SHUFFLE",
        "desc": "The primary stems for the quiz."
      },
      "OPT_A": {
        "org": "Berlin|CO2|25",
        "cond": "LINK(QUESTIONS)",
        "desc": "First multiple choice option."
      },
      "OPT_B": {
        "org": "Paris|H2O|30",
        "cond": "LINK(QUESTIONS)",
        "desc": "Second multiple choice option."
      },
      "OPT_C": {
        "org": "Madrid|O2|35",
        "cond": "LINK(QUESTIONS)",
        "desc": "Third multiple choice option."
      },
      "ANSWERS": {
        "org": "Paris|H2O|30",
        "cond": "LINK(QUESTIONS)",
        "desc": "Correct answers linked to stems."
      },
      "TOTAL_QUESTIONS": {
        "org": "3",
        "cond": "SELF",
        "desc": "Number of questions to ask."
      },
      "USER_SCORE": {
        "org": "0",
        "cond": "SELF",
        "desc": "Tracks the cumulative score of the user."
      },
      "TEMP_SCORE": {
        "org": "0",
        "cond": "SELF",
        "desc": "Temporary holding variable for evaluating each answer."
      }
    }
  },
  "prompts": [
    {
      "system": "",
      "user": "/ Setup Quiz Loop\n@REPEAT(\"@TN(\\\"1\\\")@\", \"@TN(\\\"3\\\")@\", \"@TOTAL_QUESTIONS@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Display Question\nQuestion @R_i@:\n@RADIO(\"ans\", \"@QUESTIONS[@R_i@]@\", \"@OPT_A[@R_i@]@|@OPT_B[@R_i@]@|@OPT_C[@R_i@]@\")@",
      "show": true,
      "markdown": true,
      "model": null
    },
    {
      "system": "",
      "user": "/ Grade Response\n@SET(\"TEMP_SCORE\", \"@MAP(\\\"@TR2[@R_i@]@\\\", \\\"@ANSWERS[@R_i@]@\\\", \\\"1|0\\\")@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Update Score\n@SET(\"USER_SCORE\", \"@EVAL(\\\"@USER_SCORE@ + @TEMP_SCORE@\\\")@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Final Summary\n**Quiz Complete!**\n\nYour final score is: **@USER_SCORE@ / @TOTAL_QUESTIONS@**.",
      "show": true,
      "markdown": true,
      "model": null
    }
  ]
}
```

Notable issue/Errors:
- linter issue
  - consistently shows parsing errors (using `\` for every arguments of the function and unnecessary double quotes that prevent the engine to read the code properly)
  - code fix did not happen after a few fix turns
- seems to follow OMG Framework well


### Mock LLM Wiki on CAFA Agents
Prompt: 
refer `PROMPT.md` at `User_import/mock_wiki_CAFA`

#### Output codes:
1. Architecture
```json
{
  "options": {
    "title": "LLM Wiki Builder",
    "name": "Wiki_Builder",
    "brief": "Authoring tool to ingest sources and generate an LLM Wiki.",
    "description": "Agent A for building an interlinked wiki from raw sources.",
    "greeting": "Welcome to the LLM Wiki Builder. Please select an action.",
    "params": {
      "raw_curr_idx": { "org": "0", "cond": "SELF", "desc": "Current source count snapshot" },
      "raw": { "org": "[]", "cond": "SELF", "desc": "JSON array of raw sources" },
      "raw_name": { "org": "[]", "cond": "SELF", "desc": "JSON array of source titles" },
      "wiki": { "org": "{}", "cond": "SELF", "desc": "Nested JSON KB for wiki pages" },
      "wiki_log": { "org": "[]", "cond": "SELF", "desc": "Log of indexing actions" },
      "wiki_index": { "org": "", "cond": "SELF", "desc": "Text index of the wiki" },
      "page_format": { "org": "# Title\n\n## Key Takeaways\n\n## Content\n", "cond": "SELF", "desc": "Template for generated pages" },
      "Agent_Config": { "org": "{\"Identity\": \"Wiki Author\", \"Purpose\": \"Distill and Generate\", \"Folder_structure\": \"flat\", \"rules\": \"Be objective and clear.\", \"citation_rules\": \"Cite all sources using standard referencing.\"}", "cond": "SELF", "desc": "Ontology configuration for the LLM" }
    }
  },
  "prompts": [
    {
      "user": "/ T1: Init current index\n@SET(\"raw_curr_idx\", \"@EVAL(\\\"@raw.length@\\\")@\")@",
      "show": false,
      "model": null
    },
    {
      "user": "/ T2: Main Menu\n@RADIO(\"menu_choice\", \"Select an action:\", \"Add raw sources|Lint/Audit|Launch the Runnable|End\")@",
      "show": true,
      "model": null
    },
    {
      "user": "/ T3: Router\n@JUMP(@MAP(\"@RADIO(menu_choice)@\", \"Add raw sources|Lint/Audit|Launch the Runnable|End\", \"@TN(1)@|@TN(6)@|@TN(17)@|@TN(21)@|@TN(21)@\")@)@",
      "show": false,
      "model": null
    },
    {
      "user": "/ T4: Add Title\n@TEXT(\"source_title\", \"Enter source title:\")@",
      "show": true,
      "model": null
    },
    {
      "user": "/ T5: Add Body\n@TEXTAREA(\"source_body\", \"Enter source content:\")@",
      "show": true,
      "model": null
    },
    {
      "user": "/ T6: Append Source\n@UPJ(\"raw\", \"{\\\"title\\\": \\\"@TEXT(source_title)@\\\", \\\"content\\\": \\\"@TEXTAREA(source_body)@\\\"}\")@\n@UPJ(\"raw_name\", \"\\\"@TEXT(source_title)@\\\"\")@",
      "show": false,
      "model": null
    },
    {
      "user": "/ T7: Add More Gate\n@RADIO(\"add_more\", \"Add another source?\", \"Yes|No\")@",
      "show": true,
      "model": null
    },
    {
      "user": "/ T8: Route Add More\n@JUMP(@MAP(\"@RADIO(add_more)@\", \"Yes|No\", \"@TN(-4)@|@TN(1)@|@TN(1)@\")@)@",
      "show": false,
      "model": null
    },
    {
      "system": "Rules: @Agent_Config.rules@\nCitation: @Agent_Config.citation_rules@\nList key takeaways from the provided sources.",
      "user": "Sources:\n@raw@",
      "show": true,
      "model": "gpt-4.1-nano",
      "temperature": "0.5",
      "max-tokens": "2000",
      "markdown": true
    },
    {
      "user": "/ T10: Revise Junction\n@RADIO(\"revise_choice\", \"Select action:\", \"Continue|Revise|Menu\")@",
      "show": true,
      "model": null
    },
    {
      "user": "/ T11: Route Revise\n@JUMP(@MAP(\"@RADIO(revise_choice)@\", \"Continue|Revise|Menu\", \"@TN(4)@|@TN(-2)@|@TN(1)@|@TN(1)@\")@)@",
      "show": false,
      "model": null
    },
    {
      "user": "/ T12: Rollback Loop\n@REPEAT(@TN(1)@, @TN(1)@, \"@EVAL(\\\"@raw_name.length@ - @raw_curr_idx@\\\")@\")@",
      "show": false,
      "model": null
    },
    {
      "user": "/ T13: DELJ Tail\n@DELJ(\"raw\", \"@EVAL(\\\"@raw_name.length@ + 1 - @R_i@\\\")@\")@\n@DELJ(\"raw_name\", \"@EVAL(\\\"@raw_name.length@ + 1 - @R_i@\\\")@\")@",
      "show": false,
      "model": null
    },
    {
      "user": "/ T14: Back to Menu (snapshot state refresh)\n@JUMP(@TN(-13)@)@",
      "show": false,
      "model": null
    },
    {
      "user": "/ T15: Generation Loop\n@REPEAT(@TN(1)@, @TN(2)@, \"@raw.length@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "Format:\n@page_format@\nWrite a wiki page using the specified format.",
      "user": "Source:\n@raw[@R_i@]@\nTakeaways:\n@TR@TN(-7)@[@R_i@]@",
      "show": true,
      "model": "gpt-4.1-nano",
      "temperature": "0.5",
      "max-tokens": "2000",
      "markdown": true
    },
    {
      "user": "/ T17: Store Page\n@UPJ(\"wiki\", \"{\\\"@raw_name[@R_i@]@\\\": \\\"@TR@TN(-1)@[@R_i@]@\\\"}\")@",
      "show": false,
      "model": null
    },
    {
      "system": "Regenerate the wiki index based on the accumulated pages.",
      "user": "Wiki:\n@wiki@",
      "show": true,
      "model": "gpt-4.1-nano",
      "temperature": "0.5",
      "max-tokens": "2000",
      "markdown": true
    },
    {
      "user": "/ T19: Update Index and Log\n@SET(\"wiki_index\", \"@TR@TN(-1)@@\")@\n@UPJ(\"wiki_log\", \"{\\\"date\\\": \\\"@NOW@\\\", \\\"action\\\": \\\"Index rebuilt\\\"}\")@",
      "show": false,
      "model": null
    },
    {
      "user": "/ T20: Handoff\n@RADIO(\"handoff_choice\", \"Export and launch chat, or return to menu?\", \"Chat|Menu\")@",
      "show": true,
      "model": null
    },
    {
      "user": "/ T21: Route Handoff\n@JUMP(@MAP(\"@RADIO(handoff_choice)@\", \"Chat|Menu\", \"@TN(1)@|@TN(-20)@|@TN(1)@\")@)@",
      "show": false,
      "model": null
    },
    {
      "user": "/ T22: Export Bundle\n@SET(\"export_id\", \"@EXPORT(\\\"Agent_Config|raw|wiki|wiki_index|wiki_log|page_format\\\", \\\"runner_handoff\\\")@\")@",
      "show": false,
      "model": null
    },
    {
      "user": "/ T23: Launch Link\nReady to launch.\n<a href=\"?ID_ID=@export_id@\">Launch Runner</a>",
      "show": true,
      "model": null
    },
    {
      "user": "/ T24: Terminus\n@END@",
      "show": false,
      "model": null
    }
  ]
}
```
2. Runner
```json
{
  "options": {
    "title": "LLM Wiki Chat Runner",
    "name": "Wiki_Runner",
    "brief": "RAG chat over exported wiki.",
    "description": "Agent B for querying wiki pages.",
    "greeting": "Welcome to the Wiki Chat.",
    "params": {
      "Q_answer_rule": { "org": "Read index -> read pages -> synthesize -> cite -> say if absent -> offer to file good answers back.", "cond": "SELF", "desc": "Rule for Q&A" },
      "chat_log": { "org": "[]", "cond": "SELF", "desc": "Accumulated chat history" }
    }
  },
  "prompts": [
    {
      "user": "/ T1: Import Wiki Bundle\n@IMPORT(\"@ID_ID@\")@",
      "show": false,
      "model": null
    },
    {
      "user": "/ T2: Sanity Echo\n@SET(\"sanity\", \"Imported @raw.length@ items\")@",
      "show": false,
      "model": null
    },
    {
      "user": "/ T3: Greeting\nReady to answer questions based on the wiki.",
      "show": true,
      "model": null
    },
    {
      "system": "@Q_answer_rule@\n\nWiki Index:\n@wiki_index@\n\nWiki Content:\n@wiki@\n\nChat Log:\n@chat_log@",
      "user": "",
      "show": true,
      "model": "gpt-4.1-nano",
      "temperature": "0.1",
      "max-tokens": "2000",
      "markdown": true
    },
    {
      "user": "/ T5: Continue Gate\n@RADIO(\"continue_chat\", \"Continue chat?\", \"Yes|No\")@",
      "show": true,
      "model": null
    },
    {
      "user": "/ T6: Route Continue\n@JUMP(@MAP(\"@RADIO(continue_chat)@\", \"Yes|No\", \"@TN(1)@|@TN(3)@|@TN(3)@\")@)@",
      "show": false,
      "model": null
    },
    {
      "user": "/ T7: UPJ Chat Log\n@UPJ(\"chat_log\", \"{\\\"user\\\": \\\"@TU4@\\\", \\\"bot\\\": \\\"@TR4@\\\"}\")@",
      "show": false,
      "model": null
    },
    {
      "user": "/ T8: Loop Back\n@JUMP(@TN(-4)@)@",
      "show": false,
      "model": null
    },
    {
      "user": "/ T9: Exit Message\nSession Ended. Thank you.",
      "show": true,
      "model": null
    }
  ]
}
```
notable issues/Errors:
- cannot update sources properly.
  - function argument linting issue (keeps adding `\` and unnecessary double quotes in the arguments); seems not following `linter.md` and/or `protocol.md` due to excessive context length (explicitly stated in gemini response.)
- code fix with additional prompt failed; possible due to out-of-context length that can be processed in web version.
  - due to this problem, I was not able to test the model's coding performance (technical issue on gemini side)
- response time: $\approx$ 1.5 - 2 min.



