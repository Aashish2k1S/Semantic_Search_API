# 🔍 Semantic Search API using FAISS & Sentence Transformers

This project is a simple **Semantic Search API** built using **FastAPI**, **Sentence Transformers**, and **FAISS**. The primary goal is to provide a practical understanding of how **AI models find meaning-based similarities between sentences**—a foundational concept behind advanced systems like **Retrieval-Augmented Generation (RAG)** and **ChatGPT search**.

---

## 🧠 What is Semantic Search? 

Semantic Search is the process of finding text that has a *similar meaning* rather than relying on exact keyword matches.

For example:
> The query “**Doctor helps patients**” will be considered *semantically similar* to the stored document “**Physicians treat people**.”

This mechanism is achieved using **vector embeddings**, which mathematically convert text into high-dimensional numerical representations of their meaning.

---

## 🧩 How Sentence Transformers & FAISS Work Together

Semantic Search relies on two core components:

| Component | Purpose |
| :--- | :--- |
| **Sentence Transformers** | Converts text/sentences into embeddings (dense vector numbers) that capture semantic meaning. |
| **FAISS (Facebook AI Similarity Search)** | A highly efficient library used to store and rapidly search through these embeddings to find semantically similar entries. |

### Example Workflow:
1.  **Encoding:** Encode the source text sentences using Sentence Transformers.
2.  **Indexing:** Store the resulting embeddings inside a FAISS index.
3.  **Searching:** When a new query is entered, it is first encoded, then searched against the FAISS index to get the most similar results instantly.

---

## ⚙️ Technologies Used

| Library | Purpose |
| :--- | :--- |
| `fastapi` | For building and serving the high-performance REST API. |
| `uvicorn` | ASGI server for running the FastAPI application. |
| `pydantic` | For data validation of request and response models. |
| `sentence-transformers` | For generating meaning-based text embeddings. |
| `faiss-cpu` | For fast nearest-neighbor (vector similarity) search. |
| `google-genai` | For text generation and integration with the Gemini LLM. |
| `python-dotenv` | For securely loading environment variables like API keys. |

> 💡 **Note:** You can switch `faiss-cpu` to `faiss-gpu` if your system supports CUDA for accelerated vector search.

---

## 🧰 Installation & Setup 

### 1️⃣ Clone the repository 

```bash
    git clone https://github.com/Aashish2k1S/Semantic_Search_API.git
    cd Semantic_Search_API
```

### 2️⃣ Create virtual environment & install dependencies 

```bash
    pip install -r requirements.txt
```

### 3️⃣ Add your Gemini API key 

Create a .env file in the root folder of the project:

```
    GEMINI_API_KEY=your_api_key_here
```

### 4️⃣ Run the API 

```bash 
    uvicorn main:app --reload
```

The API documentation will be live at → http://127.0.0.1:8000/docs

### 🧩 Example Request 

**Endpoint**: `POST /search`

**Request Body:**

```json
    {
        "question": "How does AI help doctors?"
    }
```

**Example Response:**

```json 
    {
        "question": "How does AI help doctors?",
        "context": [
            "AI is transforming healthcare and diagnostics.",
            "Deep learning assists in image-based medical analysis.",
            "FastAPI enables rapid API development for AI apps."
        ],
        "answer": "AI is transforming healthcare and diagnostics, offering significant assistance to doctors. It helps by revolutionizing the way medical information is processed and understood. Specifically, deep learning, a key AI technology, assists doctors with medical analysis. This support is particularly beneficial for image-based medical analysis, aiding in more accurate and efficient diagnoses."
    }
```

---

## 💡 Learning Goals

This mini-project served to solidify the following concepts:

- What **embeddings** are and how text can be represented numerically.
- The function of **FAISS** in performing rapid similarity search.
- How to expose an ML workflow through an API using **FastAPI**.
- Understanding the core **foundation of RAG** (Retrieval-Augmented Generation).

---

## 🧩Future Plans

- Add real dataset ingestion (e.g., text files, articles, PDF content) instead of mock data.
- Integrate the **Gemini or OpenAI LLM** to generate a **context-based answer** from the retrieved documents.
- Implement saving and loading of the FAISS index for persistent storage.
- Deploy the application on platforms like Render or Hugging Face Spaces.

---

## 👨‍💻 Author

**Aashish Gupta**  
.NET & Python Developer | Exploring AI Systems

🔗 [LinkedIn](https://www.linkedin.com/in/aashish2k1s) | [GitHub](https://github.com/Aashish2k1S)  

---

> 🌱 **“I’m not chasing perfection — I’m learning by doing, one project at a time.”**  



<!-- 📝 Draft for the 31 Oct Post

⚙️ Just Built: Semantic Search API with FAISS + FastAPI

This week, I explored how vector embeddings power semantic search —
enabling AI systems to understand meaning, not just keywords.

🧠 My mini project uses:

FAISS (Facebook AI Similarity Search) for vector storage

SentenceTransformers for generating embeddings

FastAPI for serving real-time semantic search queries

🔍 You can enter any query, and it returns conceptually similar results —
a foundation for RAG (Retrieval-Augmented Generation) pipelines that power modern LLM apps.

💻 GitHub: github.com/Aashish2k1S/SemanticSearchAPI

🌱 Learning AI step-by-step — from summarization to semantic understanding.

#Python #FastAPI #AI #FAISS #SemanticSearch #LLM #APIDevelopment #LearningEveryday -->
