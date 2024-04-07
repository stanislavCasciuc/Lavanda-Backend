from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import FileResponse

from database import get_async_session
from models.images import ImageOrm

router = APIRouter()


@router.get("/images/{image_id}", tags=["images"])
async def get_images(image_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = select(ImageOrm).where(ImageOrm.id == image_id)
    result = await session.execute(stmt)
    image = result.scalars().first()
    return FileResponse(image.path)
