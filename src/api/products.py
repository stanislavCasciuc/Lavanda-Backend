from typing import List, Annotated
from fastapi import APIRouter

from api.dependencies import UOWDep
from auth.router import current_active_user

from schemas.products import (
    GetProductSchema,
    GetCategorySchema,
    UserRead,
    PostCategorySchema,
)

from sevices.products import ProductsService

router = APIRouter()


@router.get("/products", response_model=List[GetProductSchema], tags=["products"])
async def get_products(uow: UOWDep):
    products = await ProductsService().find_products(uow=uow)
    return products


@router.get(
    "/products/{product_id}", response_model=GetProductSchema, tags=["products"]
)
async def get_product(product_id: int, uow: UOWDep):
    product = await ProductsService().find_product(product_id=product_id, uow=uow)
    return product


@router.get("/categories", tags=["categories"], response_model=List[GetCategorySchema])
async def get_categories(uow: UOWDep):
    categories = await ProductsService().find_categories(uow=uow)
    return categories


@router.post("/categories", tags=["categories"])
async def create_category(
    category: PostCategorySchema,
    uow: UOWDep,
    user=Annotated[UserRead, current_active_user],
):
    category = await ProductsService().create_category(
        category=category, uow=uow, user=user
    )
    return category
