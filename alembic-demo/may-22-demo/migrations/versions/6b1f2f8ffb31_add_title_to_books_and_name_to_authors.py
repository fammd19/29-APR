"""Add title to books and name to authors

Revision ID: 6b1f2f8ffb31
Revises: 0ccfaebcc3e5
Create Date: 2024-05-22 20:49:15.592012

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b1f2f8ffb31'
down_revision: Union[str, None] = '0ccfaebcc3e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("books",sa.Column("title", sa.String()))
    op.add_column("authors",sa.Column("name", sa.String()))


def downgrade() -> None:
    op.drop_column("books","title")
    op.drop_column("authors","name")
