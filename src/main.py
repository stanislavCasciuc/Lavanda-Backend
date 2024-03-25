from fastapi import FastAPI
from sqladmin import Admin, ModelView

from admin.auth import AdminAuth
from auth.router import fastapi_users, auth_backend
from auth.schemas import UserRead, UserCreate, UserUpdate
from database import engine
from models import User
from products.models import ProductOrm
from auth.config import SECRET_KEY
from products.router import router as products_router
from review.router import router as review_router

authentication_backend = AdminAuth(secret_key=SECRET_KEY)

app = FastAPI()
admin = Admin(app=app, engine=engine, authentication_backend=authentication_backend)


#ROUTES
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
app.include_router(
    products_router,
    prefix="/api",
    tags=["products"]
)
app.include_router(
    review_router,
    prefix="/api",
    tags=["reviews"]
)
#END ROUTES


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.full_name, User.email, User.is_superuser]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True

class ProductAdmin(ModelView, model=ProductOrm):
    column_list = [ProductOrm.id, ProductOrm.name, ProductOrm.description, ProductOrm.price, ProductOrm.stock]
    form_excluded_columns = [ProductOrm.created_at, ProductOrm.updated_at, ProductOrm.rating, ProductOrm.rating_count]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True




#ADMIN
admin.add_view(UserAdmin)
admin.add_view(ProductAdmin)
#END ADMIN




