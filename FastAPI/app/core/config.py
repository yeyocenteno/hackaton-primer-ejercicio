from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Formato: postgresql://usuario:contraseña@localhost:5432/nombre_bd
    DATABASE_URL: str = "postgresql://postgres:DSC2003p@localhost:5433/chat_db"

    class Config:
        env_file = ".env"

settings = Settings()