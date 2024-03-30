from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, String

from database import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    full_name = Column(String, nullable=False)

    def __str__(self):
        return f"{self.full_name}"
