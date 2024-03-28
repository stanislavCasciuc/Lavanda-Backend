from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from starlette.responses import FileResponse

from database import get_async_session
from api.products.models import ProductOrm
from api.products.schemas import GetProductSchema

router = APIRouter()


@router.get("/products", response_model=List[GetProductSchema])
async def create_product(session: AsyncSession = Depends(get_async_session)):
    stmt = select(ProductOrm).options(selectinload(ProductOrm.category))
    result = await session.execute(stmt)
    query = result.scalars().all()
    return query


@router.get("/images/{image}")
async def get_images(image: str):
    return FileResponse(image)
