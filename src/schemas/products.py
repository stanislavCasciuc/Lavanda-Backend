from datetime import datetime

from pydantic import BaseModel, Field


class GetCategorySchema(BaseModel):
    name: str
    id: int


class GetProductSchema(BaseModel):
    id: int
    name: str
    description: str
    image: str
    category: GetCategorySchema
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    created_at: datetime
    updated_at: datetime
    rating: int
    rating_count: int

    class Config:
        from_attributes = True


class UserRead(BaseModel):
    full_name: str
    email: str
    is_active: bool
    is_superuser: bool
