from datetime import datetime
from pydantic import BaseModel, ConfigDict


class ChatDto(BaseModel):
    id: int
    sender: str
    content: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)