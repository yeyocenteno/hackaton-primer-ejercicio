from fastapi import FastAPI
from app.core.database import init_db
from app.api.controller import chat_controller

app = FastAPI(
    title="Chat FastAPI Application",
    description="API estructurada en 3 capas estilo Spring Boot",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(chat_controller.router)