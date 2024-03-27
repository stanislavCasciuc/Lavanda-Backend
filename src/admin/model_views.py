from sqladmin import ModelView

from models import User
from api.products.models import ProductOrm, CategoryOrm


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.full_name, User.email, User.is_superuser]
    column_details_exclude_list = [User.id,User.hashed_password]
    can_create = True
    can_edit = False
    can_delete = False
    can_view_details = True
    name = "User"
    name_plural = "Users"
    icon = "fas fa-user"

class ProductAdmin(ModelView, model=ProductOrm):
    column_list = [ProductOrm.id, ProductOrm.name, ProductOrm.description, ProductOrm.price, ProductOrm.stock] + [ProductOrm.category]
    column_details_list = [ProductOrm.name, ProductOrm.description, ProductOrm.price, ProductOrm.stock] + [ProductOrm.category]
    form_excluded_columns = [ProductOrm.rating, ProductOrm.rating_count, ProductOrm.created_at, ProductOrm.updated_at]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    name = "Product"
    name_plural = "Products"
    icon = "fas fa-box"

class CategoryAdmin(ModelView, model=CategoryOrm):
    column_list = [CategoryOrm.id, CategoryOrm.name]
    form_excluded_columns = [CategoryOrm.products]
    column_details_list = [CategoryOrm.name, CategoryOrm.image] + [CategoryOrm.products]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    name = "Category"
    name_plural = "Categories"
    icon = "fas fa-tags"

