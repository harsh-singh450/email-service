from fastapi import APIRouter, BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, MessageType
from schemas import EmailSchema
from .transactional import conf # Re-use the config

router = APIRouter(
    prefix="/system",
    tags=["System Notifications"]
)

@router.post("/send/alert")
async def send_system_alert(email: EmailSchema, background_tasks: BackgroundTasks):
    message = MessageSchema(
        subject=f"ALERT: {email.subject}", # Prepend subject with ALERT
        recipients=email.recipients,
        template_body=email.body,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message, template_name="system_notification.html")
    
    return {"status": "success", "message": "System alert has been queued."}