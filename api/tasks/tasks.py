from pydantic import EmailStr

import smtplib

from api.config import SMTP_USER, SMTP_HOST, SMTP_PORT, SMTP_PASS
from api.tasks.email_templates import create_comfirmation_template

def send_comfirmation_email(
        code: str,
        email_to: EmailStr
):
    msg_content = create_comfirmation_template(code, email_to)

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg_content)
