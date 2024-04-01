from email.message import EmailMessage

from config import EMAIL_HOST_USER


class EmailService:
    def __init__(self, email_client):
        self.email_client = email_client

    def send_email(self, email):
        self.email_client.send_email(email)

    def get_email_template_forgot_password(self, user, token):
        email = EmailMessage()
        email["From"] = EMAIL_HOST_USER
        email["To"] = user.email
        email["Subject"] = "Password recovery"
        html_content = f"""
                <html>
                <body>
                    <h1>Password Recovery</h1>
                    <p>Hello {user.name},</p>
                    <p>Your password recovery token is: <b>{token}</b></p>
                    <p>Please use this token to recover your password.</p>
                    <p>If you did not request a password recovery, please ignore this email.</p>
                    <p>Best,</p>
                    <p>Your Team</p>
                </body>
                </html>
                """

        # Attach the HTML content
        email.add_alternative(html_content, subtype="html")
        return email

    def get_email_template_verification(self, user, token):
        email = EmailMessage()
        email["From"] = EMAIL_HOST_USER
        email["To"] = user.email
        email["Subject"] = "Email verification"
        html_content = f"""
                <html>
                <body>
                    <h1>Email Verification</h1>
                    <p>Hello {user.name},</p>
                    <p>Your email verification token is: <b>{token}</b></p>
                    <p>Please use this token to verify your email.</p>
                    <p>If you did not register, please ignore this email.</p>
                    <p>Best,</p>
                    <p>Your Team</p>
                </body>
                </html>
                """

        # Attach the HTML content
        email.add_alternative(html_content, subtype="html")
        return email
