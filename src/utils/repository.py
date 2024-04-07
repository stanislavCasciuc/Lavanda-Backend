from abc import ABC, abstractmethod
from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError

    @abstractmethod
    async def update_one(self):
        raise NotImplementedError

    @abstractmethod
    async def find_one(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> int:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def find_all(self, options: list = None, order_by=None, filter=None):
        stmt = select(self.model)
        if filter is not None:
            stmt = stmt.filter_by(**filter)
        if options is not None:
            for entity in options:
                stmt = stmt.options(entity)
        if order_by is not None:
            stmt = stmt.order_by(order_by)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def find_one(self, options: list = None, filter=None):
        stmt = select(self.model).filter_by(**filter)
        if options is not None:
            for entity in options:
                stmt = stmt.options(entity)
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def update_one(self, data: dict, id: int) -> int:
        stmt = (
            update(self.model)
            .where(self.model.id == id)
            .values(**data)
            .returning(self.model.id)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one()
