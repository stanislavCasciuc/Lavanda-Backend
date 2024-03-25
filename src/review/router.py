from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from auth.router import current_active_user
from database import get_async_session
from products.models import ProductOrm
from .models import ReviewOrm
from models import User
from review.schemas import PostReview

router = APIRouter()

@router.post("/reviews")
async def create_review(review: PostReview, user: User = Depends(current_active_user), session: AsyncSession = Depends(get_async_session)):
    stmt = insert(ReviewOrm).values(
        product_id=review.product_id,
        rating=review.rating,
        comment=review.comment,
        name=review.name,
        user_id=user.id
    )
    await session.execute(stmt)
    stmt = update(ProductOrm).where(ProductOrm.id == review.product_id).values(rating=ProductOrm.rating + review.rating, rating_count=ProductOrm.rating_count + 1)
    await session.execute(stmt)
    await session.commit()
    return {"message": "Review created successfully."}

# @router.get("/reviews/{product_id}")

