from turtle import update

from sqlalchemy import select, insert, update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload

from api.products.models import ProductOrm
from api.reviews.models import ReviewOrm


async def get_product_reviews_from_db(session, product_id: int):
    query = (
        select(ReviewOrm)
        .where(ReviewOrm.product_id == product_id)
        .options(selectinload(ReviewOrm.user))
    )
    result = await session.execute(query)
    return result.scalars().all()


async def insert_review_into_db(session, review, user):
    try:
        stmt = insert(ReviewOrm).values(
            product_id=review.product_id,
            rating=review.rating,
            comment=review.comment,
            name=review.name,
            user_id=user.id,
        )
        await session.execute(stmt)
        stmt = (
            update(ProductOrm)
            .where(ProductOrm.id == review.product_id)
            .values(
                rating=ProductOrm.rating + review.rating,
                rating_count=ProductOrm.rating_count + 1,
            )
        )
        await session.execute(stmt)
        await session.commit()
    except SQLAlchemyError as e:
        print(f"An error occurred while inserting the review into the database: {e}")
        await session.rollback()
