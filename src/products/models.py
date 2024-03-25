import enum
from datetime import datetime
from typing import Optional

from fastapi_storages import FileSystemStorage
from fastapi_storages.integrations.sqlalchemy import FileType
from sqlalchemy import text, Column
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

img_storage = FileSystemStorage(path=r"static\images")

class Category(enum.Enum):
    uleiuri_esentiale = "Uleiuri Esentiale"
    sapunuri = "Sapunuri"
    creme = "Creme"
    parfumuri = "Parfumuri"


class ProductOrm(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    image = Column(FileType(storage=img_storage))
    category: Mapped[Category]
    price: Mapped[float]
    stock: Mapped[int]
    created_at: Mapped[datetime | None] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    updated_at: Mapped[datetime | None] = mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.now
    )
    rating: Mapped[Optional[float]] = mapped_column(server_default=text("0"))
    rating_count: Mapped[Optional[int]] = mapped_column(server_default=text("0"))

