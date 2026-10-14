from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr
import firebase_admin
from firebase_admin import credentials, messaging
from app.core.config import settings
import os

# Configuración de FastAPI-Mail
conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS=settings.MAIL_STARTTLS,
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
    USE_CREDENTIALS=settings.USE_CREDENTIALS
)

# Inicializar Firebase Admin SDK (si existe el archivo de credenciales)
if os.path.exists(settings.FIREBASE_CREDENTIALS_PATH):
    if not firebase_admin._apps:
        cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
        firebase_admin.initialize_app(cred)

class NotificationService:

    @staticmethod
    async def send_email(email_to: EmailStr, subject: str, body_text: str):
        message = MessageSchema(
            subject=subject,
            recipients=[email_to],
            body=body_text,
            subtype=MessageType.plain
        )
        fm = FastMail(conf)
        await fm.send_message(message)
        return {"message": f"Correo enviado exitosamente a {email_to}"}

    @staticmethod
    def send_push_notification(token: str, title: str, body: str):
        if not os.path.exists(settings.FIREBASE_CREDENTIALS_PATH):
            raise Exception("Archivo serviceAccountKey.json de Firebase no encontrado en app/core/")
            
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            token=token,
        )
        response = messaging.send(message)
        return {"message": "Notificación Push enviada con éxito", "firebase_response": response}