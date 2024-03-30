from schemas.reviews import PostReviewSchema
from schemas.users import UserRead
from utils.unit_of_work import IUnitOfWork


class ReviewsService:
    async def add_review(
        self,
        uow: IUnitOfWork,
        review: PostReviewSchema,
        user: UserRead,
    ) -> int:
        review_dict = review.model_dump()
        review_dict["user_id"] = user.id
        async with uow:
            review_id = await uow.reviews.add_one(review_dict)

            product = await uow.products.find_one(id=review.product_id)
            product_rating = {
                "rating": (product.rating + review.rating),
                "rating_count": (product.rating_count + 1),
            }
            await uow.products.update_one(id=review.product_id, data=product_rating)
            await uow.commit()

        return review_id
