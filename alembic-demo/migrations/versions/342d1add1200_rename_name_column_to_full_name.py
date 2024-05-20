"""Rename name column to full_name

Revision ID: 342d1add1200
Revises: af4ce0d6926d
Create Date: 2024-05-20 20:22:04.625697

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '342d1add1200'
down_revision: Union[str, None] = 'af4ce0d6926d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column("users","name",new_column_name="full_name")


def downgrade() -> None:
    op.alter_column("users","full_name",new_column_name="name")
