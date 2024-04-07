from fastapi_storages.integrations.sqlalchemy import FileType
from sqlalchemy import Column
from sqlalchemy.orm import Mapped, mapped_column
from starlette.responses import FileResponse

from config import product_img_storage
from database import Base


class ImageOrm(Base):
    __tablename__ = "image"

    id: Mapped[int] = mapped_column(primary_key=True)
    path = Column(FileType(storage=product_img_storage), nullable=False)

    def to_dict(self):
        return {"id": self.id, "path": self.path}
