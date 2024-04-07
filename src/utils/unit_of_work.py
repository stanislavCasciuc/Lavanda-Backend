from abc import ABC, abstractmethod
from typing import Type

from database import async_session_maker
from repositories.categories import CategoriesRepository
from repositories.images import ImagesRepository
from repositories.products import ProductsRepository
from repositories.reviews import ReviewsRepository


class IUnitOfWork(ABC):
    reviews: Type[ReviewsRepository]
    products: Type[ProductsRepository]
    images: Type[ImagesRepository]
    categories: Type[CategoriesRepository]

    @abstractmethod
    def __init__(self): ...

    @abstractmethod
    async def __aenter__(self): ...

    @abstractmethod
    async def __aexit__(self, *args): ...

    @abstractmethod
    async def commit(self): ...

    @abstractmethod
    async def rollback(self): ...


class UnitOfWork:
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        self.reviews = ReviewsRepository(self.session)
        self.products = ProductsRepository(self.session)
        self.images = ImagesRepository(self.session)
        self.categories = CategoriesRepository(self.session)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
