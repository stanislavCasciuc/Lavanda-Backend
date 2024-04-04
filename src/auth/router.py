import uuid
from typing import Optional
from fastapi import Depends, Request, BackgroundTasks
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from auth.config import SECRET_KEY
from auth.utils import get_user_db
from models.users import User
from sevices.email import EmailService

SECRET = SECRET_KEY


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    def __init__(
        self, user_db: SQLAlchemyUserDatabase, background_tasks: BackgroundTasks
    ):
        super().__init__(user_db)
        self.background_tasks = background_tasks

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self,
        user: User,
        token: str,
        request: Optional[Request] = None,
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")

        email_service = EmailService(user=user, token=token)
        template = email_service.get_email_template_verification()
        email_service.send_email_background(
            email=template, background_tasks=self.background_tasks
        )
        return {"message": "Email sent"}


async def get_user_manager(
    background_tasks: BackgroundTasks, user_db=Depends(get_user_db)
):
    yield UserManager(user_db, background_tasks)


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
