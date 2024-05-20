"""Add age column to users

Revision ID: af4ce0d6926d
Revises: a96ccb7fdc74
Create Date: 2024-05-20 20:16:32.249962

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af4ce0d6926d'
down_revision: Union[str, None] = 'a96ccb7fdc74'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users",sa.Column("age", sa.Integer()))

def downgrade() -> None:
    op.drop_column("users", "age")
