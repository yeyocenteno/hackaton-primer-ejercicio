from typing import List
from sqlmodel import Session, select
from app.api.entity.chat_message import ChatMessage
from app.api.repository.base_repository import BaseRepository

class ChatRepository(BaseRepository[ChatMessage]):
    def __init__(self, session: Session):
        super().__init__(ChatMessage, session)

    def find_by_sender(self, sender: str) -> List[ChatMessage]:
        statement = select(ChatMessage).where(ChatMessage.sender == sender)
        return list(self.session.exec(statement).all())