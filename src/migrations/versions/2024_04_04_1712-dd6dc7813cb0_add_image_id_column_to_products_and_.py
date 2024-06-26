"""Add image_id column to products and categories

Revision ID: dd6dc7813cb0
Revises: b387f135f97b
Create Date: 2024-04-04 17:12:25.361483

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "dd6dc7813cb0"
down_revision: Union[str, None] = "b387f135f97b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("category", sa.Column("image_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        None, "category", "image", ["image_id"], ["id"], ondelete="SET NULL"
    )
    op.add_column("product", sa.Column("image_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        None, "product", "image", ["image_id"], ["id"], ondelete="SET NULL"
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "product", type_="foreignkey")
    op.drop_column("product", "image_id")
    op.drop_constraint(None, "category", type_="foreignkey")
    op.drop_column("category", "image_id")
    # ### end Alembic commands ###
