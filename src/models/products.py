from datetime import datetime
from typing import Optional, List


from fastapi_storages.integrations.sqlalchemy import FileType
from sqlalchemy import text, Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config import category_img_storage, product_img_storage
from database import Base


class CategoryOrm(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    image = Column(FileType(storage=category_img_storage))

    products: Mapped[List["ProductOrm"]] = relationship()

    def __str__(self):
        return f"{self.name}"


class ProductOrm(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    image = Column(FileType(storage=product_img_storage))
    category_id = Column(Integer, ForeignKey("category.id", ondelete="SET NULL"))
    price: Mapped[float]
    stock: Mapped[int]
    created_at: Mapped[datetime | None] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )
    updated_at: Mapped[datetime | None] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.now
    )
    rating: Mapped[Optional[int]] = mapped_column(server_default=text("0"))
    rating_count: Mapped[Optional[int]] = mapped_column(server_default=text("0"))

    category: Mapped["CategoryOrm"] = relationship()

    def __str__(self):
        return f"{self.name}"
