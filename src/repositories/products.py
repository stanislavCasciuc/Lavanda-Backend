from api.products.models import ProductOrm
from utils.repository import SQLAlchemyRepository


class ProductsRepository(SQLAlchemyRepository):
    model = ProductOrm
