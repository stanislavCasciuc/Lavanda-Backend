from repositories.products import ProductsRepository
from repositories.reviews import ReviewsRepository
from sevices.reviews import ReviewsService
from sevices.products import ProductsService


def get_reviews_service():
    return ReviewsService(ReviewsRepository)


def get_products_service():
    return ProductsService(ProductsRepository)
