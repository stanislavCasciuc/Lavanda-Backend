import uuid
from uuid import UUID

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, String

from database import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    full_name = Column(String, nullable=False)