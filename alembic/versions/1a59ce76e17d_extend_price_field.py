"""Extend price field

Revision ID: 1a59ce76e17d
Revises: b1e5201a77ea
Create Date: 2022-02-17 12:02:24.038052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a59ce76e17d'
down_revision = 'b1e5201a77ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("ALTER Table dota_item_history ALTER price SET DATA TYPE NUMERIC(10,2);")
    op.execute("ALTER Table dota_item_history ALTER median_price SET DATA TYPE NUMERIC(10,2);")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("ALTER Table dota_item_history ALTER price SET DATA TYPE NUMERIC(6,2);")
    op.execute("ALTER Table dota_item_history ALTER median_price SET DATA TYPE NUMERIC(6,2);")
    # ### end Alembic commands ###
