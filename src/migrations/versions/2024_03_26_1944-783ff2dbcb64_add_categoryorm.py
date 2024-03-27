"""Add CategoryOrm

Revision ID: 783ff2dbcb64
Revises: 
Create Date: 2024-03-26 19:44:45.188903

"""
from typing import Sequence, Union

import fastapi_storages
import fastapi_users_db_sqlalchemy
from alembic import op
import sqlalchemy as sa

from api.products.models import category_img_storage, product_img_storage

# revision identifiers, used by Alembic.
revision: str = '783ff2dbcb64'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('image', fastapi_storages.integrations.sqlalchemy.FileType(category_img_storage), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('user',
                    sa.Column('full_name', sa.String(), nullable=False),
                    sa.Column('id', fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False),
                    sa.Column('email', sa.String(length=320), nullable=False),
                    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
                    sa.Column('is_active', sa.Boolean(), nullable=False),
                    sa.Column('is_superuser', sa.Boolean(), nullable=False),
                    sa.Column('is_verified', sa.Boolean(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('product',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('description', sa.String(), nullable=False),
                    sa.Column('price', sa.Float(), nullable=False),
                    sa.Column('stock', sa.Integer(), nullable=False),
                    sa.Column('image', fastapi_storages.integrations.sqlalchemy.FileType(product_img_storage), nullable=True),
                    sa.Column('category_id', sa.Integer(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"),
                              nullable=True),
                    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"),
                              nullable=True),
                    sa.Column('rating', sa.Float(), server_default=sa.text('0'), nullable=True),
                    sa.Column('rating_count', sa.Integer(), server_default=sa.text('0'), nullable=True),
                    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ondelete='SET NULL'),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('review',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('product_id', sa.Integer(), nullable=False),
                    sa.Column('rating', sa.Integer(), nullable=False),
                    sa.Column('comment', sa.String(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('user_id', fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"),
                              nullable=True),
                    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    op.drop_table('product')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('category')
    # ### end Alembic commands ###