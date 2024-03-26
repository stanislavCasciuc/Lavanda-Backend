from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import insert, update, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from auth.router import current_active_user
from database import get_async_session
from products.models import ProductOrm
from .models import ReviewOrm
from models import User
from reviews.schemas import PostReviewSchema, GetReviewSchema
from .util import get_product_reviews_from_db, insert_review_into_db

router = APIRouter()

@router.post("/reviews")
async def create_review(review: PostReviewSchema, user: User = Depends(current_active_user), session: AsyncSession = Depends(get_async_session)):
    await insert_review_into_db(session, review, user)
    return {"message": "Review created successfully."}

@router.get("/reviews/{product_id}", response_model=List[GetReviewSchema])
async def get_product_reviews(product_id: int, session: AsyncSession=Depends(get_async_session)):
    response = await get_product_reviews_from_db(session, product_id)
    return response

