"""create pitch table

Revision ID: 58fd47133fb8
Revises: 01f02eefc353
Create Date: 2019-02-26 18:04:11.443011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58fd47133fb8'
down_revision = '01f02eefc353'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.Column('pass_secure', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitch')
    # ### end Alembic commands ###
