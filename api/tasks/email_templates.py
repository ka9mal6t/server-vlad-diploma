from email.message import EmailMessage
from api.config import SMTP_USER
from pydantic import EmailStr


def create_comfirmation_template(
        code: str,
        email_to: EmailStr,

):
    email = EmailMessage()

    email['Subject'] = "Підтвердіть свою пошту"
    email['From'] = SMTP_USER
    email['To'] = email_to

    email.set_content(
        f"""
        <h1>Підтвердіть свою пошту<h1>
        <a href="http://127.0.0.1:8000/auth/confirm_email/{code}" 
        style="display: inline-block; padding: 10px 20px; 
        background-color: #007bff; color: #fff; 
        text-decoration: none; border-radius: 5px;">Підтвердити</a>
        
        """,
        subtype="html"
    )
    return email
