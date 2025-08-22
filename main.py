from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("Secret_key"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AIRequest(BaseModel):
    prompt: str
    
@app.post("/ask-ai")
async def ask_ai(request: AIRequest):
    """
    Receives a prompt from frontend and sends it to OpenAI's API.
    Returns AI's response.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a personal tech tutor skilled in Python, JavaScript, Docker, Git, CLI, Command line prompts and software deployment. Explain clearly and give examples"
                },
                {
                    "role": "user",
                    "content": request.prompt
                }
            ],
            temperature=0.5
        )
        
        return {
            "response": response.choices[0].message.content
        }
    except Exception as e:
        return {"error": str(e)}