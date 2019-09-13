"""empty message

Revision ID: a3024e7f37a3
Revises: 6643cdbf0130
Create Date: 2019-09-13 11:49:53.254328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3024e7f37a3'
down_revision = '6643cdbf0130'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('email', sa.String(length=128), nullable=True))
    op.add_column('student', sa.Column('phone_num', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('student', 'phone_num')
    op.drop_column('student', 'email')
    # ### end Alembic commands ###
