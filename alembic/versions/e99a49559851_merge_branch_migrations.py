"""Merge branch migrations

Revision ID: e99a49559851
Revises: 22bc3a930f6d, 8032ba6c25d8
Create Date: 2024-11-06 12:53:22.906430

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e99a49559851'
down_revision: Union[str, None] = ('22bc3a930f6d', '8032ba6c25d8')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
