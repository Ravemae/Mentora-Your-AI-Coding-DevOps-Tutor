from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("Secret_key"))

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Prompt(BaseModel):
    user_input: str

# Root endpoint (avoids 404 on `/`)
@app.get("/")
async def root():
    return {"message": "DevBot API is running."}

# Chat endpoint
@app.post("/chat")
async def chat(prompt: Prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt.user_input}]
        )
        response_text = response.choices[0].message.content
        return {"response": response_text}
    except Exception as e:
        return {"error": str(e)}
