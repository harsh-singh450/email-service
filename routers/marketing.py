from fastapi import APIRouter, BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, MessageType
from schemas import EmailSchema
from .transactional import conf # Re-use the config

router = APIRouter(
    prefix="/marketing",
    tags=["Marketing & Product Updates"]
)

@router.post("/send/campaign")
async def send_marketing_campaign(email: EmailSchema, background_tasks: BackgroundTasks):
    message = MessageSchema(
        subject=email.subject,
        recipients=email.recipients,
        template_body=email.body,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message, template_name="marketing_template.html")
    
    return {"status": "success", "message": "Marketing campaign has been queued."}