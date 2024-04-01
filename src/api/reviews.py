from typing import List, Annotated
from fastapi import APIRouter, Depends

from auth.router import current_active_user
from schemas.reviews import PostReviewSchema, GetReviewSchema

from api.dependencies import UOWDep
from schemas.users import UserRead
from sevices.reviews import ReviewsService

router = APIRouter()


@router.post("/reviews", tags=["reviews"])
async def add_review(
    review: PostReviewSchema,
    user: Annotated[UserRead, Depends(current_active_user)],
    uow: UOWDep,
):

    review_id = await ReviewsService().add_review(
        review=review,
        user=user,
        uow=uow,
    )
    return {"review_id": review_id}


@router.get(
    "/reviews/{product_id}", response_model=List[GetReviewSchema], tags=["reviews"]
)
async def get_product_reviews(product_id: int, uow: UOWDep):
    reviews = await ReviewsService().find_product_reviews(
        product_id=product_id,
        uow=uow,
    )
    return reviews
