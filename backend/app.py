from fastapi import FastAPI
from pydantic import BaseModel


class Message(BaseModel):
    message: str

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (for testing)
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {"message":"Server is working!"}
@app.get("/hello")
def hello():
    return {"message":"Hello, World!"}
@app.post("/chat")
def chat(msg: Message):
    return {"message": f"Hello Assistant! You said: {msg.message}"}