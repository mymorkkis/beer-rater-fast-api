"""create users table

Revision ID: 907497509bcd
Revises:
Create Date: 2023-01-13 11:51:18.227074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "907497509bcd"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # TODO add unique contstraint on email and hash password
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String),
        sa.Column("password", sa.String),
    )


def downgrade() -> None:
    op.drop_table("users")
