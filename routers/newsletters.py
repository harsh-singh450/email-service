from fastapi import APIRouter, BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, MessageType
from schemas import EmailSchema
from .transactional import conf # Re-use the config from another router

router = APIRouter(
    prefix="/newsletters",
    tags=["Newsletters"]
)

@router.post("/send")
async def send_newsletter(email: EmailSchema, background_tasks: BackgroundTasks):
    message = MessageSchema(
        subject=email.subject,
        recipients=email.recipients,
        template_body=email.body,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message, template_name="newsletter_template.html")
    
    return {"status": "success", "message": "Newsletter has been queued for sending."}