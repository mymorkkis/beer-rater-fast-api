"""create ratings table

Revision ID: fe63944d7447
Revises: 907497509bcd
Create Date: 2023-01-13 11:57:45.375623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "fe63944d7447"
down_revision = "907497509bcd"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # TODO Add unique constraint on (user_id, beer_id)
    op.create_table(
        "ratings",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id")),
        sa.Column("beer_id", sa.Integer),
        sa.Column("rating", sa.Integer),
    )


def downgrade() -> None:
    op.drop_table("ratings")
