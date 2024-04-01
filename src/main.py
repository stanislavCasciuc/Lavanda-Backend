from fastapi import FastAPI
from sqladmin import Admin
from starlette.middleware.cors import CORSMiddleware

from admin.auth import AdminAuth
from admin.model_views import UserAdmin, ProductAdmin, CategoryAdmin, ReviewAdmin
from auth.router import fastapi_users, auth_backend
from auth.schemas import UserRead, UserCreate, UserUpdate
from database import engine
from auth.config import SECRET_KEY
from api.routers import all_routers

authentication_backend = AdminAuth(secret_key=SECRET_KEY)

app = FastAPI()
admin = Admin(app=app, engine=engine, authentication_backend=authentication_backend)


# AUTH ROUTES
app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
# END AUTH ROUTES
for router in all_routers:
    app.include_router(router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ADMIN
admin.add_view(UserAdmin)
admin.add_view(ProductAdmin)
admin.add_view(CategoryAdmin)
admin.add_view(ReviewAdmin)
# END ADMIN
