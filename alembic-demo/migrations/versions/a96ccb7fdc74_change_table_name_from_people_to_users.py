"""Change table name from people to users

Revision ID: a96ccb7fdc74
Revises: 7f60d0808a95
Create Date: 2024-05-20 20:09:55.212966

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a96ccb7fdc74'
down_revision: Union[str, None] = '7f60d0808a95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table("people", "users")


def downgrade() -> None:
    op.rename_table("users", "people")
