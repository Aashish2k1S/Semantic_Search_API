import os, dotenv
from google import genai

dotenv.load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY")) 

def generate_answer(question, context_list):
    context_text = "\n".join(context_list)
    prompt = f"""
    Use the following context to answer the question.
    Context:
    {context_text}

    Question:
    {question}

    Answer in 4-5 concise sentences, only using provided context.
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )

    return response.text

