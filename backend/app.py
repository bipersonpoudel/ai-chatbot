<<<<<<< HEAD
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
=======
from urllib import response

>>>>>>> a70f3f1 (Debugged API issue)
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
        response = client.models.generate_content(
            model="models/gemini-flash-latest",  # your working model
            contents=request.message
        )
        return {"message": response.text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
<<<<<<< HEAD
>>>>>>> 6efec07 (Merged)
=======


# @app.post("/chat")
# async def chat(request: ChatRequest):
#     try:
#         response = client.models.generate_content(
#             model="gemini-1.5-flash",
#             contents=request.message
#         )
#         return {"message": response.text}

#     except Exception as e:
#         import traceback
#         traceback.print_exc()
#         raise HTTPException(status_code=500, detail=str(e))
>>>>>>> a70f3f1 (Debugged API issue)
