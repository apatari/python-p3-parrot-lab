"""added Student

Revision ID: 9f4f33036f11
Revises: 8dc2541d5327
Create Date: 2023-10-04 16:08:36.852647

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f4f33036f11'
down_revision: Union[str, None] = '8dc2541d5327'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
