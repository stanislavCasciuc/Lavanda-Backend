from datetime import datetime

from fastapi import UploadFile
from pydantic import BaseModel, Field


class ImageSchema(BaseModel):
    id: int
    path: str


class PostCategorySchema(BaseModel):
    name: str
    image: UploadFile


class GetCategorySchema(PostCategorySchema):
    id: int
    image: ImageSchema
    products_count: int


class CategoryRead(BaseModel):
    id: int
    name: str


class GetProductSchema(BaseModel):
    id: int
    name: str
    description: str
    image: ImageSchema
    category: CategoryRead
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
