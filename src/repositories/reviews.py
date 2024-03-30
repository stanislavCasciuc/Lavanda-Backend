from models.reviews import ReviewOrm
from utils.repository import SQLAlchemyRepository


class ReviewsRepository(SQLAlchemyRepository):
    model = ReviewOrm
