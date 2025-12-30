from fastapi import APIRouter
from schemas import MessageCreate
import requests, os

router = APIRouter()

@router.post("/chat/send")
def chat_send(payload: MessageCreate):
    key = os.getenv("OPENROUTER_API_KEY")
    if not key:
        return {"text": f"Fake reply: {payload.message}"}
    resp = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {key}"},
        json={
            "model": "mistralai/mistral-7b-instruct:free",
            "messages":[{"role":"user","content": payload.message}]
        }
    )
    return resp.json()
