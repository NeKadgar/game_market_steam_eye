"""First migration

Revision ID: b1e5201a77ea
Revises: 
Create Date: 2022-02-17 11:06:29.620538

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b1e5201a77ea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dota_item',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=128), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('dota_item_history',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('price', sa.Numeric(precision=6, scale=2), nullable=False),
                    sa.Column('volume', sa.Integer(), nullable=False),
                    sa.Column('median_price', sa.Numeric(precision=6, scale=2), nullable=False),
                    sa.Column('date', sa.DateTime(), nullable=True),
                    sa.Column('item_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['item_id'], ['dota_item.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dota_item_history')
    op.drop_table('dota_item')
    # ### end Alembic commands ###
