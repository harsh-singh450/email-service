from fastapi import APIRouter, BackgroundTasks
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from schemas import EmailSchema
from config import settings

router = APIRouter(
    prefix="/transactional",
    tags=["Transactional Emails"]
)

# Configuration for fastapi-mail
conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS=settings.MAIL_STARTTLS,
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER='./templates'
)

@router.post("/send/password-reset")
async def send_password_reset_email(email: EmailSchema, background_tasks: BackgroundTasks):
    message = MessageSchema(
        subject=email.subject,
        recipients=email.recipients,
        template_body=email.body,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    # Add the send_message task to the background
    background_tasks.add_task(fm.send_message, message, template_name="password_reset_template.html")

    return {"status": "success", "message": "Password reset email has been queued."}


@router.post("/send/simple")
async def send_simple_email(email: EmailSchema, background_tasks: BackgroundTasks):
    # This endpoint assumes email.body is a simple string
    message = MessageSchema(
        subject=email.subject,
        recipients=email.recipients,
        body=email.body, # Directly use the string body
        subtype=MessageType.plain # Send as plain text
    )

    fm = FastMail(conf)
    background_tasks.add_task(fm.send_message, message)

    return {"status": "success", "message": "Simple email has been queued."}