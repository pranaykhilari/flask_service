"""empty message

Revision ID: 6643cdbf0130
Revises: 2f96f8d8dc96
Create Date: 2019-09-12 14:27:24.033147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6643cdbf0130'
down_revision = '2f96f8d8dc96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Employee', sa.Column('phone_num', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Employee', 'phone_num')
    # ### end Alembic commands ###