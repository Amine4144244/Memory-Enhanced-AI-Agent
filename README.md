# 🧠 Memory-Enhanced Agent — Stateful AI with Selective Memory & Evaluation

> A production-style AI agent that **selectively stores, updates, and retrieves user knowledge** to improve responses over time—backed by **scoring, compression, and evaluation**.

---

## 🚀 Why this project stands out

Most “memory agents” just dump conversations into a vector DB.

This system is different:

* 🎯 **Selective memory** (store only high-value information)
* 🔄 **Memory updates** (handle contradictions & changes over time)
* 🧩 **Structured memory schema** (not raw text blobs)
* 🔍 **Hybrid retrieval** (similarity + importance + recency)
* 🧪 **Evaluation-first design** (measure usefulness, not just output)

---

## 🧠 Problem Statement

Naive approaches treat memory as storage:

* Save everything
* Retrieve by similarity

This leads to:

* ❌ Noise accumulation
* ❌ Contradictions
* ❌ Irrelevant context injection

👉 This project builds a system that **manages memory like a resource**, not a dump.

---

## 🏗️ Architecture Overview

```
User Input
   ↓
Short-Term Memory (context window)
   ↓
LLM Response
   ↓
Memory Processor
   ├── Extract candidate memories
   ├── Score importance
   ├── Update / resolve conflicts
   └── Store in vector DB
   ↓
Memory Retrieval (next turn)
   ↓
Augmented Prompt → Better Response
```

---

## 🧠 Memory Design

### 1) Short-Term Memory (Working Context)

* Token-based sliding window
* Keeps recent + relevant turns only
* Prevents context overflow

---

### 2) Long-Term Memory (Semantic Store)

Stored as **structured objects** (not raw text):

```json
{
  "type": "preference",
  "content": "User prefers Python over JavaScript",
  "timestamp": "2026-04-18",
  "confidence": 0.9,
  "frequency": 2
}
```

**Memory Types**

* Preferences
* Goals
* Skills
* Decisions
* Constraints

---

### 3) Memory Compression

* Conversation summaries → preserve context
* Memory extraction → persist key knowledge

👉 Prevents long-term memory pollution

---

## 🎯 What Counts as “Important Memory”

A memory is stored only if it is:

* **Durable** → useful across sessions
* **Impactful** → changes future responses
* **Reinforced** → repeated or confirmed
* **Decisive** → explicit user commitment

---

## 🧮 Memory Scoring

```python
score = (
    0.4 * durability +
    0.3 * impact +
    0.2 * frequency +
    0.1 * confidence
)
```

Store only if:

```python
score > threshold
```

👉 Prevents over-storage and noise

---

## 🔄 Memory Update & Conflict Resolution

Handles evolving user preferences:

**Example:**

* Old → "Prefers Python"
* New → "Switched to Node.js"

**System behavior:**

* Update existing memory
* Lower confidence of outdated info
* Maintain optional history

---

## 🔍 Retrieval Strategy (Hybrid)

Instead of naive similarity search:

Combine:

* Semantic similarity
* Importance score
* Recency weighting
* Frequency signal

```python
final_score = (
    0.5 * similarity +
    0.2 * importance +
    0.2 * recency +
    0.1 * frequency
)
```

👉 Retrieve **top 5–7 relevant memories only**

---

## 🧠 Memory-Aware Prompting

```text
User Profile:
- Prefers Python
- Building AI agents

Relevant Past Context:
- Recently explored LangGraph

Current Question:
{query}

Instruction:
Use memory only if relevant.
```

---

## ⚠️ Failure Modes Addressed

* ❌ Memory pollution → scoring + thresholds
* ❌ Contradictions → update logic
* ❌ Over-retrieval → capped ranked recall
* ❌ Stale memory → recency decay

---

## 📊 Evaluation Framework

### Memory Metrics

* **Memory Precision** → % of useful stored memories
* **Memory Recall** → ability to remember correct info

### System Metrics

* **Response Improvement** → with vs without memory
* **Consistency** → avoids contradictions
* **Personalization Score** → relevance to user context

---

## 🗂️ Project Structure

```
memory-agent/
│
├── app/
│   ├── main.py
│   ├── config.py
│
│   ├── memory/
│   │   ├── short_term.py
│   │   ├── long_term.py
│   │   ├── memory_store.py
│   │   ├── memory_retriever.py
│   │   └── memory_scorer.py
│
│   ├── extraction/
│   │   ├── extractor.py
│   │   └── prompts.py
│
│   ├── update/
│   │   └── memory_updater.py
│
│   ├── agent/
│   │   ├── agent_core.py
│   │   └── reasoning.py
│
│   ├── evaluation/
│   │   ├── metrics.py
│   │   └── test_cases.json
│
│   └── utils/
│       └── helpers.py
│
├── data/
├── notebooks/
├── tests/
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* Python
* LangChain / LangGraph
* ChromaDB (vector memory)
* OpenAI / local LLM (Ollama)

---

## 🔁 Execution Flow

1. User sends message
2. Short-term memory builds context
3. Retrieve relevant long-term memory
4. Generate response
5. Extract candidate memories
6. Score + filter
7. Update memory store

---

## 📈 Example

**User:** “I’m learning LangGraph and building AI agents”

**Stored Memory:**

* Goal: building AI agents
* Skill: learning LangGraph

**Later Query:** “What should I learn next?”

**Agent Response:**

* Recommends advanced agent workflows
* Suggests LangGraph projects

👉 Personalized, not generic

---

## 🚀 Future Improvements

* Memory decay (automatic forgetting)
* Self-reflection (agent decides what to store)
* User-editable memory
* UI dashboard for memory inspection

---

## 🧨 Key Insight

> Memory is not about storing everything.
> It’s about storing what **changes future behavior**.

---

## 📬 Contact

Open to opportunities and collaborations.

---

⭐ If you found this interesting, consider starring the repo.
