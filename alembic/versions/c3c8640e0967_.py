"""empty message

Revision ID: c3c8640e0967
Revises: 629b9a0d9c5a
Create Date: 2024-11-05 22:12:53.795231

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3c8640e0967'
down_revision: Union[str, None] = '629b9a0d9c5a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
