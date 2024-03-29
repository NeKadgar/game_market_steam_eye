"""Median price null

Revision ID: 9b4286219299
Revises: 1a59ce76e17d
Create Date: 2022-02-17 14:44:52.887249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b4286219299'
down_revision = '1a59ce76e17d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dota_item_history', 'median_price',
               existing_type=sa.NUMERIC(precision=10, scale=2),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dota_item_history', 'median_price',
               existing_type=sa.NUMERIC(precision=10, scale=2),
               nullable=False)
    # ### end Alembic commands ###
