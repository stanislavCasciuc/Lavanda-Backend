from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from api.dependencies import UOWDep
from database import get_async_session
from models.products import ProductOrm
from schemas.products import GetProductSchema
from sevices.products import ProductsService
from utils.unit_of_work import UnitOfWork

router = APIRouter()


@router.get("/products", response_model=List[GetProductSchema], tags=["products"])
async def get_products(uow: UOWDep):
    products = await ProductsService().find_products(uow=uow)
    return products


@router.get("/products1", response_model=List[GetProductSchema])
async def create_product():
    uow = UnitOfWork()
    async with uow:
        products = await uow.products.find_all(
            options=[selectinload(ProductOrm.category)],
        )
    result = [
        GetProductSchema.model_validate(product, from_attributes=True)
        for product in products
    ]
    return result
