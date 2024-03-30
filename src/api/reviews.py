from typing import List, Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from auth.router import current_active_user
from database import get_async_session
from schemas.reviews import PostReviewSchema, GetReviewSchema
from api.util import get_product_reviews_from_db

from api.dependencies import UOWDep
from schemas.users import UserRead
from sevices.reviews import ReviewsService

router = APIRouter()


@router.post("/reviews")
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


@router.get("/reviews/{product_id}", response_model=List[GetReviewSchema])
async def get_product_reviews(
    product_id: int, session: AsyncSession = Depends(get_async_session)
):
    response = await get_product_reviews_from_db(session, product_id)
    return response
