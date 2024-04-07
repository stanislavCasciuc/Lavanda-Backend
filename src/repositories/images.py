from models.images import ImageOrm
from utils.repository import SQLAlchemyRepository


class ImagesRepository(SQLAlchemyRepository):
    model = ImageOrm
