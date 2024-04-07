from datetime import datetime
from typing import Optional, List

from sqlalchemy import text, Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from models.images import ImageOrm


class CategoryOrm(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    image_id = Column(Integer, ForeignKey("image.id", ondelete="SET NULL"))

    products: Mapped[List["ProductOrm"]] = relationship(back_populates="category")

    image: Mapped[ImageOrm] = relationship()

    def __str__(self):
        return f"{self.name}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image.to_dict(),
            "products_count": len(self.products) if self.products else 0,
        }

    def to_read(self):
        return {
            "id": self.id,
            "name": self.name,
        }


class ProductOrm(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    category_id = Column(Integer, ForeignKey("category.id", ondelete="SET NULL"))
    image_id = Column(Integer, ForeignKey("image.id", ondelete="SET NULL"))
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

    category: Mapped["CategoryOrm"] = relationship(back_populates="products")

    image: Mapped[ImageOrm] = relationship()

    def __str__(self):
        return f"{self.name}"

    def to_read(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "image": self.image.to_dict(),
            "category": self.category.to_read(),
            "price": self.price,
            "stock": self.stock,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "rating": self.rating,
            "rating_count": self.rating_count,
        }
