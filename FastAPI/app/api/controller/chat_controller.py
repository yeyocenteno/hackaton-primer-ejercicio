from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.core.database import get_session
from app.api.command.new_chat_message_command import NewChatMessageCommand
from app.api.dto.chat_dto import ChatDto
from app.api.repository.chat_repository import ChatRepository
from app.api.service.chat_service import ChatService

router = APIRouter(prefix="/chat", tags=["Chat"])

def get_chat_service(session: Session = Depends(get_session)) -> ChatService:
    repository = ChatRepository(session)
    return ChatService(repository)

@router.post("/", response_model=ChatDto, status_code=status.HTTP_201_CREATED)
def create_message(
    command: NewChatMessageCommand,
    service: ChatService = Depends(get_chat_service)
):
    return service.create_message(command)

@router.get("/", response_model=List[ChatDto])
def get_all_messages(
    service: ChatService = Depends(get_chat_service)
):
    return service.get_all_messages()

@router.get("/{message_id}", response_model=ChatDto)
def get_message_by_id(
    message_id: int,
    service: ChatService = Depends(get_chat_service)
):
    message = service.get_message_by_id(message_id)
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Mensaje no encontrado"
        )
    return message