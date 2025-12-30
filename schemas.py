from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str
    class Config:
        orm_mode = True

class MessageCreate(BaseModel):
    message: str

class MoodCreate(BaseModel):
    mood: str

class JournalCreate(BaseModel):
    content: str
