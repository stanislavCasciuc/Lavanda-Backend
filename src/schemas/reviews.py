from datetime import datetime

from pydantic import BaseModel, Field


class ReviewUserSchema(BaseModel):
    full_name: str
    email: str


class PostReviewSchema(BaseModel):
    product_id: int
    name: str
    comment: str
    rating: int = Field(..., ge=1, le=5)


class GetReviewSchema(PostReviewSchema):
    id: int
    user: ReviewUserSchema
    created_at: datetime
