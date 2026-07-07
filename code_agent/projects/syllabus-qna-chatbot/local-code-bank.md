<!-- code-bank match (score=36, keywords: answer, chat, chatbot, conversation, exit, loop, question, syllabus) -->
# Syllabus Q&A Chatbot – Ontology-Grounded Conversational Agent

## Metadata

- Frameworks: OMG (Ontology Model-centered Generation), IMPACT
    
- Complexity: Intermediate
    
- Primary Function: Syllabus-bounded Question Answering
    
- Key Symbolic Commands: REPEAT, RADIO, MAP, JUMP
    
- Key Concepts: Ontology grounding, conversational memory, controlled exit, teaching-assistant agent
    

## 1. Background and Objective

The Syllabus Q&A Chatbot is a domain-bounded conversational agent designed to act as an automated teaching assistant (TA). Its primary objective is to answer student questions exclusively using the content of a provided syllabus, without hallucination or external inference.

This agent demonstrates a practical implementation of Ontology Model-centered Generation (OMG):

- The syllabus is embedded as a structured ontology model (OM_Syllabus).
    
- The LLM is constrained by a strict persona to reference only that ontology and prior conversation history.
    
- Questions outside the syllabus scope are explicitly refused, with redirection to the instructor.
    
- A multi-turn conversational loop is maintained using the IMPACT framework.
    
- A user-controlled exit mechanism ensures predictable and safe termination.
    

This pattern is ideal for academic support bots, policy assistants, and compliance-critical Q&A systems.

## 2. Full Agent Code

{

    "options": {

        "title": "Syllabus Q&A Chatbot",

        "brief": "A chatbot that answers questions based on a provided syllabus.",

        "name": "Syllabus Chatbot",

        "description": "This agent acts as a tutor, answering student questions about course policies, schedules, and grading criteria based strictly on a provided syllabus.",

        "greeting": "Hello! I am a TA chatbot for this course. I can answer questions based on the provided syllabus. What would you like to know?",

        "params": {

            "CHATBOT_PERSONA": {

                "org": "You are a helpful and polite teaching assistant. Answer student questions using only the information in OM_Syllabus and the conversation history. If the question cannot be answered using the syllabus, politely say so and direct the student to contact the instructor at smith(at)sample.edu.",

                "cond": "SELF"

            },

            "OM_Syllabus": {

                "org": "## Course Information\n- Course Name: Introduction to Statistics\n- Instructor: Professor Smith\n- Instructor Email: smith(at)sample.edu\n- Meeting Time: MWF, 10:00 AM - 10:50 AM\n- Classroom: Building A, Room 101\n- Office Hours: Tuesday, 2:00 PM - 4:00 PM\n- Office Location: Building C, Room 303\n\n## Grading Breakdown\n- Midterm Exam: 40%\n- Final Exam: 40%\n- Assignments: 20%\n\n## Assignments\n- All assignments must be submitted online.\n- Due Date: Every Friday at 6:00 PM.",

                "cond": "SELF"

            },

            "MAX_CHAT": {

                "org": "10",

                "cond": "SELF"

            }

        }

    },

    "prompts": [

        {

            "user": "/ Initialize conversational loop\n@REPEAT(2, 6, @MAX_CHAT@)@",

            "show": false

        },

        {

            "system": "@CHATBOT_PERSONA@\n\nSyllabus:\n@OM_Syllabus@\n\nConversation History:\n@TR3@",

            "user": "",

            "temperature": "0.5",

            "max-tokens": "2000",

            "markdown": true,

            "show": true,

            "model": "gpt-4.1-nano"

        },

        {

            "user": "/ Log conversation history\nTurn @R_i@ {\nUser: @TU2[@R_i@]@\nBot: @TR2[@R_i@]@\n}",

            "show": false

        },

        {

            "user": "/ Ask whether to continue\n@RADIO(\"continue_choice\", \"Would you like to continue the conversation?\", \"Yes|No\")@",

            "show": true

        },

        {

            "user": "/ Route based on choice\n@JUMP(@MAP(\"@RADIO(continue_choice)@\", \"Yes\", \"6|7\")@)@",

            "show": false

        },

        {

            "user": "Okay, let’s continue.",

            "show": true

        },

        {

            "user": "The conversation has ended. Please click 'Start' to begin a new chat.",

            "markdown": true,

            "show": true

        }

    ]

}

  

## 3. Knowledge and Configuration (options.params)

### Core Parameters

|   |   |
|---|---|
|Parameter|Purpose|
|CHATBOT_PERSONA|Enforces syllabus-only answering and polite refusal of out-of-scope questions|
|OM_Syllabus|The ontology model containing all allowed knowledge|
|MAX_CHAT|Upper bound on conversational turns|

The syllabus parameter functions as a read-only ontology, ensuring deterministic and auditable answers.

## 4. Execution Flow (prompts)

### Turn 1: Loop Initialization (Symbolic ⚙️)

- REPEAT(2, 6, MAX_CHAT)
    
- Defines the IMPACT conversational loop.
    

### Loop Body (Turns 2–6)

#### Turn 2: Ontology-Grounded Response (LLM 🤖)

- Injects:
    

- Persona rules
    
- Syllabus ontology
    
- Accumulated history (@TR3@)
    

- Waits for user input and generates a bounded answer.
    

#### Turn 3: History Logging (Symbolic ⚙️)

- Captures user input and agent response.
    
- Appends formatted dialogue to @TR3@.
    

#### Turn 4: Continuation Prompt (Symbolic ⚙️)

- Explicitly asks the user whether to continue.
    

#### Turn 5: Conditional Routing (Symbolic ⚙️)

- Yes → Continue loop
    
- No → Exit conversation
    

Uses MAP + JUMP for deterministic flow control.

#### Turn 6: Continuation Acknowledgment (Symbolic ⚙️)

- Provides feedback before returning to Turn 2.
    

### Turn 7: Termination Message (Symbolic ⚙️)

- Clean, user-visible end state.
    

## 5. Best Practices and Key Takeaways

- Ontology-bounded generation prevents hallucination
    
- Explicit refusal logic is as important as correct answers
    
- Conversation memory improves coherence without expanding knowledge scope
    
- User-controlled exits increase trust and usability
    

## 6. Possible Extensions

1. Multiple Ontologies: Split syllabus into policies, grading, and schedule models
    
2. Keyword Routing: Detect question type before answering
    
3. Transcript Export: Save conversation logs for instructor review
    
4. Coverage Diagnostics: Signal partial or weak syllabus support in responses
    

---

---

=====

<!-- code-bank match (score=32, keywords: chat, chatbot, conversation, loop) -->
# Essential Chatbot: IMPACT-Based Multi-Turn Conversational Loop

## Metadata

- Framework: IMPACT
    
- Complexity: Beginner–Intermediate
    
- Primary Function: Conversational Interaction
    
- Key Symbolic Commands: REPEAT, SET
    
- Key Concepts: Iterative Chat Loop, Turn Memory, Conversation Logging, System Parameters
    

## Background & Objective

- Problem Solved:  
    Single-turn chat agents cannot maintain conversational context or support sustained dialogue over multiple turns.
    
- Core Mechanism:  
    This agent implements the IMPACT (Iterative Multi-turn Process for AI Collaboration Technique) framework by using a REPEAT loop to alternate between an LLM conversation turn and a symbolic logging turn, preserving dialogue history via System Parameters.
    

## Full CAFA Agent Code

{

    "options": {

        "title": "CAFA Agent: Essential Chatbot",

        "brief": "A foundational, multi-turn chatbot that holds a conversation for a configurable number of turns.",

        "name": "Essential Chatbot",

        "description": "This is a core agent that uses a REPEAT loop to create an iterative chatbot experience. It uses a configurable parameter to determine the number of conversational turns and maintains a conversation history to provide coherent and contextual responses.",

        "greeting": "How may I help you?",

        "params": {

            "CHABOT_PERSONA": {

                "org": "You are a helpful and engaging chatbot. Your goal is to continue a conversation with the user. You must be concise and conversational.",

                "cond": "SELF",

                "desc": "Chatbot Persona"

            },

            "MAX_CHAT": {

                "org": "5",

                "cond": "SELF",

                "desc": "Maximum Number of Chat Turns"

            }

        }

    },

    "prompts": [

        {

            "user": "/ This hidden symbolic turn sets up a loop to run the conversational turns.\n@REPEAT(2, 3, @MAX_CHAT@)@",

            "show": false

        },

        {

            "system": "@CHABOT_PERSONA@\n\n- Previous conversation history:\n@TR3@",

            "user": "",

            "temperature": "0.5",

            "max-tokens": "2000",

            "show": true,

            "model": "gpt-4.1-nano"

        },

        {

            "user": "/ This hidden symbolic turn logs the full conversation history for the next turn.\nTurn @R_i@ Conversation {\n  - User: @TU2[@R_i@]@\n  - Chatbot: @TR2[@R_i@]@\n}",

            "show": false

        }

    ]

}

  

## Detailed Logic Breakdown

### Ontology Model (options.params):

- CHABOT_PERSONA:  
    A static instruction string defining the chatbot’s tone, role, and conversational constraints. Loaded into every LLM turn.
    
- MAX_CHAT:  
    Controls the total number of conversational iterations executed by the @REPEAT loop.
    

### Execution Flow (prompts array):

- Turn 1 (Symbolic): Loop Setup  
    Uses @REPEAT(2, 3, @MAX_CHAT@) to define the conversational cycle. Hidden and executes instantly.
    
- Turn 2 (LLM): Conversational Response
    

- System Prompt: Injects chatbot persona and accumulated conversation history (@TR3@).
    
- User Prompt: Empty string ("") pauses execution and waits for user input.
    
- Output: AI-generated response stored in @TR2@.
    

- Turn 3 (Symbolic): History Logging
    

- Captures user input (@TU2@) and chatbot output (@TR2@).
    
- Formats and appends dialogue into @TR3@, which serves as memory for the next loop iteration.
    
- Hidden turn; no LLM involved.
    

## Visualization Mermaid Code

graph TD

    A[Start] --> B[Turn 1: Setup REPEAT Loop]

    B --> C[Turn 2: LLM Chat Response]

    C --> D[Turn 3: Log Conversation History]

    D --> C

    C --> E[Loop Ends After MAX_CHAT]

  

## Related Questions and Instructions

### Design & Architecture Requests

- Framework Related:  
    “Create an IMPACT-based chatbot with a fixed number of turns.”
    
- Structure Related:  
    “Build a multi-turn conversational agent using REPEAT.”
    
- Complexity Related:  
    “Generate a beginner-level conversational CAFA agent.”
    

### Usage & Modification Requests

- Task Related:  
    “Adapt this chatbot to act as a tutor or customer support agent.”
    
- Reuse:  
    “Reuse this IMPACT loop with a different persona.”
    
- Bounded Changes:  
    “Increase MAX_CHAT without adding new turns.”
    

## References

- Choi, J. (2025). Essential Chatbot: IMPACT-Based Multi-Turn Conversational Loop. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---

=====

<!-- code-bank match (score=18, keywords: answer, free, loop, question) -->
# AoA Rubric Quiz Agent: Looped Symbolic-Input → LLM-Evaluation → Hidden-Control Sandwich with Loop-Indexed Verdict Scoring

## Metadata

- Framework: AoA (Architecture of Alignment / Assessment)
    
- Complexity: Intermediate–Advanced
    
- Primary Function: Assessment (constructed-response quiz + rubric scoring + dynamic running score)
    
- Key Symbolic Commands: REPEAT, TEXTAREA, SET, MAP, EVAL, TR, TN
    
- Key Concepts: Strict "Sandwich" architecture (Symbolic Input → LLM Evaluation → Hidden Control/Routing), per-iteration loop indexing of turn results via `@TR@TN(-1)@[@R_i@]@`, `output-values`-constrained verdict labels, dynamic running-score accumulator, order-linked question/rubric ontology lists
    

## Background & Objective

- Problem Solved: A free-text quiz needs (1) reliable, rubric-grounded grading of each answer and (2) a running score that updates as the learner progresses — without the score logic being corrupted by loop-result accumulation. This agent administers a fixed bank of constructed-response items, grades each answer against a rigid 4-level rubric, and maintains a dynamic `SCORE`.
    
- Core Mechanism: A single `REPEAT` loop wraps a three-turn Sandwich per question: a Symbolic Input turn presents the item and captures a `TEXTAREA` answer; an LLM Evaluation turn returns exactly one of four verdict labels (constrained by `output-values`); a hidden Control turn maps the verdict to points and updates the running `SCORE`. A final symbolic turn reports total, percentage, and a per-question breakdown.
    
- Critical Pitfall Addressed: Inside a `REPEAT` loop the previous turn's result System Parameter (`@TR@TN(-1)@@`) accumulates **all iterations'** outputs into one pipe-delimited string (e.g. after Q2: `Incorrect|Mostly Correct`). Feeding that growing string into `MAP` matches no single `value_list` entry, so it falls through to the default and the score is wrong. The fix is to index the loop result by the iteration number — `@TR@TN(-1)@[@R_i@]@` — extracting only the current iteration's verdict before `MAP`.
    

## Full CAFA Agent Code

{
  "options": {
    "title": "<b>AoA Quiz Agent</b>: Rubric-Scored Constructed Response",
    "brief": "An AoA-framework quiz that presents questions, captures free-text answers, grades each against a rigid rubric, updates a running score, and reports a final result.",
    "name": "AoA Rubric Quiz Agent",
    "description": "This agent implements the AoA (Architecture of Alignment / Assessment) framework as a strict Symbolic-Input -> LLM-Evaluation -> Hidden-Control sandwich, looped once per question via REPEAT. Each cycle presents a question (TEXTAREA capture), grades the answer against a rigid 4-level rubric, maps the verdict to points, and updates a dynamic SCORE variable. A final symbolic turn reports the total, percentage, and a per-question breakdown.",
    "greeting": "Welcome to the AoA Quiz. You will answer 3 short constructed-response questions. Each answer is graded against a rigid rubric, and your running score is tracked. Let's begin.",
    "params": {
      "TOTAL_QUESTIONS": {
        "org": "3",
        "cond": "SELF",
        "desc": "Number of questions in the quiz; drives the REPEAT loop count."
      },
      "MAX_SCORE": {
        "org": "9",
        "cond": "SELF",
        "desc": "Maximum achievable score (TOTAL_QUESTIONS x 3 points per question). Used for the final percentage."
      },
      "SCORE": {
        "org": "0",
        "cond": "SELF",
        "desc": "Dynamic running score, initialized to 0 and incremented each loop iteration by the points earned on that question."
      },
      "QUESTIONS": {
        "org": "Explain the difference between supervised and unsupervised machine learning, and give one example of each.|What is overfitting in a machine learning model, and name one technique used to reduce it?|Describe what a large language model (LLM) is, and state one genuine limitation it has.",
        "cond": "SELF",
        "desc": "The ordered bank of constructed-response questions presented one per loop iteration."
      },
      "RUBRICS": {
        "org": "Full credit requires: (a) supervised learning uses labeled data to map inputs to known outputs; (b) unsupervised learning finds structure in unlabeled data; (c) one valid example of each, such as classification or regression versus clustering or dimensionality reduction.|Full credit requires: (a) overfitting is when a model learns noise and training-specific detail so it generalizes poorly to new data; (b) one valid mitigation such as regularization, more training data, cross-validation, dropout, or early stopping.|Full credit requires: (a) an LLM is a neural network trained on large text corpora to predict and generate language; (b) one genuine limitation such as hallucination, outdated knowledge, bias, or lack of true reasoning.",
        "cond": "LINK(QUESTIONS)",
        "desc": "Rigid scoring criteria, order-linked to QUESTIONS so each rubric stays paired with its question."
      }
    }
  },
  "prompts": [
    {
      "system": "",
      "user": "/ Hidden control: loop the question sandwich (present -> evaluate -> score) once per question.\n@REPEAT(@TN(1)@, @TN(3)@, \"@TOTAL_QUESTIONS@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Symbolic Input layer: present question @R_i@ and capture the constructed response.\n## Question @R_i@ of @TOTAL_QUESTIONS@\n\n@QUESTIONS[@R_i@]@\n\n@TEXTAREA(\"answer_@R_i@\", \"Type your full answer here, then press Submit.\")@",
      "show": true,
      "model": null,
      "markdown": true
    },
    {
      "system": "You are a strict, consistent assessment grader. Score the student's answer ONLY against the provided rubric for this specific question. Use this rigid 4-level scale:\n- Fully Correct: the answer satisfies every criterion in the rubric.\n- Mostly Correct: the answer satisfies most criteria with only a minor omission or error.\n- Partially Correct: the answer satisfies some criteria but has significant gaps.\n- Incorrect: the answer is irrelevant, wrong, or misses the rubric criteria.\nDo not reward fluency, length, or unrelated facts. Output exactly one of the four labels and nothing else.",
      "user": "Question:\n@QUESTIONS[@R_i@]@\n\nScoring rubric (rigid):\n@RUBRICS[@R_i@]@\n\nStudent answer:\n@TEXTAREA(\"answer_@R_i@\")@\n\nReturn the single most accurate grade label.",
      "show": true,
      "model": "gpt-4.1-nano",
      "temperature": "0.1",
      "max-tokens": "100",
      "output-values": "Incorrect|Partially Correct|Mostly Correct|Fully Correct"
    },
    {
      "system": "",
      "user": "/ Hidden Control layer: convert this iteration's verdict to points and update the dynamic running SCORE.\n@SET(\"VERDICT_@R_i@\", \"@TR@TN(-1)@[@R_i@]@\")@\n@SET(\"POINTS_@R_i@\", \"@MAP(\"@TR@TN(-1)@[@R_i@]@\", \"Incorrect|Partially Correct|Mostly Correct|Fully Correct\", \"0|1|2|3|0\")@\")@\n@SET(\"SCORE\", \"@EVAL(\"@SCORE@ + @MAP(\"@TR@TN(-1)@[@R_i@]@\", \"Incorrect|Partially Correct|Mostly Correct|Fully Correct\", \"0|1|2|3|0\")@\")@\")@",
      "show": false,
      "model": null
    },
    {
      "system": "",
      "user": "/ Final score report (runs after the loop completes).\n# Quiz Complete\n\nYou answered **@TOTAL_QUESTIONS@** questions.\n\n**Total score: @SCORE@ / @MAX_SCORE@**\n\n**Percentage: @EVAL(\"Math.round(@SCORE@ / @MAX_SCORE@ * 100)\")@%**\n\n---\n\n### Question 1\n@QUESTIONS[1]@\n\n- **Your answer:** @TEXTAREA(\"answer_1\")@\n- **Verdict:** @VERDICT_1@ (@POINTS_1@/3)\n\n### Question 2\n@QUESTIONS[2]@\n\n- **Your answer:** @TEXTAREA(\"answer_2\")@\n- **Verdict:** @VERDICT_2@ (@POINTS_2@/3)\n\n### Question 3\n@QUESTIONS[3]@\n\n- **Your answer:** @TEXTAREA(\"answer_3\")@\n- **Verdict:** @VERDICT_3@ (@POINTS_3@/3)",
      "show": true,
      "model": null,
      "markdown": true
    }
  ]
}

## Detailed Logic Breakdown

### Ontology Model (options.params)

- QUESTIONS (SELF) and RUBRICS (LINK(QUESTIONS)): order-linked parallel lists. The link guarantees each rubric stays paired with its question even if ordering changes.
    
- TOTAL_QUESTIONS, MAX_SCORE: scalars controlling loop count and the percentage denominator.
    
- SCORE: the dynamic running score, pre-initialized to "0" in options.params (Rule 9.4) so the very first accumulation has a defined value.
    

### Execution Flow (prompts array)

- Turn 1 (Symbolic, hidden) — Loop controller: `@REPEAT(@TN(1)@, @TN(3)@, "@TOTAL_QUESTIONS@")@` loops the three-turn Sandwich (T2–T4). REPEAT is alone in its dedicated hidden turn.
    
- Turn 2 (Symbolic, visible) — **Symbolic Input layer**: displays `@QUESTIONS[@R_i@]@` and captures the answer with `@TEXTAREA("answer_@R_i@", ...)@`. Iteration-scoped variable names keep each answer separate.
    
- Turn 3 (LLM, visible) — **LLM Evaluation layer**: grades the captured answer against `@RUBRICS[@R_i@]@`. `output-values` constrains the response to exactly one of four labels, making it safe for downstream MAP.
    
- Turn 4 (Symbolic, hidden) — **Hidden Control layer**: indexes this iteration's verdict with `@TR@TN(-1)@[@R_i@]@`, stores `VERDICT_@R_i@`, maps the verdict to `POINTS_@R_i@`, and updates the running `SCORE` via `EVAL`. The SCORE accumulator reads the prior-iteration value (a previous turn execution) and re-runs MAP inline rather than referencing the same-turn `POINTS_@R_i@`, so no same-turn dependency is violated.
    
- Turn 5 (Symbolic, visible) — Final report: shows total, percentage (`@EVAL("Math.round(@SCORE@ / @MAX_SCORE@ * 100)")@`), and a per-question breakdown.
    

### The Loop-Indexing Trick (`@TR@TN(-1)@[@R_i@]@`)

Within a REPEAT loop the engine appends each iteration's turn result to a single pipe-delimited System Parameter. Reading `@TR@TN(-1)@@` on iteration 2 therefore returns `verdict1|verdict2`, which MAP cannot match. Indexing with the current iteration number `[@R_i@]` returns only `verdict2`. Always index loop-internal `TR`/`TU` results when feeding them to MAP, INDEX, EVAL, or SET.

## Visualization Mermaid Code

graph TD

    A[Start] --> B[T1 Symbolic/Hidden: REPEAT T2-T4 x TOTAL_QUESTIONS]

    B --> C[T2 Symbolic/Visible: Present Q_Ri + TEXTAREA capture]

    C --> D[T3 LLM/Visible: Grade vs rubric, output-values verdict label]

    D --> E[T4 Symbolic/Hidden: index TR by R_i, MAP to points, update SCORE]

    E --> C

    B --> F[T5 Symbolic/Visible: Final score report + percentage]

    F --> G[End]

## Modification Recipes

- To Change Question Count: edit TOTAL_QUESTIONS and MAX_SCORE (= count x 3), extend QUESTIONS/RUBRICS, and add matching rows to the T5 report. The loop logic is unchanged.
    
- To Change the Rubric Scale: edit the four labels in T3's system prompt and `output-values`, and keep the MAP value_list/return_list in T4 in sync (return_list must be N+1 with the default last).
    
- To Add Per-Question Feedback: insert a visible LLM turn after T3 (no `output-values`) that explains the verdict; keep the scoring turn separate so grading stays machine-parseable.
    
- To Randomize Item Order: set QUESTIONS `cond` to "SHUFFLE"; RUBRICS stays "LINK(QUESTIONS)" so pairing is preserved.
    

## Related Questions and Instructions

### Design and Architecture Requests

- Framework Related: “Build an AoA quiz with a strict Symbolic-Input → LLM-Evaluation → Hidden-Control sandwich looped via REPEAT.”
    
- Structure Related: “Show how to read a single loop iteration's LLM result with `@TR@TN(-1)@[@R_i@]@` before MAP.”
    
- Complexity Related: “Create a rubric-scored constructed-response quiz with a dynamic running score.”
    

### Usage and Modification Requests

- Task Related: “Swap the ML questions for a history quiz without changing the loop architecture.”
    
- Reuse: “Reuse the verdict→points MAP + SCORE accumulator for any rubric quiz.”
    
- Bounded Changes: “Add a fourth question without altering the scoring logic.”
    

## References

- Choi, J. (2025). AoA Rubric Quiz Agent: Looped Symbolic-Input → LLM-Evaluation → Hidden-Control Sandwich with Loop-Indexed Verdict Scoring. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.

=====

<!-- code-bank match (score=17, keywords: conversation, loop, question) -->
# AI-to-AI Monitored Conversation: Two-Agent Simulation with Human Stop/Continue Gate and Supervisory Analysis

## Metadata

- Framework: RISE (looped multi-agent exchange with REPEAT, iteration index @R_i@, and a mid-loop “evaluation gate” via monitor control)
    
- Complexity: Advanced
    
- Primary Function: Simulation & Supervision (AI-to-AI dialogue generation with human monitoring and final analysis)
    
- Key Symbolic Commands: TEXTAREA, REPEAT, TN, TR, EVAL, RADIO, MAP, JUMP
    
- Key Concepts: Dual personas (Counselor/Counselee), human-in-the-loop checkpoint, conditional loop break (Stop → jump to analysis), cumulative transcript logging across iterations
    

## Background & Objective

- Problem Solved: Pure AI-to-AI simulations can run uncontrolled and lose auditability. This agent adds (1) a human monitor checkpoint each turn and (2) deterministic transcript accumulation, enabling supervised simulations for training, testing, and review.
    
- Core Mechanism: The user supplies the Counselee’s initial problem, a @REPEAT loop runs Counselor→Counselee→Monitor→Router→Logger, the monitor can terminate early via “Stop” (breaking out to final analysis), and the full transcript is synthesized by an analysis persona.
    

## Full CAFA Agent Code

{  
"options": {  
"title": "AI Counselor & Counselee Session (Monitored)",  
"name": "AI Counselor Session (Monitored)",  
"description": "An agent that simulates a monitored conversation between an AI Counselor and Counselee, allowing the user to stop or continue the session at each step.",  
"greeting": "Welcome. Please describe the problem or topic you would like the AI Counselee to discuss with the AI Counselor.",  
"params": {  
"COUNSELOR_PERSONA": {  
"org": "You are a thoughtful and empathetic AI Counselor. Your goal is to help the Counselee explore their feelings and thoughts about the problem they are facing. Ask open-ended, insightful, and supportive questions. Do not give advice, but rather guide them to find their own understanding.",  
"cond": "SELF",  
"desc": "Defines the Counselor's persona."  
},  
"COUNSELEE_PERSONA": {  
"org": "You are an AI Counselee. You will be given a problem to discuss. Respond honestly and reflectively to the Counselor's questions. Base your personality and responses on the initial problem description.",  
"cond": "SELF",  
"desc": "Defines the Counselee's persona."  
},  
"MAX_TURNS": {  
"org": "5",  
"cond": "SELF",  
"desc": "The number of back-and-forth exchanges in the session."  
},  
"ANALYSIS_PERSONA": {  
"org": "You are a clinical supervisor reviewing a counseling session. Analyze the full conversation between the Counselor and Counselee. Summarize the key themes discussed, the Counselor's approach, and the Counselee's progress or insights.",  
"cond": "SELF",  
"desc": "The persona for the final analysis of the session."  
}  
}  
},  
"prompts": [  
{  
"user": "/ This turn captures the initial problem from the user.\n@TEXTAREA("counselee_problem", "Please describe the problem for the Counselee:")@",  
"show": true,  
"model": null  
},  
{  
"user": "/ This hidden turn sets up the conversation loop.\n@REPEAT(@TN(1)@, @TN(5)@, @MAX_TURNS@)@",  
"show": false,  
"model": null  
},  
{  
"system": "@COUNSELOR_PERSONA@",  
"user": "This is a counseling session. Here is the context:\n\n- Initial Problem: "@TEXTAREA(counselee_problem)@"\n\n- Conversation History So Far:\n@TR@TN(4)@[@EVAL("@R_i@-1")@]@\n\nPlease continue the conversation by asking your next question.",  
"temperature": "0.7",  
"max-tokens": "2000",  
"show": true,  
"model": "gpt-4.1-nano",  
"markdown": true  
},  
{  
"system": "@COUNSELEE_PERSONA@",  
"user": "You are in a counseling session. Here is the context:\n\n- Your Initial Problem: "@TEXTAREA(counselee_problem)@"\n\n- Conversation History So Far:\n@TR@TN(3)@[@EVAL("@R_i@-1")@]@\n\n- The Counselor just said to you:\n"@TR@TN(-1)@[@R_i@]@"\n\nPlease provide your response.",  
"temperature": "0.7",  
"max-tokens": "2000",  
"show": true,  
"model": "gpt-4.1-nano",  
"markdown": true  
},  
{  
"user": "/ This turn asks the monitor if the session should continue.\n@RADIO("monitor_choice_@R_i@", "Monitor: Do you want to continue the session?", "Continue|Stop")@",  
"show": true,  
"model": null  
},  
{  
"user": "/ This hidden turn acts as a router. If the monitor selects 'Stop', it jumps to the final analysis turn.\n@JUMP(@MAP("@RADIO(monitor_choice_@R_i@)@", "Stop", "@TN(2)@", "")@)@",  
"show": false,  
"model": null  
},  
{  
"user": "/ This hidden turn logs the full, cumulative history for the next loop.\n@TR@TN(0)@[@EVAL("@R_i@-1")@]@\n\nTurn @R_i@:\n- Counselor: @TR@TN(-4)@[@R_i@]@\n- Counselee: @TR@TN(-3)@[@R_i@]@",  
"show": false,  
"model": null  
},  
{  
"system": "@ANALYSIS_PERSONA@",  
"user": "Please analyze the following counseling session transcript.\n\n### Initial Problem\n@TEXTAREA(counselee_problem)@\n\n### Full Transcript\n@TR@TN(-1)@@",  
"temperature": "0.1",  
"max-tokens": "4000",  
"show": true,  
"model": "gpt-4.1-nano",  
"markdown": true  
}  
]  
}

## Detailed Logic Breakdown

### Ontology Model (options.params):

- COUNSELOR_PERSONA: Controls questioning style (empathetic, open-ended, non-advice).
    
- COUNSELEE_PERSONA: Controls reflective respondent behavior anchored to the initial problem.
    
- MAX_TURNS: Upper bound on loop iterations (conversation “budget”).
    
- ANALYSIS_PERSONA: Defines supervisory synthesis format at the end.
    

### Execution Flow (prompts array):

- Turn 1 (Symbolic, visible): Scenario seed (human)
    

- Captures the initial counselee problem via @TEXTAREA("counselee_problem", ...)@.
    

- Turn 2 (Symbolic, hidden): Loop setup
    

- @REPEAT(@TN(1)@, @TN(5)@, @MAX_TURNS@)@ repeats Turns 3–7 for up to MAX_TURNS iterations.
    

- Turn 3 (LLM, visible; in loop): Counselor generates next question
    

- Receives initial problem + “conversation so far” (pulled from the logger’s stored history using indexed access with @EVAL("@R_i@-1")@).
    

- Turn 4 (LLM, visible; in loop): Counselee responds
    

- Receives the problem + history + the counselor’s latest utterance and produces a reflective reply.
    

- Turn 5 (Symbolic, visible; in loop): Monitor checkpoint
    

- Human chooses Continue/Stop using a per-iteration key: monitor_choice_@R_i@.
    

- Turn 6 (Symbolic, hidden; in loop): Conditional break router
    

- If Stop, @JUMP(...)@ routes to the final analysis turn; if Continue, execution falls through.
    

- Turn 7 (Symbolic, hidden; in loop): Transcript accumulator
    

- Appends the latest counselor + counselee lines to the cumulative transcript for the next iteration’s context.
    

- Turn 8 (LLM, visible): Supervisory analysis
    

- Uses ANALYSIS_PERSONA to summarize themes, counselor approach, and counselee progress, consuming the fully accumulated transcript.
    

## Visualization Mermaid Code

graph TD

  A[Start] --> B[T1 (Symbolic): TEXTAREA counselee_problem]

  B --> C[T2 (Hidden): REPEAT loop setup (Turns 3–7) up to MAX_TURNS]

  

  C --> D[T3 (LLM): Counselor asks next question<br/>Inputs: problem + prior transcript]

  D --> E[T4 (LLM): Counselee responds<br/>Inputs: problem + transcript + last counselor line]

  E --> F[T5 (Symbolic): Monitor RADIO Continue/Stop]

  F --> G{T6 (Hidden): If Stop?}

  G -- Continue --> H[T7 (Hidden): Append counselor+counselee to cumulative transcript]

  H --> D

  

  G -- Stop --> I[T8 (LLM): Supervisory analysis (ANALYSIS_PERSONA)]

  C -->|Loop ends naturally| I

  I --> J[End]

  

## Related Questions and Instructions

### Design & Architecture Requests

- Framework Related:  
    “Generate a monitored AI-to-AI simulation agent with a human Continue/Stop gate each iteration.”
    
- Structure Related:  
    “Create a two-persona REPEAT loop where each persona sees the cumulative transcript and produces the next turn.”
    
- Complexity Related:  
    “Build an advanced multi-agent loop that can be terminated early with MAP+JUMP and ends with a supervisor summary.”
    

### Usage & Modification Requests

- To Change the Intervention Frequency:  
    If you want the monitor checkpoint every 2 turns instead of every turn, then move the RADIO + router turns to run conditionally (e.g., only when @EVAL("@R_i@ % 2")@ matches) while keeping the transcript logger in every iteration.
    
- To Add a Second Monitor Action (e.g., “Rewrite last counselor question”):  
    If you add a third option, then extend the MAP/JUMP router to branch to a corrective path turn before logging.
    
- To Reuse for Sales/Support/Negotiation:  
    Replace COUNSELOR_PERSONA/COUNSELEE_PERSONA with the two target roles and keep the same monitor gate + logging + analysis structure.
    
- To Make the Transcript More Structured:  
    If you want JSON logs, then change Turn 7’s formatting to a consistent JSON-like record per Turn @R_i@ (do not change REPEAT bounds).
    

## References

- Choi, J. (2025). AI-to-AI Monitored Conversation: Two-Agent Simulation with Human Stop/Continue Gate and Supervisory Analysis. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---

=====

<!-- code-bank match (score=17, keywords: answer, loop, question) -->
# 2-Param Stem with Parallel Enumeration List using IOTA Framework: Linked P1/P2 Stem Assembly + P3 Answer Bank

## Metadata

- Framework: IOTA
    
- Complexity: Intermediate
    
- Primary Function: Assessment Item Generation (Item Factory)
    
- Key Symbolic Commands: REPEAT, D, SETJ, RADIO, TR, TN
    
- Key Concepts: Parallel enumeration lists, SHUFFLE + LINK alignment, 2-parameter stem template, Distractor generation from answer pool, JSON item bank compilation, Optional human validation loop
    

## Background & Objective

- Problem Solved: Many assessment items require a stem composed from two linked attributes (e.g., Subject + Attribute) while mapping to a single correct answer; maintaining pairing integrity during randomization is error-prone.
    
- Core Mechanism: Uses a 10-item ontology of linked parallel lists where P1 is shuffled and P2/P3 are LINKed to P1. A REPEAT loop enumerates instances, builds each item’s JSON (prompt from P1+P2; correctAnswer from P3), generates choices using @D() from the pooled answers, compiles all items into one JSON array, then stores it as a JP artifact (assessmentTest) with an optional validation loop.
    

## Full CAFA Agent Code

{  

    "options": {  

        "title": "IOTA Example: General Knowledge Item",  

        "brief": "A dynamic item generator that uses a 10-item parallel ontology (2 for stem, 1 for answer).",  

        "name": "IOTA - AIG Item Template - 2-Param Stem (10-Item)",  

        "description": "This IOTA agent uses parallel lists (P1, P2, P3). The stem is generated from P1 and P2, and the answer is from P3. It compiles the generated items into a JSON array and provides an optional validation loop.",  

        "greeting": "Welcome to the IOTA Item Generator. This agent will create a set of general knowledge problems.",  

        "params": {  

            "P1": {  

                "org": "William Shakespeare|J.R.R. Tolkien|Isaac Newton|Leonardo da Vinci|Albert Einstein|Marie Curie|Vincent van Gogh|Ludwig van Beethoven|Galileo Galilei|Charles Darwin",  

                "cond": "SHUFFLE",  

                "desc": "Parameter 1: The 'Subject' (e.g., Author/Scientist). This list is shuffled."  

            },  

            "P2": {  

                "org": "most famous play|most famous novel|most famous law|most famous painting|most famous equation|pioneering research field|most famous painting|most famous symphony|most famous astronomical observation|most famous theory",  

                "cond": "LINK(P1)",  

                "desc": "Parameter 2: The 'Attribute' (e.g., Work Type). Linked to P1."  

            },  

            "P3": {  

                "org": "Hamlet|The Lord of the Rings|The law of universal gravitation|Mona Lisa|E=mc²|Radioactivity|The Starry Night|Symphony No. 5|Moons of Jupiter|Theory of Evolution",  

                "cond": "LINK(P1)",  

                "desc": "Parameter 3: The 'Answer'. Linked to P1 to maintain the correct relationship."  

            },  

            "prompt": {  

                "org": "What is @P1[@R_i@]@'s @P2[@R_i@]@?",  

                "cond": "SELF",  

                "desc": "The template for the question stem, using P1 and P2."  

            },  

            "correctAnswer": {  

                "org": "@P3[@R_i@]@",  

                "cond": "SELF",  

                "desc": "The template for the correct answer, pulled from the linked P3 list."  

            },  

            "choices": {  

                "org": "@P3@",  

                "cond": "SELF",  

                "desc": "The pool of potential distractors (all answers). The @D() command will pull from this."  

            },  

            "numberOfChoices": {  

                "org": "4",  

                "cond": "SELF",  

                "desc": "The total number of choices (1 correct + 3 distractors) for each item."  

            },  

            "numberOfInstances": {  

                "org": "10",  

                "cond": "SELF",  

                "desc": "The total number of unique item instances to generate."  

            }  

        }  

    },  

    "prompts": [  

        {  

            "system": "",  

            "user": "/ T1: This hidden control turn sets up the REPEAT loop to generate all item instances (T2 and T3).\n@REPEAT(@TN(1)@, @TN(2)@, \"@numberOfInstances@\")@",  

            "show": false,  

            "model": null  

        },  

        {  

            "system": "",  

            "user": "/ T2 (LOOP 1/2): Generate the JSON string for a single item instance. This runs N times.\n{\"identifier\":\"Insatance_@R_i@\",\"prompt\":\"@prompt@\",\"choices\":\"@D(\"@correctAnswer@\", \"\", \"@choices@\", \"@numberOfChoices@\", \"ASCE\")@\",\"correctAnswer\":\"@correctAnswer@\"}",  

            "show": true,  

            "model": null  

        },  

        {  

            "system": "",  

            "user": "/ T3 (LOOP 2/2): Store the JSON string from T2 into a unique JSON Parameter (e.g., Insatance_1).\n@SETJ(Insatance_@R_i@, @TR@TN(-1)[@R_i@]@)@",  

            "show": true,  

            "model": null  

        },  

        {  

            "system": "You are provided with @numberOfInstances@ JSON objects, concatenated as a raw string. Your task is to compile them into a valid JSON array, starting with [ and ending with ]. Provide ONLY the raw JSON array, without any other text or markdown wrappers.",  

            "user": "@TR@TN(-2)@@",  

            "show": true,  

            "model": "gpt-4.1-nano"  

        },  

        {  

            "system": "",  

            "user": "/ T5: Store the final, complete JSON array from the LLM into the 'assessmentTest' parameter.\n@SETJ(assessmentTest, @TR@TN(-1)@@)@",  

            "show": true,  

            "model": null  

        },  

        {  

            "system": "",  

            "user": "/ T6: This hidden turn sets up an optional REPEAT loop to validate the generated items.\n@REPEAT(@TN(1)@, @TN(1)@, \"@numberOfInstances@\")@",  

            "show": false,  

            "model": null  

        },  

        {  

            "system": "",  

            "user": "/ T7 (VALIDATION LOOP): Display each item from the 'assessmentTest' JSON array using a RADIO control for human validation.\n@RADIO(R_@R_i@, \"@assessmentTest[@R_i@].prompt@\", \"@assessmentTest[@R_i@].choices@\")@",  

            "show": true,  

            "model": null  

        }  

    ]  

}

  

## Detailed Logic Breakdown

### Ontology Model (options.params):

- P1: Primary subject list; cond: SHUFFLE randomizes item order per session.
    
- P2: Attribute list; cond: LINK(P1) keeps attribute aligned to shuffled subjects.
    
- P3: Answer list; cond: LINK(P1) ensures correctAnswer remains aligned to the subject–attribute pair.
    
- prompt: Stem template combining two parameters (P1 + P2) at loop index @R_i@.
    
- correctAnswer: Answer template pulling from P3 at @R_i@.
    
- choices: Distractor pool defined as the full P3 list.
    
- numberOfChoices: Choice count for @D() (1 correct + distractors).
    
- numberOfInstances: Loop length; generates one item per ontology row.
    

### Execution Flow (prompts array):

- Turn 1 (Symbolic, Hidden): Starts generation loop across instances with REPEAT (runs Turns 2–3).
    
- Turn 2 (Symbolic, Visible, Loop): Constructs one JSON object string for the current instance, including:
    

- prompt assembled from @prompt@ (P1+P2)
    
- choices generated by @D(correctAnswer, "", choices, numberOfChoices, "ASCE")@
    
- correctAnswer from P3
    

- Turn 3 (Symbolic, Visible, Loop): Stores each per-instance JSON string into a distinct JP (Insatance_@R_i@) using SETJ.
    
- Turn 4 (LLM, Visible): Compiles concatenated JSON objects into a single valid JSON array (formatting utility role).
    
- Turn 5 (Symbolic, Visible): Stores the final JSON array into assessmentTest via SETJ.
    
- Turn 6 (Symbolic, Hidden): Optional validation loop setup across numberOfInstances.
    
- Turn 7 (Symbolic, Visible, Loop): Human validation UI: displays each assessmentTest[@R_i@] as a RADIO.
    

## Visualization Mermaid Code

graph TD

  A[Start] --> B[Turn 1: REPEAT x numberOfInstances<br/>(runs Turns 2-3)]

  B --> C[Turn 2 (Loop): Build item JSON string<br/>prompt=P1+P2, answer=P3, choices=@D()]

  C --> D[Turn 3 (Loop): SETJ Insatance_Ri = item JSON]

  D --> B

  B --> E[Turn 4: LLM compile raw objects -> JSON array]

  E --> F[Turn 5: SETJ assessmentTest = final array]

  F --> G[Turn 6: Optional REPEAT validation loop]

  G --> H[Turn 7 (Loop): RADIO display assessmentTest[Ri]]

  H --> G

  G --> I[End]

  

## Related Questions and Instructions

### Design & Architecture Requests

- Framework Related:  
    “Generate an IOTA agent that produces a JSON item bank using linked parallel lists and a two-field stem template.”
    
- Structure Related:  
    “Create an item factory where P2 and P3 are LINKed to a SHUFFLEd P1.”
    
- Complexity Related:  
    “Generate an intermediate IOTA that uses @D() for distractors and outputs a compiled JSON array.”
    

### Usage & Modification Requests

- Task Related:  
    “Replace the subject/attribute/answer ontology with a different domain (e.g., diseases + test type → recommended test).”
    
- Reuse:  
    “Reuse this structure to generate vocabulary items: word + part-of-speech → definition.”
    
- Bounded Changes:  
    “Change numberOfChoices from 4 to 5 without adding turns.”
    

Modification Recipes (If/Then):

- To Add Rationales: If you want explanations, then add a new linked parameter P4 with cond: LINK(P1) and include "rationale":"@P4[@R_i@]@" inside Turn 2’s JSON.
    
- To Remove Validation UI: If you want a pure factory-only IOTA, then remove Turns 6–7 (optional loop) and end after Turn 5 storing assessmentTest.
    
- To Change Distractor Strategy: If you want different ordering, then adjust the final argument of @D(..., "ASCE")@ (keeping the command structure unchanged).
    

## References

- Choi, J. (2025). 2-Param Stem with Parallel Enumeration List using IOTA Framework: Linked P1/P2 Stem Assembly + P3 Answer Bank. In Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence. CAFA Lab, Inc.
    

---

=====

