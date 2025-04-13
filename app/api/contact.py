from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from sqlalchemy.orm import Session
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

from app.database import get_db, supabase
from app.core.config import settings
from app.schemas.contact import ContactRequest, ContactResponse

router = APIRouter(prefix="/contact", tags=["contact"])

def send_email_background(contact: ContactRequest):
    if not settings.EMAILS_ENABLED:
        return
    
    try:
        # メール送信設定
        message = MIMEMultipart()
        message["From"] = settings.SMTP_USER
        message["To"] = settings.EMAIL_RECIPIENT
        message["Subject"] = f"ポートフォリオサイトからの問い合わせ: {contact.subject}"
        
        # メール本文
        body = f"""
        ポートフォリオサイトから問い合わせがありました。
        
        名前: {contact.name}
        メールアドレス: {contact.email}
        件名: {contact.subject}
        
        メッセージ:
        {contact.message}
        
        送信日時: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        message.attach(MIMEText(body, "plain"))
        
        # SMTP接続
        server = smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT)
        server.starttls()
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        
        # メール送信
        server.sendmail(settings.SMTP_USER, settings.EMAIL_RECIPIENT, message.as_string())
        server.quit()
        
        # Supabaseにメッセージを保存
        supabase.table("contact_messages").insert({
            "name": contact.name,
            "email": contact.email,
            "subject": contact.subject,
            "message": contact.message,
            "created_at": datetime.now().isoformat()
        }).execute()
        
    except Exception as e:
        print(f"メール送信エラー: {str(e)}")

@router.post("", response_model=ContactResponse)
async def send_contact_message(
    contact: ContactRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    try:
        # バックグラウンドでメール送信
        background_tasks.add_task(send_email_background, contact)
        
        return {
            "success": True,
            "message": "お問い合わせを受け付けました。ありがとうございます。"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 
