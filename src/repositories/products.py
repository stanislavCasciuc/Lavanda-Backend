from models.products import ProductOrm
from utils.repository import SQLAlchemyRepository


class ProductsRepository(SQLAlchemyRepository):
    model = ProductOrm
