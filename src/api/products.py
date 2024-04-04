from typing import List
from fastapi import APIRouter

from api.dependencies import UOWDep

from schemas.products import GetProductSchema

from sevices.products import ProductsService

router = APIRouter()


@router.get("/products", response_model=List[GetProductSchema], tags=["products"])
async def get_products(uow: UOWDep):
    products = await ProductsService().find_products(uow=uow)
    return products
