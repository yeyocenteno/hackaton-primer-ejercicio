from typing import Generator
from sqlmodel import SQLModel, Session, create_engine
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)

def init_db() -> None:
    """Crea las tablas en PostgreSQL 17 si no existen."""
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    """Inyección de dependencia para obtener la sesión de BD por petición."""
    with Session(engine) as session:
        yield session