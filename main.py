from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth import router as auth_router
from chat import router as chat_router
from database import engine, Base  # import your engine and Base
from models import User  # import all models here

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router, prefix="/api/auth")
app.include_router(chat_router, prefix="/api")

# ---------- Add this startup event ----------
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    print("✅ All tables are created (if not exist)")
