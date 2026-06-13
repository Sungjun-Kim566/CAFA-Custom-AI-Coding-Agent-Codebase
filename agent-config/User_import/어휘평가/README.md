---
type: project
status: complete
deadline: 2026-05-30
---
```dataviewjs
const pages = dv.pages()
  .where(p => p.type === "project");

dv.table(
  ["Project", "Done", "Total", "Progress"],
  pages.map(p => {
    const tasks = p.file.tasks;
    const done = tasks.where(t => t.completed).length;
    const total = tasks.length;
    const percent = total === 0 ? 0 : Math.round((done / total) * 100);

    return [
      p.file.link,
      done,
      total,
      `${percent}%`
    ];
  })
);
```


# 초중고 어휘평가 에이전트 생성 

- [x] Skeletal Structure Overview
- [x] Project Parameter Setup
- [x] List types of AI Agents to create
- [x] Vocab Test Config JSON Schema
- [x] Architecture Agent Parameter Setup
- [x] Workflow Summary
- [x] Randomized Question Selection
- [x] Indexing issue(Resolved)
- [x] Automatic Scoring with index adjustment
- [x] Updating test config JSON data
- [x] LLM Feedback Prompt
- [x] Prototype Agent confirmed
- [x] Multi-Agent Environment Setup
	- [x] 초등
		- [x] Derivatives
			- [x] T1: Form Recognition
			- [x] T2: Meaning Recall
			- [x] T3: Form Recall
		- [x] Context
			- [x] T1
			- [x] T2
			- [x] T3
		- [x] Form+meaning
			- [x] T1
			- [x] T2
			- [x] T3
		- [x] Collocation
			- [x] T1
			- [x] T2
			- [x] T3
	- [x] 중등
		- [x] Derivatives
			- [x] T1
			- [x] T2
			- [x] T3
		- [x] Context
			- [x] T1
			- [x] T2
			- [x] T3
		- [x] Form+meaning
			- [x] T1
			- [x] T2
			- [x] T3
		- [x] Collocation
			- [x] T1
			- [x] T2
			- [x] T3
	- [x] 고등
		- [x] Derivatives
			- [x] T1
			- [x] T2
			- [x] T3
		- [x] Context
			- [x] T1
			- [x] T2
			- [x] T3
		- [x] Form+meaning
			- [x] T1
			- [x] T2
			- [x] T3
		- [x] Collocation
			- [x] T1
			- [x] T2
			- [x] T3
# 초중고 어휘평가 에이전트 생성 
## Link: https://docs.google.com/spreadsheets/d/1aBlR9qtUs1FQpvI_zf-efVIPFGJWz2MJ0T6QaU3OAFI/edit?gid=551881220#gid=551881220
## Slide: https://docs.google.com/presentation/d/1d0c1gV-x1_U7lWvYCOETxoPKO-lmtWdMbciTIPMkyr8/edit?slide=id.p#slide=id.p

| 초중고 어휘밴드 | 평가 어휘요소 | 문항유형 | 총 에이전트 개수 |
| -------- | ------- | ---- | --------- |
| 3개       | 4개      | 3종류  | 36개       |

# 초등: Word_B1(L)
## Word Band 1st (Elementary)
## T1: Form Recognition
## T2: Meaning Recall
## T3: Form Recall

| 문항유형 \ 어휘요소              | 파생어(Derivatives)  | 문맥 민감성(Context) | 형태-의미 연결(Form+meaning) | 연어(Collocation)   |
| ------------------------ | ----------------- | --------------- | ---------------------- | ----------------- |
| T1: Form Recognition(MC) | Derivatives B1 T1 | Context B1 T1   | form+meaning B1 T1     | collocation B1 T1 |
| T2: Meaning Recall(SA)   | Derivatives B1 T2 | Context B1 T2   | form+meaning B1 T2     | collocation B1 T2 |
| T3: Form Recall(SA)      | Derivatives B1 T3 | Context B1 T3   | form+meaning B1 T3     | collocation B1 T3 |
# 중등: Word band_2(M)
## Word Band 2nd (Middle)
## T1: Form Recognition
## T2: Meaning Recall
## T3: Form Recall
| 문항유형 \ 어휘요소              | 파생어(Derivatives)  | 문맥 민감성(Context) | 형태-의미 연결(Form+meaning) | 연어(Collocation)   |
| ------------------------ | ----------------- | --------------- | ---------------------- | ----------------- |
| T1: Form Recognition(MC) | Derivatives B2 T1 | Context B2 T1   | form+meaning B2 T1     | collocation B2 T1 |
| T2: Meaning Recall(SA)   | Derivatives B2 T2 | Context B2 T2   | form+meaning B2 T2     | collocation B2 T2 |
| T3: Form Recall(SA)      | Derivatives B2 T3 | Context B2 T3   | form+meaning B2 T3     | collocation B2 T3 |
# 고등: Word band_3(H)
## Word Band 3rd (High)
## T1: Form Recognition
## T2: Meaning Recall
## T3: Form Recall
| 문항유형 \ 어휘요소              | 파생어(Derivatives)  | 문맥 민감성(Context) | 형태-의미 연결(Form+meaning) | 연어(Collocation)   |
| ------------------------ | ----------------- | --------------- | ---------------------- | ----------------- |
| T1: Form Recognition(MC) | Derivatives B3 T1 | Context B3 T1   | form+meaning B3 T1     | collocation B3 T1 |
| T2: Meaning Recall(SA)   | Derivatives B3 T2 | Context B3 T2   | form+meaning B3 T2     | collocation B3 T2 |
| T3: Form Recall(SA)      | Derivatives B3 T3 | Context B3 T3   | form+meaning B3 T3     | collocation B3 T3 |
# Application Frames
## Overall Skeletal Structure
```JSON
{
  "Difficulty": [
    {"Elementary": "B1", "Middle": "B2", "High": "B3"}
  ],
  "B1": {
    "T1": "Form_Recognition(MC)",
    "T2": "Meaning_Recall(SA)",
    "T3": "Form Recall(SA)",
    "Problem_combination":[
      "Derivatives",
      "Context",
      "Form+Meaning",
      "Collocation"
    ]
  },
  "B2": {
    "T1": "Form_Recognition(MC)",
    "T2": "Meaning_Recall(SA)",
    "T3": "Form Recall(SA)",
    "Problem_combination":[
      "Derivatives",
      "Context",
      "Form+Meaning",
      "Collocation"
    ]
  },
  "B3": {
    "T1": "Form_Recognition(MC)",
    "T2": "Meaning_Recall(SA)",
    "T3": "Form Recall(SA)",
    "Problem_combination":[
      "Derivatives",
      "Context",
      "Form+Meaning",
      "Collocation"
    ]
  }
}
```
## Parameters

| GSID: Reference memory address               | Problem Parameters (PRM)(LINK(ANS))<br>Dependent Variables | Answer Parameters (ANS)(SHUFFLE)<br>Independent Variables | Feedback (FB_Neg / Pos)                                                                                                                                        | BYE(end comment)                       | N(Iteration indicator)<br>Random Number generated |
| -------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ------------------------------------------------- |
| 1aBlR9qtUs1FQpvI_zf-efVIPFGJWz2MJ0T6QaU3OAFI | 1. Noun<br>2. Verb<br>3. Adjective                         | 1. Noun<br>2. Verb<br>3. Adjective                        | the number of points earned; 1 point per each question<br>correct/incorrect problems solved enumeration required for automatic scoring and LLM-based Feedbacks | Random Ending comments after each test | @N@                                               |
# testing problems JSON Schema
```JSON
{
  "Noun": [
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    }
  ],
  "Verb": [
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    }
  ],
  "Adjective": [
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": "",
      "Student_answer": "",
      "correctness": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": ""
    },
    {
      "problem": "",
      "problem_reference": "",
      "answer": "",
      "LLM_FBK": ""
    }
  ],
  "Result": [{
    "Noun": 1,
    "Verb": 1,
    "Adjective": 1,
    "Cumulative": 1,
    "Direction": ""
  }]
}
```
## LLM Feedback 
### Prompt
```XML
<instructions>
    <task>
        Given the answer for the question and its derivative groups, create a feedback report for each of three major POS questions (Noun, Verb, Adjective) that includes the answer's and each of its derivative's POS, definition, and a short example sentence with its Korean translation in Korean. 
    </task>
    <example>
1. **correct (형용사)**  
- 의미: 옳은, 정확한  
- 예문: Please give the correct answer. (제발 올바른 답을 주세요.)

2. **correctly (부사)**  
- 의미: 정확하게, 올바르게  
- 예문: She answered the question correctly. (그녀는 질문에 정확하게 답했어요.)

3. **correction (명사)**  
- 의미: 수정, 교정  
- 예문: The teacher made a correction on my essay. (선생님이 내 에세이를 수정하셨어요.)

4. **incorrect (형용사)**  
- 의미: 틀린, 부정확한  
- 예문: His answer was incorrect. (그의 답은 틀렸다.)
    </example>
</instructions>
```
### Given variables for LLM Feedback
```txt
<instructions>
    <task>
        Given the answer for the question and its derivative groups, create a feedback report for each of three major POS questions (Noun, Verb, Adjective) that includes the answer's and each of its derivative's POS, definition, and a short example sentence with its Korean translation in Korean. 
    </task>
    <example>
1. **correct (형용사)**  
- 의미: 옳은, 정확한  
- 예문: Please give the correct answer. (제발 올바른 답을 주세요.)

2. **correctly (부사)**  
- 의미: 정확하게, 올바르게  
- 예문: She answered the question correctly. (그녀는 질문에 정확하게 답했어요.)

3. **correction (명사)**  
- 의미: 수정, 교정  
- 예문: The teacher made a correction on my essay. (선생님이 내 에세이를 수정하셨어요.)

4. **incorrect (형용사)**  
- 의미: 틀린, 부정확한  
- 예문: His answer was incorrect. (그의 답은 틀렸다.)
    </example>
    
</instructions>
```

# 현재 에이전트 Example Schema

```JSON
{
  "options": {
    "title": "<h1>CAFA Agent</h1>",
    "brief": "",
    "name": "[Updated] 초등학교 파생어_기본 (형태)",
    "description": "초등학교 수준 어휘 75개를 바탕으로 파생어에 대한 기본 지식을 평가합니다. 이 앱은 개인정보를 수집하지 않습니다. ",
    "greeting": "주어진 파생어 그룹을 참고하여 이 단어들의 기본형이 된다고 생각하는 단어를 맨 아래 입력창에 쓰세요. <br> 나열된 단어 중 하나를 그대로 베껴 쓰지 마세요. <br>\n\n\n(예시)  action / active / activity  --->  기본형: act",
    "keep-in-app-cafakey": false,
    "is-template": false,
    "is-public": false,
    "params": {
      "N_IDX": {
        "org": "10",
        "cond": "SELF",
        "desc": ""
      },
      "V_IDX": {
        "org": "19",
        "cond": "SELF",
        "desc": ""
      },
      "ADJ_IDX": {
        "org": "15",
        "cond": "SELF",
        "desc": ""
      },
      "Rand_iteration": {
        "org": "4",
        "cond": "SELF",
        "desc": ""
      },
      "JSON_test_config": {
        "org": "{\n  \"Noun\": [\n    {\n      \"problem\": \"1. 파생어 그룹 addressable / addresser의 기본형을 쓰시오.\",\n      \"problem_reference\": \"addressable / addresser\",\n      \"answer\": \"address\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"address\",\n      \"correctness\": 1\n    },\n    {\n      \"problem\": \"2. 파생어 그룹 modeling / modeler / remodel의 기본형을 쓰시오.\",\n      \"problem_reference\": \"modeling / modeler / remodel\",\n      \"answer\": \"model\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"model\",\n      \"correctness\": 1\n    },\n    {\n      \"problem\": \"3. 파생어 그룹 memorable / memorization / memorized의 기본형을 쓰시오.\",\n      \"problem_reference\": \"memorable / memorization / memorized\",\n      \"answer\": \"memory\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"memory\",\n      \"correctness\": 1\n    },\n    {\n      \"problem\": \"4. 파생어 그룹 dressed / undress / dressy의 기본형을 쓰시오.\",\n      \"problem_reference\": \"dressed / undress / dressy\",\n      \"answer\": \"dress\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"dress\",\n      \"correctness\": 1\n    },\n    {\n      \"problem\": \"5. 파생어 그룹 earthy / earthen의 기본형을 쓰시오.\",\n      \"problem_reference\": \"earthy / earthen\",\n      \"answer\": \"earth\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"market\",\n      \"correctness\": 1\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    }\n  ],\n  \"Verb\": [\n    {\n      \"problem\": \"1. 파생어 그룹 focused / refocus의 기본형을 쓰시오.\",\n      \"problem_reference\": \"focused / refocus\",\n      \"answer\": \"focus\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"focus\",\n      \"correctness\": 1\n    },\n    {\n      \"problem\": \"2. 파생어 그룹 choice / choosable의 기본형을 쓰시오.\",\n      \"problem_reference\": \"choice / choosable\",\n      \"answer\": \"choose\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"choose\",\n      \"correctness\": 1\n    },\n    {\n      \"problem\": \"3. 파생어 그룹 decision / decisive / indecisive의 기본형을 쓰시오.\",\n      \"problem_reference\": \"decision / decisive / indecisive\",\n      \"answer\": \"decide\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"decide\",\n      \"correctness\": 1\n    },\n    {\n      \"problem\": \"4. 파생어 그룹 missing / dismiss의 기본형을 쓰시오.\",\n      \"problem_reference\": \"missing / dismiss\",\n      \"answer\": \"miss\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"miss\",\n      \"correctness\": 1\n    },\n    {\n      \"problem\": \"5. 파생어 그룹 holder / uphold의 기본형을 쓰시오.\",\n      \"problem_reference\": \"holder / uphold\",\n      \"answer\": \"hold\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"act\",\n      \"correctness\": 1\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    }\n  ],\n  \"Adjective\": [\n    {\n      \"problem\": \"1. 파생어 그룹 clarity / clearly / unclear의 기본형을 쓰시오.\",\n      \"problem_reference\": \"clarity / clearly / unclear\",\n      \"answer\": \"clear\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"clear\",\n      \"correctness\": 1\n    },\n    {\n      \"problem\": \"2. 파생어 그룹 safety / safely / unsafe의 기본형을 쓰시오.\",\n      \"problem_reference\": \"safety / safely / unsafe\",\n      \"answer\": \"safe\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"safe\",\n      \"correctness\": 1\n    },\n    {\n      \"problem\": \"3. 파생어 그룹 newness / newly / renew의 기본형을 쓰시오.\",\n      \"problem_reference\": \"newness / newly / renew\",\n      \"answer\": \"new\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"new\",\n      \"correctness\": 1\n    },\n    {\n      \"problem\": \"4. 파생어 그룹 hardly / hardness / harden의 기본형을 쓰시오.\",\n      \"problem_reference\": \"hardly / hardness / harden\",\n      \"answer\": \"hard\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"hard\",\n      \"correctness\": 1\n    },\n    {\n      \"problem\": \"5. 파생어 그룹 brightness / brightly / brighten의 기본형을 쓰시오.\",\n      \"problem_reference\": \"brightness / brightly / brighten\",\n      \"answer\": \"bright\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"cleane\",\n      \"correctness\": 0\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    },\n    {\n      \"problem\": \"\",\n      \"problem_reference\": \"\",\n      \"answer\": \"\",\n      \"LLM_FBK\": \"\",\n      \"Student_answer\": \"\",\n      \"correctness\": \"\"\n    }\n  ],\n  \"Result\": [\n    {\n      \"Noun\": 1,\n      \"Verb\": 1,\n      \"Adjective\": 1,\n      \"Cumulative\": 1,\n      \"Direction\": \"\"\n    }\n  ]\n}",
        "cond": "",
        "desc": ""
      },
      "P_N1": {
        "org": "{\n  \"id\": \"P_N1\",\n  \"label\": \"1. 파생어 그룹 addressable / addresser의 기본형을 쓰시오.\",\n  \"response\": \"address\"\n}",
        "cond": "",
        "desc": ""
      },
      "P_V1": {
        "org": "{\n  \"id\": \"P_V1\",\n  \"label\": \"1. 파생어 그룹 focused / refocus의 기본형을 쓰시오.\",\n  \"response\": \"focus\"\n}",
        "cond": "",
        "desc": ""
      },
      "P_ADJ1": {
        "org": "{\n  \"id\": \"P_ADJ1\",\n  \"label\": \"1. 파생어 그룹 clarity / clearly / unclear의 기본형을 쓰시오.\",\n  \"response\": \"clear\"\n}",
        "cond": "",
        "desc": ""
      },
      "P_N2": {
        "org": "{\n  \"id\": \"P_N2\",\n  \"label\": \"2. 파생어 그룹 modeling / modeler / remodel의 기본형을 쓰시오.\",\n  \"response\": \"model\"\n}",
        "cond": "",
        "desc": ""
      },
      "P_V2": {
        "org": "{\n  \"id\": \"P_V2\",\n  \"label\": \"2. 파생어 그룹 choice / choosable의 기본형을 쓰시오.\",\n  \"response\": \"choose\"\n}",
        "cond": "",
        "desc": ""
      },
      "P_ADJ2": {
        "org": "{\n  \"id\": \"P_ADJ2\",\n  \"label\": \"2. 파생어 그룹 safety / safely / unsafe의 기본형을 쓰시오.\",\n  \"response\": \"safe\"\n}",
        "cond": "",
        "desc": ""
      },
      "PRM_N": {
        "org": "addressable / addresser|banker / bankrupt|onboard / boarded|bodily / embody|checklist / checkup / checkable|classy / classified / classification|conditional / conditionally / conditioned|cultural / culturally / multicultural|datable / outdated / dateless|dressed / undress / dressy|energetic / energetically / energize|earthy / earthen|factual / factful / factless|formal / formation / reform|grouping / ungroup / regroup|lighting / lightly / lighten|marketing / marketer / marketable|memorable / memorization / memorized|modeling / modeler / remodel|paperwork / paperless|placement / misplaced / replace|powerful / powerless / empower",
        "cond": "SELF",
        "desc": ""
      },
      "ANS_N": {
        "org": "address|bank|board|body|check|class|condition|culture|date|dress|energy|earth|fact|form|group|light|market|memory|model|paper|place|power",
        "cond": "SELF",
        "desc": ""
      },
      "ANS_V": {
        "org": "act|agree|believe|break|build|call|change|choose|control|decide|drive|end|fall|focus|hold|lie|make|mind|miss|stand",
        "cond": "SELF",
        "desc": ""
      },
      "PRM_V": {
        "org": "action / active / activity|agreement / disagreement|belief / believable / disbelief|broken / breakable / breakdown|builder / rebuilt / rebuild|caller / recall / callback|changeable / exchange|choice / choosable|controller / uncontrollable|decision / decisive / indecisive|driver / driven|endless / endpoint|fallen / downfall|focused / refocus|holder / uphold|liar / lied|maker / remake / makeup|mindful / reminder / mindless|missing / dismiss|standing / standard",
        "cond": "SELF",
        "desc": ""
      },
      "ANS_ADJ": {
        "org": "bad|bright|certain|clean|clear|close|cold|cool|dark|dead|difficult|free|fun|great|hard|heavy|high|last|new|open|right|safe",
        "cond": "SELF",
        "desc": ""
      },
      "PRM_ADJ": {
        "org": "badly / badness|brightness / brightly / brighten|certainty / certainly / uncertain|cleanliness / cleanly / unclean|clarity / clearly / unclear|closure / closely / enclose|coldness / coldly|coolness / cooler / cooling|darkness / darken|deadly / death|difficulty / difficultly|freely / freedom|funny / funnily|greatly / greatness|hardly / hardness / harden|heavily / heav|highly / height / heighten|lastly / lasting|newness / newly / renew|openly / openness / reopen|rightly / rightness|safety / safely / unsafe",
        "cond": "SELF",
        "desc": ""
      },
      "P_N3": {
        "org": "{\n  \"id\": \"P_N3\",\n  \"label\": \"3. 파생어 그룹 memorable / memorization / memorized의 기본형을 쓰시오.\",\n  \"response\": \"memory\"\n}",
        "cond": "",
        "desc": ""
      },
      "P_V3": {
        "org": "{\n  \"id\": \"P_V3\",\n  \"label\": \"3. 파생어 그룹 decision / decisive / indecisive의 기본형을 쓰시오.\",\n  \"response\": \"decide\"\n}",
        "cond": "",
        "desc": ""
      },
      "P_ADJ3": {
        "org": "{\n  \"id\": \"P_ADJ3\",\n  \"label\": \"3. 파생어 그룹 newness / newly / renew의 기본형을 쓰시오.\",\n  \"response\": \"new\"\n}",
        "cond": "",
        "desc": ""
      },
      "P_N4": {
        "org": "{\n  \"id\": \"P_N4\",\n  \"label\": \"4. 파생어 그룹 dressed / undress / dressy의 기본형을 쓰시오.\",\n  \"response\": \"dress\"\n}",
        "cond": "",
        "desc": ""
      },
      "P_V4": {
        "org": "{\n  \"id\": \"P_V4\",\n  \"label\": \"4. 파생어 그룹 missing / dismiss의 기본형을 쓰시오.\",\n  \"response\": \"miss\"\n}",
        "cond": "",
        "desc": ""
      },
      "P_ADJ4": {
        "org": "{\n  \"id\": \"P_ADJ4\",\n  \"label\": \"4. 파생어 그룹 hardly / hardness / harden의 기본형을 쓰시오.\",\n  \"response\": \"hard\"\n}",
        "cond": "",
        "desc": ""
      },
      "Identification": {
        "org": "S-113",
        "cond": "SELF",
        "desc": ""
      },
      "ID": {
        "org": "{\n  \"id\": \"ID\",\n  \"label\": \"선생님이 배부해준 S-OOO 형식의 일련번호를 입력하세요. (입력예시: S-113) 틀린 일련번호 입력시, 일련번호 입력창이 다시 로드됩니다.\",\n  \"response\": \"S-113\"\n}",
        "cond": "",
        "desc": ""
      },
      "P_N5": {
        "org": "{\n  \"id\": \"P_N5\",\n  \"label\": \"5. 파생어 그룹 marketing / marketer / marketable의 기본형을 쓰시오.\",\n  \"response\": \"market\"\n}",
        "cond": "",
        "desc": ""
      },
      "P_V5": {
        "org": "{\n  \"id\": \"P_V5\",\n  \"label\": \"5. 파생어 그룹 action / active / activity의 기본형을 쓰시오.\",\n  \"response\": \"act\"\n}",
        "cond": "",
        "desc": ""
      },
      "P_ADJ5": {
        "org": "{\n  \"id\": \"P_ADJ5\",\n  \"label\": \"5. 파생어 그룹 cleanliness / cleanly / unclean의 기본형을 쓰시오.\",\n  \"response\": \"cleane\"\n}",
        "cond": "",
        "desc": ""
      }
    }
  },
  "prompts": [
    {
      "system": "",
      "user": "/\n@SET(Rand_iteration, \"@N(2,5)@\")@",
      "temperature": "0.5",
      "max-tokens": "2000",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/\n@TEXT(ID, \"선생님이 배부해준 S-OOO 형식의 일련번호를 입력하세요. (입력예시: S-113) 틀린 일련번호 입력시, 일련번호 입력창이 다시 로드됩니다.\")@",
      "temperature": "0.5",
      "max-tokens": "2000",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/틀리면 turn 2, 맞으면 turn 4\n@JUMP(@MAP(\"@TEXT(ID)@\", \"@Identification@\", \"4|@TN(-1)@\", EXACT)@)@",
      "temperature": "0.5",
      "max-tokens": "2000",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/\n어휘 테스트에 오신것을 환영합니다. <br>\n테스트 1회분의 문제수는 @EVAL(\"3*@Rand_iteration@\")@개 입니다",
      "temperature": "0.5",
      "max-tokens": "2000",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ 문제 풀이 iteration\n@REPEAT(@TN(1)@, @TN(2)@, @Rand_iteration@)@",
      "temperature": "0.5",
      "max-tokens": "2000",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/\n@SET(N_IDX, \"@INDEX(\"@PRM_N@\", \"@PRM_N[.]@\")@\", SELF)@\n@SET(V_IDX, \"@INDEX(\"@PRM_V@\", \"@PRM_V[.]@\")@\", SELF)@\n@SET(ADJ_IDX, \"@INDEX(\"@PRM_ADJ@\", \"@PRM_ADJ[.]@\")@\", SELF)@",
      "temperature": "0.5",
      "max-tokens": "2000",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ 문항 JSON 셋업\n@UPJ(JSON_test_config.Noun[@R_i@].problem, \"@EVAL(@R_i@)@. 파생어 그룹 @PRM_N[@N_IDX@]@의 기본형을 쓰시오.\")@\n@UPJ(JSON_test_config.Noun[@R_i@].problem_reference, \"@PRM_N[@N_IDX@]@\")@\n@UPJ(JSON_test_config.Noun[@R_i@].answer, \"@ANS_N[@N_IDX@]@\")@\n\n@UPJ(JSON_test_config.Verb[@R_i@].problem, \"@EVAL(@R_i@)@. 파생어 그룹 @PRM_V[@V_IDX@]@의 기본형을 쓰시오.\")@\n@UPJ(JSON_test_config.Verb[@R_i@].problem_reference, \"@PRM_V[@V_IDX@]@\")@\n@UPJ(JSON_test_config.Verb[@R_i@].answer, \"@ANS_V[@V_IDX@]@\")@\n\n@UPJ(JSON_test_config.Adjective[@R_i@].problem, \"@EVAL(@R_i@)@. 파생어 그룹 @PRM_ADJ[@ADJ_IDX@]@의 기본형을 쓰시오.\")@\n@UPJ(JSON_test_config.Adjective[@R_i@].problem_reference, \"@PRM_ADJ[@ADJ_IDX@]@\")@\n@UPJ(JSON_test_config.Adjective[@R_i@].answer, \"@ANS_ADJ[@ADJ_IDX@]@\")@",
      "temperature": "0.5",
      "max-tokens": "2000",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/ 문제 풀이 iteration\n@REPEAT(@TN(1)@, @TN(3)@, @Rand_iteration@)@",
      "temperature": "0.5",
      "max-tokens": "2000",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/\n@TEXT(P_N@R_i@, \"@JSON_test_config.Noun[@R_i@].problem@\")@|\n@TEXT(P_V@R_i@, \"@JSON_test_config.Verb[@R_i@].problem@\")@|\n@TEXT(P_ADJ@R_i@,\n\"@JSON_test_config.Adjective[@R_i@].problem@\")@|",
      "temperature": "0.5",
      "max-tokens": "2000",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "//automatic scoring; need to subtract 1 from final score due to indexing issue\n\n1. Noun\nT/F boolean: @MAP(\"@TEXT(P_N@R_i@)@\", \"@JSON_test_config.Noun[@R_i@].answer@\", \"1|0\",RWORD)@\n\nCurrent Score: @JSON_test_config.Result[1].Noun@\n\nEnumerated: @EVAL(\"@JSON_test_config.Result[1].Noun@ + @MAP(\"@TEXT(P_N@R_i@)@\", \"@JSON_test_config.Noun[@R_i@].answer@\", \"1|0\",RWORD)@\")@\n\nupdate:\n@UPJ(JSON_test_config.Result[1].Noun, @EVAL(\"@JSON_test_config.Result[1].Noun@ + @MAP(\"@TEXT(P_N@R_i@)@\", \"@JSON_test_config.Noun[@R_i@].answer@\", \"1|0\",RWORD)@\")@)@\n@UPJ(JSON_test_config.Noun[@R_i@].Student_answer, \"@TEXT(P_N@R_i@)@\")@\n@UPJ(JSON_test_config.Noun[@R_i@].correctness, @MAP(\"@TEXT(P_N@R_i@)@\", \"@JSON_test_config.Noun[@R_i@].answer@\", \"1|0\",RWORD)@)@\n\n2. Verb\nT/F boolean: @MAP(\"@TEXT(P_V@R_i@)@\", \"@JSON_test_config.Verb[@R_i@].answer@\", \"1|0\",RWORD)@\n\nCurrent Score: @JSON_test_config.Result[1].Verb@\n\nEnumerated: @EVAL(\"@JSON_test_config.Result[1].Verb@ + @MAP(\"@TEXT(P_V@R_i@)@\", \"@JSON_test_config.Verb[@R_i@].answer@\", \"1|0\",RWORD)@\")@\n\nupdate:\n@UPJ(JSON_test_config.Result[1].Verb, @EVAL(\"@JSON_test_config.Result[1].Verb@ + @MAP(\"@TEXT(P_V@R_i@)@\", \"@JSON_test_config.Verb[@R_i@].answer@\", \"1|0\",RWORD)@\")@)@\n@UPJ(JSON_test_config.Verb[@R_i@].Student_answer, \"@TEXT(P_V@R_i@)@\")@\n@UPJ(JSON_test_config.Verb[@R_i@].correctness, @MAP(\"@TEXT(P_V@R_i@)@\", \"@JSON_test_config.Verb[@R_i@].answer@\", \"1|0\",RWORD)@)@\n\n3. Adjective\nT/F boolean: @MAP(\"@TEXT(P_ADJ@R_i@)@\", \"@JSON_test_config.Adjective[@R_i@].answer@\", \"1|0\",RWORD)@\n\nCurrent Score: @JSON_test_config.Result[1].Adjective@\n\nEnumerated: @EVAL(\"@JSON_test_config.Result[1].Adjective@ + @MAP(\"@TEXT(P_ADJ@R_i@)@\", \"@JSON_test_config.Adjective[@R_i@].answer@\", \"1|0\",RWORD)@\")@\n\nupdate:\n@UPJ(JSON_test_config.Result[1].Adjective, @EVAL(\"@JSON_test_config.Result[1].Adjective@ + @MAP(\"@TEXT(P_ADJ@R_i@)@\", \"@JSON_test_config.Adjective[@R_i@].answer@\", \"1|0\",RWORD)@\")@)@\n@UPJ(JSON_test_config.Adjective[@R_i@].Student_answer, \"@TEXT(P_ADJ@R_i@)@\")@\n@UPJ(JSON_test_config.Adjective[@R_i@].correctness, @MAP(\"@TEXT(P_ADJ@R_i@)@\", \"@JSON_test_config.Adjective[@R_i@].answer@\", \"1|0\",RWORD)@)@\n",
      "temperature": "0.5",
      "max-tokens": "2000",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "<instructions>\n    <task>\n        Given the answer for the question and its derivative groups, create a feedback report for each of three major POS questions (Noun, Verb, Adjective) that includes the answer's and each of its derivative's POS, definition, and a short example sentence with its Korean translation in Korean. \n    </task>\n    <example>\n1. **correct (형용사)**  \n- 의미: 옳은, 정확한  \n- 예문: Please give the correct answer. (제발 올바른 답을 주세요.)\n\n2. **correctly (부사)**  \n- 의미: 정확하게, 올바르게  \n- 예문: She answered the question correctly. (그녀는 질문에 정확하게 답했어요.)\n\n3. **correction (명사)**  \n- 의미: 수정, 교정  \n- 예문: The teacher made a correction on my essay. (선생님이 내 에세이를 수정하셨어요.)\n\n4. **incorrect (형용사)**  \n- 의미: 틀린, 부정확한  \n- 예문: His answer was incorrect. (그의 답은 틀렸다.)\n    </example>\n    \n</instructions>",
      "user": "1. Noun\n- Question: @P_N@R_i@@\n- Corresponding answer: @JSON_test_config.Noun[@R_i@].answer@\n- Derivatives: @JSON_test_config.Noun[@R_i@].problem_reference@\n2. Verb\n- Question: @P_V@R_i@@\n- Corresponding answer: @JSON_test_config.Verb[@R_i@].answer@\n- Derivatives: @JSON_test_config.Verb[@R_i@].problem_reference@\n3. Adjective\n- Question: @P_ADJ@R_i@@\n- Corresponding answer: @JSON_test_config.Adjective[@R_i@].answer@\n- Derivatives: @JSON_test_config.Adjective[@R_i@].problem_reference@",
      "temperature": "0.3",
      "max-tokens": "4000",
      "send-mail": false,
      "markdown": true,
      "show": true,
      "model": "gpt-4.1",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/\n@TR@TN(-1)@@",
      "temperature": "0.5",
      "max-tokens": "2000",
      "send-mail": false,
      "markdown": true,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "//Adjust Final Score; Cumulative score and due to CAFA indexing issue\n@UPJ(JSON_test_config.Result[1].Noun, @EVAL(\"@JSON_test_config.Result[1].Noun@ - 1\")@)@\n@UPJ(JSON_test_config.Result[1].Verb, @EVAL(\"@JSON_test_config.Result[1].Verb@ - 1\")@)@\n@UPJ(JSON_test_config.Result[1].Adjective, @EVAL(\"@JSON_test_config.Result[1].Adjective@ - 1\")@)@\n\n@UPJ(JSON_test_config.Result[1].Cumulative, @EVAL(\"@JSON_test_config.Result[1].Noun@+@JSON_test_config.Result[1].Verb@+@JSON_test_config.Result[1].Adjective@\")@)@",
      "temperature": "0.5",
      "max-tokens": "2000",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    },
    {
      "system": "",
      "user": "/다음 인풋을 위한 점수 초기화\n@UPJ(JSON_test_config.Result[1].Noun, 1)@\n@UPJ(JSON_test_config.Result[1].Verb, 1)@\n@UPJ(JSON_test_config.Result[1].Adjective, 1)@\n@UPJ(JSON_test_config.Result[1].Cumulative, 1)@\n@UPJ(JSON_test_config.Result[1].Direction, \"\")@",
      "temperature": "0.5",
      "max-tokens": "2000",
      "send-mail": false,
      "markdown": false,
      "show": true,
      "model": "gpt-4.1-nano",
      "output-values": ""
    }
  ]
}
```
