from sqlalchemy.orm import selectinload, joinedload

from models.products import ProductOrm
from schemas.products import GetProductSchema
from utils.unit_of_work import IUnitOfWork


class ProductsService:
    async def find_products(self, uow: IUnitOfWork) -> list:
        async with uow:
            products = await uow.products.find_all(
                options=[selectinload(ProductOrm.category)],
            )
        print(products[0].id)
        result = [
            GetProductSchema.model_validate(product, from_attributes=True)
            for product in products
        ]
        return result
