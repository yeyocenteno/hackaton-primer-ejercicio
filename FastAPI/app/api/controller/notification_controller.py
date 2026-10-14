from fastapi import APIRouter, HTTPException
from app.api.dto.notification_dto import EmailRequestDto, PushNotificationRequestDto
from app.api.service.notification_service import NotificationService

router = APIRouter(prefix="/notifications", tags=["Notifications"])

@router.post("/email")
async def send_email_endpoint(payload: EmailRequestDto):
    try:
        result = await NotificationService.send_email(
            email_to=payload.email,
            subject=payload.subject,
            body_text=payload.message
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/push")
async def send_push_endpoint(payload: PushNotificationRequestDto):
    try:
        result = NotificationService.send_push_notification(
            token=payload.token,
            title=payload.title,
            body=payload.body
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))