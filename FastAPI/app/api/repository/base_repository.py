from typing import TypeVar, Generic, Type, Optional, List, Any
from sqlmodel import Session, select, SQLModel

ModelType = TypeVar("ModelType", bound=SQLModel)

class BaseRepository(Generic[ModelType]):
    """Repositorio genérico que emula la interfaz JpaRepository de Spring Boot."""

    def __init__(self, model: Type[ModelType], session: Session):
        self.model = model
        self.session = session

    def save(self, entity: ModelType) -> ModelType:
        """Equivalente a repository.save(entity)"""
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def find_by_id(self, id_val: Any) -> Optional[ModelType]:
        """Equivalente a repository.findById(id)"""
        return self.session.get(self.model, id_val)

    def find_all(self) -> List[ModelType]:
        """Equivalente a repository.findAll()"""
        statement = select(self.model)
        return list(self.session.exec(statement).all())

    def delete_by_id(self, id_val: Any) -> bool:
        """Equivalente a repository.deleteById(id)"""
        entity = self.find_by_id(id_val)
        if entity:
            self.session.delete(entity)
            self.session.commit()
            return True
        return False