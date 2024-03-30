from datetime import timedelta

from fastapi import Depends
from sqladmin.authentication import AuthenticationBackend
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request
from starlette.responses import RedirectResponse

from admin.util import authenticate_user, create_access_token, get_current_user
from database import get_async_session


class AdminAuth(AuthenticationBackend):
    async def login(
        self, request: Request, session: AsyncSession = Depends(get_async_session)
    ) -> bool:
        form = await request.form()
        email, password = form["username"], form["password"]
        user = await authenticate_user(email, password)
        if not user:
            return RedirectResponse(url="/admin/login")
        access_token_expires = timedelta(seconds=3600)
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )

        request.session.update({"token": access_token})

        return True

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return RedirectResponse(url="/admin/login")

        user = await get_current_user(token)
        if not user:
            return False
        if not user.is_superuser:
            return False
        return True
