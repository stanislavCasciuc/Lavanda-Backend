from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import FileResponse

from database import get_async_session
from products.models import ProductOrm

router = APIRouter()

@router.get("/products")
async def create_product(session: AsyncSession = Depends(get_async_session)):
    stmt = select(ProductOrm)
    result = await session.execute(stmt)
    query = result.scalars().all()
    return query


@router.get("/images/{image}")
async def get_images(image: str):
    return FileResponse("src/" + image)
