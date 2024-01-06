"""Renaming students to scholars

Revision ID: aa768c9f9da8
Revises: 791279dd0760
Create Date: 2024-01-06 10:09:57.386143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa768c9f9da8'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table("students","scholars")


def downgrade() -> None:
    op.rename_table("scholars","students")
