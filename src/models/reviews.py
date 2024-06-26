from datetime import datetime
from uuid import UUID
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import mapped_column, Mapped, relationship

from database import Base
from models.users import User


class ReviewOrm(Base):
    __tablename__ = "review"
    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    rating: Mapped[int]
    comment: Mapped[str]
    name: Mapped[str]
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"))
    created_at: Mapped[datetime | None] = mapped_column(
        server_default=text("TIMEZONE('utc', now())")
    )

    user: Mapped["User"] = relationship()

    product: Mapped["ProductOrm"] = relationship()

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "rating": self.rating,
            "comment": self.comment,
            "name": self.name,
            "user_id": self.user_id,
            "created_at": self.created_at,
        }
