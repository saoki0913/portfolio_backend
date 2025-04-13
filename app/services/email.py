import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Dict, Any

from app.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_email(
    email_to: str,
    subject: str,
    html_content: str,
    environment: Dict[str, Any] = {},
) -> bool:
    if not settings.EMAILS_ENABLED:
        logger.info(f"Would send email: {subject} to {email_to}")
        logger.info(f"Content: {html_content}")
        return True

    try:
        message = MIMEMultipart()
        message["From"] = f"{settings.EMAILS_FROM_NAME} <{settings.EMAILS_FROM_EMAIL}>"
        message["To"] = email_to
        message["Subject"] = subject
        message.attach(MIMEText(html_content, "html"))

        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            if settings.SMTP_TLS:
                server.starttls()
            if settings.SMTP_USER and settings.SMTP_PASSWORD:
                server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            server.sendmail(
                settings.EMAILS_FROM_EMAIL, email_to, message.as_string()
            )
        
        logger.info(f"Email sent successfully to {email_to}")
        return True
    
    except Exception as e:
        logger.error(f"Failed to send email to {email_to}: {e}")
        return False

def send_contact_email(name: str, email: str, subject: str, message: str) -> bool:
    """
    問い合わせメールを管理者に送信する
    """
    html_content = f"""
    <h2>ポートフォリオサイトからの問い合わせ</h2>
    <p><strong>名前:</strong> {name}</p>
    <p><strong>メールアドレス:</strong> {email}</p>
    <p><strong>件名:</strong> {subject}</p>
    <p><strong>メッセージ:</strong></p>
    <p>{message}</p>
    """
    
    return send_email(
        email_to=settings.EMAIL_RECIPIENT,
        subject=f"ポートフォリオサイトからの問い合わせ: {subject}",
        html_content=html_content,
    ) 
