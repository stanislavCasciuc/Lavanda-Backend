from datetime import datetime

from pydantic import BaseModel, Field
from starlette.responses import FileResponse




class GetCategorySchema(BaseModel):
    name: str
    id: int

class GetProductSchema(BaseModel):
    name: str
    description: str
    image: str
    category: GetCategorySchema
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    created_at: datetime
    updated_at: datetime

class UserRead(BaseModel):
    full_name: str
    email: str
    is_active: bool
    is_superuser: bool
