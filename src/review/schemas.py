from pydantic import BaseModel, Field


class ReviewUser(BaseModel):
    username: str
    email: str


class PostReview(BaseModel):
    product_id: int
    name: str
    comment: str
    rating: int = Field(..., ge=1, le=5)

class Review(PostReview):
    id: int
    product_id: int
    username: ReviewUser