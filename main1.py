# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from openai import OpenAI
# import os
# from dotenv import load_dotenv

# load_dotenv()

# client = OpenAI(api_key=os.getenv("Secret_key"))

# app = FastAPI(title="DevBot API", description="AI Coding + DevOps Tutor", version="1.0.0")

# # CORS (adjust origins as needed)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],  
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class Prompt(BaseModel):
#     user_input: str

# @app.get("/")
# async def root():
#     return {"message": "DevBot API is running."}

# @app.post("/chat")
# async def chat(prompt: Prompt):
#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o",  
#             messages=[
#                 {
#                     "role": "system",
#                     "content": (
#                         "You are DevBot, an AI coding and DevOps tutor. "
#                         "You help beginners learn Python, JavaScript, Git, Docker, and terminal commands. "
#                         "Provide clear, beginner-friendly answers with examples."
#                     )
#                 },
#                 {"role": "user", "content": prompt.user_input}
#             ]
#         )
#         return {"response": response.choices[0].message.content}
#     except Exception as e:
#         return {"error": str(e)}
