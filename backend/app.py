<<<<<<< HEAD
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
gemini_model = None
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel("gemini-1.5-flash")
=======
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY missing")

client = genai.Client(api_key=api_key)  # new SDK
>>>>>>> 6efec07 (Merged)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

<<<<<<< HEAD

class Message(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Server is working!"}


@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}


@app.post("/chat")
def chat(msg: Message):
    if not GEMINI_API_KEY or gemini_model is None:
        raise HTTPException(
            status_code=500,
            detail="GEMINI_API_KEY is not set. Please add it to your .env file.",
        )
    try:
        response = gemini_model.generate_content(msg.message)
        reply = response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gemini API error: {str(e)}")
    return {"message": reply}
=======
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Correct way to generate text using the new SDK
        response = client.models.generate_text(
            model="gemini-1.5-flash",  # current free model
            prompt=request.message
        )
        return {"message": response.output_text}  # output_text contains the text

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
>>>>>>> 6efec07 (Merged)
