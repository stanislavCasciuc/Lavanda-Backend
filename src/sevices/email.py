import smtplib
from email.message import EmailMessage

from fastapi import BackgroundTasks

from config import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

SMP_HOST = "smtp.gmail.com"
SMP_PORT = 465


class EmailService:
    def __init__(self, user, token: str):
        self.user = user
        self.token = token

    def get_email_template_forgot_password(self):
        email = EmailMessage()
        email["From"] = EMAIL_HOST_USER
        email["To"] = self.user.email
        email["Subject"] = "Password recovery"
        html_content = f"""
                <html>
                <body>
                    <h1>Password Recovery</h1>
                    <p>Hello {self.user.full_name},</p>
                    <p>Your password recovery token is: <b>{self.token}</b></p>
                    <p>Please use this token to recover your password.</p>
                    <p>If you did not request a password recovery, please ignore this email.</p>
                    <p>Best,</p>
                    <p>Your Team</p>
                </body>
                </html>
                """

        email.add_alternative(html_content, subtype="html")
        return email

    def get_email_template_verification(self):
        email = EmailMessage()
        email["From"] = EMAIL_HOST_USER
        email["To"] = self.user.email
        email["Subject"] = "Email verification"
        html_content = f"""
                <html>
                <body>
                    <h1>Email Verification</h1>
                    <p>Hello {self.user.full_name},</p>
                    <p>Your email verification token is: <b>{self.token}</b></p>
                    <p>Please use this token to verify your email.</p>
                    <p>If you did not register, please ignore this email.</p>
                    <p>Best,</p>
                    <p>Your Team</p>
                </body>
                </html>
                """
        email.add_alternative(html_content, subtype="html")
        return email

    def send_email(self, email: EmailMessage):
        with smtplib.SMTP_SSL(SMP_HOST, SMP_PORT) as smtp:
            smtp.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            smtp.send_message(email)

    def send_email_background(
        self, email: EmailMessage, background_tasks: BackgroundTasks
    ):
        background_tasks.add_task(self.send_email, email)
