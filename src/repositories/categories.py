from models.products import CategoryOrm
from utils.repository import SQLAlchemyRepository


class CategoriesRepository(SQLAlchemyRepository):
    model = CategoryOrm
