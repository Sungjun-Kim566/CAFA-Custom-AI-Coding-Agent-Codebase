# Python Concepts Quiz Agent (AoA Framework)

This directory contains the implementation of a CAFA quiz agent built using the **AoA (Architecture of Alignment / Assessment)** framework.

## Files

- [quiz-agent-python-aoa.json](file:///Users/sungjunkim/Desktop/CAFA-Custom-AI-Coding-Agent-Codebase/agent-config/quiz-agent-python-aoa/quiz-agent-python-aoa.json) — The main CAFA agent configuration file containing options, parameters, and prompts.

## Key Design Patterns Used

1. **Sandwich Architecture**: The evaluation loop runs inside a `REPEAT` block composed of three distinct phases:
   - **Symbolic Input Layer** (Turn 2): Captures user free-text response via `@TEXTAREA`.
   - **LLM Evaluation Layer** (Turn 3): Grades answer against a strict rubric and returns exactly one of four labels (`Incorrect|Partially Correct|Mostly Correct|Fully Correct`) constrained by `output-values`.
   - **Hidden Control Layer** (Turn 4): Converts the label to points and increments the dynamic `SCORE` variable.

2. **Loop-Result Indexing Trick**: Accumulating turn results in a `REPEAT` loop append into a pipe-delimited list. We resolve this by indexing with the current iteration: `@TR@TN(-1)@[@R_i@]@` inside MAP/EVAL.

3. **No Same-Turn Dependencies**: Dynamic variables modified in Turn 4 are computed inline and not accessed within Turn 4 to preserve atomicity and protocol parsing compliance.

## How to Import & Run

To run this agent on the CAFA Platform:

1. Copy the entire contents of [quiz-agent-python-aoa.json](file:///Users/sungjunkim/Desktop/CAFA-Custom-AI-Coding-Agent-Codebase/agent-config/quiz-agent-python-aoa/quiz-agent-python-aoa.json).
2. Go to https://ai.cafalab.com/
3. Click **Create Agent** $\rightarrow$ **Build from Scratch** $\rightarrow$ **Import from Text**.
4. Paste the JSON and click **Import**.

## References

- Choi, J. (2025). AoA Rubric Quiz Agent: Looped Symbolic-Input → LLM-Evaluation → Hidden-Control Sandwich with Loop-Indexed Verdict Scoring. In *Collective AI on the Foundation AI (CAFA): The pathway of digital transformation of intelligence.* CAFA Lab, Inc.
- Choi, J., Kim, S., & Yoon, K. (2012–present). *Collective AI on the Foundation AI (CAFA) Platform.* CAFA Lab, Inc. https://ai.cafalab.com
