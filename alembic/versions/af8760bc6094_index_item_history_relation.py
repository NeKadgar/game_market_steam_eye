"""Index item history relation

Revision ID: af8760bc6094
Revises: 3fcb772c7bde
Create Date: 2022-02-23 14:59:54.929078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af8760bc6094'
down_revision = '3fcb772c7bde'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_dota_item_history_item_id'), 'dota_item_history', ['item_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dota_item_history_item_id'), table_name='dota_item_history')
    # ### end Alembic commands ###