from pydantic import BaseModel, Field

class NewChatMessageCommand(BaseModel):
    sender: str = Field(..., min_length=1, max_length=50)
    content: str = Field(..., min_length=1)