from fastapi import FastAPI
from app.core.database import init_db
from app.api.controller import chat_controller, notification_controller

app = FastAPI(
    title="Chat & Notification FastAPI Application",
    description="API estructurada en 3 capas estilo Spring Boot con soporte de Chat y Notificaciones",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    init_db()

# Registrar los routers de los controladores
app.include_router(chat_controller.router)
app.include_router(notification_controller.router)