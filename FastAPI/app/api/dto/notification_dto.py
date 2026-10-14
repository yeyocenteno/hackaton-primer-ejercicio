from pydantic import BaseModel, EmailStr

class EmailRequestDto(BaseModel):
    email: EmailStr
    subject: str
    message: str

class PushNotificationRequestDto(BaseModel):
    token: str
    title: str
    body: str