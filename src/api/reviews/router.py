from typing import List, Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from auth.router import current_active_user
from database import get_async_session
from api.reviews.schemas import PostReviewSchema, GetReviewSchema
from api.reviews.util import get_product_reviews_from_db

from api.dependencies import get_reviews_service, get_products_service
from schemas import UserRead
from sevices.products import ProductsService
from sevices.reviews import ReviewsService

router = APIRouter()


@router.post("/reviews")
async def create_review(
    review: PostReviewSchema,
    user: Annotated[UserRead, Depends(current_active_user)],
    reviews_service: Annotated[ReviewsService, Depends(get_reviews_service)],
    product_service: Annotated[ProductsService, Depends(get_products_service)],
):
    review_id = await reviews_service.add_review(review, user)
    await product_service.update_product(review.product_id, {"rating": review.rating})
    return {"review_id": review_id}


@router.get("/reviews/{product_id}", response_model=List[GetReviewSchema])
async def get_product_reviews(
    product_id: int, session: AsyncSession = Depends(get_async_session)
):
    response = await get_product_reviews_from_db(session, product_id)
    return response
