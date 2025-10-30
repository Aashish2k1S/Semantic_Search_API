from fastapi import FastAPI
from pydantic import BaseModel
from vector_engine import retrieve_context
from generator import generate_answer

app = FastAPI(title="RAG AI Assistant")

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_ai(query: Query):
    context = retrieve_context(query.question)
    answer = generate_answer(query.question, context)
    return {"question": query.question, "context": context, "answer": answer}
