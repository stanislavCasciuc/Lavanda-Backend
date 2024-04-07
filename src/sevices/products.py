from sqlalchemy.orm import selectinload, joinedload

from models.products import ProductOrm, CategoryOrm
from schemas.exceptions import NotSuperUserException
from schemas.products import (
    GetProductSchema,
    GetCategorySchema,
    PostCategorySchema,
    UserRead,
)
from utils.unit_of_work import IUnitOfWork


class ProductsService:
    async def find_products(self, uow: IUnitOfWork) -> list:
        async with uow:
            products = await uow.products.find_all(
                options=[
                    selectinload(ProductOrm.category),
                    selectinload(ProductOrm.image),
                ],
            )
        result = [
            GetProductSchema.model_validate(product.to_read(), from_attributes=True)
            for product in products
        ]
        return result

    async def find_product(self, product_id: int, uow: IUnitOfWork) -> GetProductSchema:
        async with uow:
            product = await uow.products.find_one(
                filter={"id": product_id},
                options=[
                    selectinload(ProductOrm.category),
                    selectinload(ProductOrm.image),
                ],
            )
        return GetProductSchema.model_validate(product.to_read(), from_attributes=True)

    async def find_categories(self, uow: IUnitOfWork) -> list:
        async with uow:
            categories = await uow.categories.find_all(
                options=[
                    selectinload(CategoryOrm.image),
                    selectinload(CategoryOrm.products),
                ]
            )
        result = [
            GetCategorySchema.model_validate(category.to_dict(), from_attributes=True)
            for category in categories
        ]
        return result

    async def create_category(
        self, category: PostCategorySchema, uow: IUnitOfWork, user: UserRead
    ) -> GetCategorySchema:
        if user.is_superuser is False:
            raise NotSuperUserException
        async with uow:
            image_id = await uow.images.add_one(
                {
                    "path": category.image.file,
                }
            )
            category_id = await uow.products.add_one(
                {
                    "name": category.name,
                    "image": image_id,
                }
            )
        return {"image_id": image_id, "category_id": category_id}
