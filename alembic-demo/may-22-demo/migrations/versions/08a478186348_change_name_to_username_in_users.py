"""Change name to username in Users

Revision ID: 08a478186348
Revises: dbd228807589
Create Date: 2024-05-22 19:22:01.219699

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08a478186348'
down_revision: Union[str, None] = 'dbd228807589'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column("users","name",new_column_name="username")


def downgrade() -> None:
    op.alter_column("users","username",new_column_name="name")
