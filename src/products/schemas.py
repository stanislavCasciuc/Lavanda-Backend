from pydantic import BaseModel, Field
from starlette.responses import FileResponse

from products.models import Category





class Product(BaseModel):
    name: str
    description: str
    image: FileResponse
    category: Category
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    created_at: str
    updated_at: str

class UserRead(BaseModel):
    full_name: str
    email: str
    is_active: bool
    is_superuser: bool
