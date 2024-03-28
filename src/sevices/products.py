from utils.repository import AbstractRepository


class ProductsService:
    def __init__(self, product_repository: AbstractRepository):
        self.product_repository: AbstractRepository = product_repository()

    async def update_product(self, product_id: int, product_data: dict) -> int:
        product_id = await self.product_repository.update_one_by_id(
            id=product_id, data=product_data
        )
        return product_id

    async def update_product_rating(self, product_id: int, product_data: dict) -> int:
        product_id = await self.product_repository.update_one_by_id(
            id=product_id, data=product_data
        )
        return product_id
