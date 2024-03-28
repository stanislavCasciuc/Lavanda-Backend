from api.reviews.models import ReviewOrm
from utils.repository import SQLAlchemyRepository


class ReviewsRepository(SQLAlchemyRepository):
    model = ReviewOrm
