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
- [x] Student Authentication: 숫자 범위 검증(26001–26160) 방식으로 전환
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
# Tier별 구조 (T1 / T2 / T3)

각 어휘요소(Derivatives·Context·Form+Meaning·Collocation)는 3개의 Tier로 제작되며,
Tier는 **문항 형식**과 **채점 방식**으로 구분됩니다. 학생 인증(turn 0–3), 문항 생성 루프,
점수 초기화·최종 보정 로직은 모든 Tier가 동일하게 공유합니다.

| Tier | 유형 | 입력 방식 | 채점 방식 | 턴 구조 | LLM 피드백 |
| --- | --- | --- | --- | --- | --- |
| **T1** | Form Recognition (MC) | `@RADIO` (4지선다) | `@MAP(…, EXACT)` 결정론적 | 컴팩트 (~13 turn) | 전체 POS 일괄 1회 |
| **T2** | Meaning Recall (SA) | `@TEXT` (단답) | **LLM 판정** (`@TR`, `1`/`0`) | POS별 확장 (~34 turn) | POS별 개별 생성·저장 |
| **T3** | Form Recall (SA) | `@TEXT` (단답) | `@MAP(…, EXACT)` 결정론적 | 컴팩트 (~13 turn) | 전체 POS 일괄 1회 |

> **예외 — 파생어(Derivatives):** "기본형 쓰기"라는 생성형 과제 특성상 **T1도 단답(`@TEXT`)**으로
> 구현되며, 철자 변형을 허용하기 위해 `EXACT` 대신 **`RWORD`**(느슨한 단어 일치)로 채점합니다.
> Derivatives T3도 동일하게 `RWORD`를 사용합니다. (Context·Form+Meaning·Collocation의 T1은 MC.)

## 공통 파라미터 (모든 Tier)

| 파라미터 | 역할 |
| --- | --- |
| `GSID` | 문항 구글 시트 주소(메모리 참조) — `1aBlR9qtUs1FQpvI_zf-efVIPFGJWz2MJ0T6QaU3OAFI` |
| `Rand_iteration` | 1회분 문항 반복 수 — `@N(2,5)@`로 랜덤 생성 |
| `ID` / `ID_LOWER` / `ID_UPPER` / `Student_auth_list` | 학생 인증 (아래 [학생 인증] 절 참고) |
| `N_IDX` / `V_IDX` / `ADJ_IDX` / `OTH_IDX` | POS별 문항 풀에서 추출한 랜덤 인덱스 |
| `*_ANS` (`N_ANS`, `V_ANS`, …) | POS별 정답 풀 |
| `JSON_test_config` | 문항·정답·학생응답·정오·`LLM_FBK`·누적점수(`Result`)를 담는 중앙 메타데이터 |
| `P_N1`, `P_V1`, … `P_OTH4` | 렌더링용 개별 문항 객체(질문·선택지) |

> POS는 어휘요소에 따라 3종(Noun·Verb·Adjective) 또는 4종(+others)입니다.
> 4종 구성에서는 `OTH_*` 계열 파라미터가 함께 존재합니다.

## Tier·어휘요소별 고유 파라미터

| 파라미터(접두) | 의미 | 주 등장 위치 |
| --- | --- | --- |
| `*_DSTR` | 오답 선택지(distractor) 풀 | **T1(MC)** — `@D(정답,"",*_DSTR,4)`로 4지선다 생성 |
| `*_SEN` | 문항 예문(빈칸 문장) | Context / Form+Meaning / Collocation |
| `*_DEF` | 정답의 뜻(정의) | Context T1·T3, 피드백 맥락 |
| `*_POLY` | 다의어 원형(polysemy root) | **Context T2·T3** — 의미 채점·피드백 근거 |
| `PRM_*` | 문항 소스(파생어 그룹/형태소 단서 등) | Derivatives / Form+Meaning |
| `DRV_*`, `DRV_*Q` | 파생어 보기·질문 | Derivatives T2 |
| `POS`, `N`/`V`/…, `*_COL` | 연어(collocation) 표제어·짝 | Collocation |
| `L_*` | 보기 레이블 | Form+Meaning T3 |

> **PRM ↔ ANS 관계:** 문항 소스 파라미터(`PRM_*` 등)는 정답 풀(`*_ANS`)에 **연결(LINK)된 종속
> 변수**이고, `*_ANS`는 매 회차 **셔플(SHUFFLE)되는 독립 변수**입니다. 같은 인덱스(`*_IDX`)로
> 두 풀에서 문항과 정답을 함께 추출해 `JSON_test_config`에 기록하므로, 둘의 순서·길이가
> 항상 정렬을 유지해야 합니다.

## 턴(turn) 아키텍처

### 공통 골격 — 모든 Tier

| Turn | 작업 | 산출물 / 사용처 |
| --- | --- | --- |
| 0 | `@SET(Rand_iteration, "@N(2,5)@")@` | 1회분 문항 수 결정 |
| 1–2 | 학생 인증 입력 + `@JUMP` 범위 검증 | 통과 시 turn 4로 진행 |
| 3 | 환영 메시지 — `@EVAL`로 총 문항 수 표시 | 학생에게 표시 |
| 4 | `@REPEAT`로 문항 생성 루프 시작 | 반복 인덱스 `@R_i@` |
| 5 | `@INDEX` / `@SET`으로 POS별 랜덤 인덱스 추출 | `*_IDX` |
| 6 | `@UPJ`로 `JSON_test_config`에 문항·정답(·distractor) 기록 | 중앙 메타데이터 |
| 마지막 3턴 | 점수 `-1` 보정 → 누적 합산(`Cumulative`) → 다음 응시용 초기화 | `JSON_test_config.Result` |

> CAFA 인덱싱 특성상 각 POS 점수는 `1`에서 시작하므로, 최종 단계에서 `-1` 보정 후 합산합니다.

### T1 / T3 — 컴팩트형 (결정론적 채점)

| Turn | 작업                                                               | 산출물 / 사용처          |
| ---- | ---------------------------------------------------------------- | ------------------ |
| 풀이   | **T1** `@RADIO(P_x@R_i@, 문항, 보기)` · **T3** `@TEXT(P_x@R_i@, 문항)` | 전 POS를 한 턴에서 응답 수집 |
| 채점   | `@MAP("@RADIO/@TEXT…@", "정답", "1\|0", EXACT)` → `@UPJ`로 점수·정오 기록 | Symbolic, LLM 미사용  |
| 피드백  | **gpt-4.1**, `markdown:true` — 전 POS 해설을 한 번에 생성                 | **그대로 학생에게 표시**    |

### T2 — POS별 확장형 (LLM 채점·피드백)

POS(Noun → Verb → Adjective → others)마다 동일한 **6-턴 블록**이 반복됩니다.

| 블록 턴 | 작업 | LLM 산출물 / 사용처 |
| --- | --- | --- |
| ① `@REPEAT` | 해당 POS 문항 루프 시작 | — |
| ② `@TEXT(P_x@R_i@, 문항)` | 학생 단답 입력 | `P_x` 저장 |
| ③ **LLM 판정** (gpt-4.1, `system`=채점 지시) | 학생답과 정답의 의미 유사도 평가 | **`1` 또는 `0`** 출력 |
| ④ 자동 채점 | 직전 LLM 결과를 `@TR@TN(-1)@[@R_i@]@`로 읽어 점수·정오 `@UPJ` | ③의 출력을 소비 |
| ⑤ **LLM 피드백** (gpt-4.1, `system`=피드백 지시, 다의어/예문 맥락 제공) | 한국어 해설 생성 | 텍스트 출력 |
| ⑥ 피드백 저장 | `@UPJ(…LLM_FBK, "@TR@TN(-1)@[@R_i@]@")@` | ⑤ 출력을 JSON에 저장 |

> `@TR@TN(-1)@`는 **직전 turn의 LLM 출력(Turn Result)**을 가져오며, `[@R_i@]`로 현재
> 반복 회차의 결과만 선택합니다. 즉 T2는 회차·POS마다 LLM을 두 번(판정 1 + 피드백 1) 호출하고,
> 그 출력이 각각 점수(`correctness`)와 `LLM_FBK`로 흘러갑니다.
> 모든 POS 종료 후 **최종 리포트** 턴과 점수 보정·초기화 턴이 이어집니다.

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

# 학생 인증 (Student Authentication)

36개 에이전트는 모두 동일한 **숫자 범위 기반(numeric-range) 인증** 방식을 사용합니다.
학생이 배부받은 일련번호(예: `26113`)를 입력하면, 그 값이 허용 범위
`ID_LOWER`(26001) ~ `ID_UPPER`(26160) 안에 있는지 검증합니다. 범위를 벗어나면
인증 입력 turn으로 다시 돌아가고, 범위 안이면 테스트 본문(turn 4)으로 진행합니다.

> **변경 이력:** 이전 방식은 단일 값(`Identification`, 예: `S-113`)과의 문자열 일치(EXACT)에
> 의존했으나, 현재는 번호 구간 비교로 전환되어 학급/그룹 단위의 연속 일련번호 배부를 지원합니다.

## 인증 파라미터

| 파라미터 | 값 / 식 | 역할 |
| --- | --- | --- |
| `ID` | `@TEXT(ID, …)@`로 입력되는 학생 일련번호 | 인증 입력값 저장 |
| `ID_LOWER` | `26001` | 허용 최소 번호 |
| `ID_UPPER` | `26160` | 허용 최대 번호 |
| `Student_auth_list` | `@COMPARE("@EVAL("@TEXT(ID)@-26000")@", "0", ">")@` `\|` `@COMPARE("@EVAL("26161-@TEXT(ID)@")@", "0", ">")@` | 두 경계 비교 결과(`true\|true`) 생성 |

`Student_auth_list`는 두 부등식을 평가합니다.

- 1차 비교: `(입력값 - 26000) > 0`  →  입력값 ≥ 26001
- 2차 비교: `(26161 - 입력값) > 0`  →  입력값 ≤ 26160

두 비교가 모두 `true`(즉 `true|true`)일 때만 인증을 통과합니다.

## 인증 turn 흐름

| Turn | 프롬프트(요약) | 동작 |
| --- | --- | --- |
| 1 | `@SET(Rand_iteration, "@N(2,5)@")@` | 문항 반복 횟수 랜덤 생성 |
| 2 | `@TEXT(ID, "…26OOO 형식…")@` | 학생 일련번호 입력 |
| 3 | `@JUMP(@MAP("@EQUAL("@Student_auth_list@", "true\|true")@", "true", "4\|@TN(-1)@", EXACT)@)@` | 범위 통과 시 turn 4, 실패 시 직전 입력 turn(`@TN(-1)@`)으로 복귀 |
| 4 | 환영 메시지 | 테스트 본문 시작 |

> **학급별 번호 구간이 다른 경우:** 해당 에이전트의 `ID_LOWER`/`ID_UPPER` 값과
> `Student_auth_list` 식 안의 경계값(`26000`, `26161`)만 함께 수정하면 됩니다.
> 그 외 채점·피드백 로직은 인증 방식과 독립적이므로 변경할 필요가 없습니다.

