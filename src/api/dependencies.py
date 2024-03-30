from typing import Annotated

from fastapi import Depends

from repositories.products import ProductsRepository
from repositories.reviews import ReviewsRepository
from sevices.reviews import ReviewsService
from sevices.products import ProductsService
from utils.unit_of_work import IUnitOfWork, UnitOfWork


# def get_reviews_service():
#     return ReviewsService(ReviewsRepository)
#
#
# def get_products_service():
#     return ProductsService(ProductsRepository)


UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
