from typing import List, Optional
from app.api.entity.chat_message import ChatMessage
from app.api.command.new_chat_message_command import NewChatMessageCommand
from app.api.dto.chat_dto import ChatDto
from app.api.repository.chat_repository import ChatRepository

class ChatService:
    def __init__(self, chat_repository: ChatRepository):
        self.chat_repository = chat_repository

    def create_message(self, command: NewChatMessageCommand) -> ChatDto:
        message_entity = ChatMessage(
            sender=command.sender,
            content=command.content
        )
        saved_message = self.chat_repository.save(message_entity)
        return ChatDto.model_validate(saved_message)

    def get_all_messages(self) -> List[ChatDto]:
        messages = self.chat_repository.find_all()
        return [ChatDto.model_validate(msg) for msg in messages]

    def get_message_by_id(self, message_id: int) -> Optional[ChatDto]:
        message = self.chat_repository.find_by_id(message_id)
        if message:
            return ChatDto.model_validate(message)
        return None