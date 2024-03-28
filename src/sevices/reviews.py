from api.reviews.schemas import PostReviewSchema
from schemas import UserRead
from utils.repository import AbstractRepository


class ReviewsService:
    def __init__(self, reviews_repository: AbstractRepository):
        self.reviews_repository: AbstractRepository = reviews_repository()

    async def add_review(self, review: PostReviewSchema, user: UserRead) -> int:
        review_dict = review.model_dump()
        review_dict["user_id"] = user.id
        review_id = await self.reviews_repository.add_one(review_dict)
        return review_id
