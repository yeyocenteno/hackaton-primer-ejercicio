from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Notification & Chat API"
    DATABASE_URL: str = "postgresql://postgres:DSC2003p@localhost:5433/chat_db"
    
    # Configuración de Correo (Cambiamos al puerto 465 con SSL/TLS)
    MAIL_USERNAME: str = "pracdsc@gmail.com"
    MAIL_PASSWORD: str = "ykzx rslr zspv orpo"
    MAIL_FROM: str = "pracdsc@gmail.com"
    MAIL_PORT: int = 465              # <--- Cambiado de 587 a 465
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_STARTTLS: bool = False       # <--- Desactivado para puerto 465
    MAIL_SSL_TLS: bool = True         # <--- Activado para puerto 465
    USE_CREDENTIALS: bool = True
    
    # Firebase
    FIREBASE_CREDENTIALS_PATH: str = "app/core/serviceAccountKey.json"

    class Config:
        env_file = ".env"

settings = Settings()