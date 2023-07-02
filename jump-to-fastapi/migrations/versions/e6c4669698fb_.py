"""empty message

Revision ID: e6c4669698fb
Revises: 15d058fbd061
Create Date: 2023-06-24 22:10:38.878747

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6c4669698fb'
down_revision = '15d058fbd061'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('create_date', sa.DateTime(), nullable=False))
    op.drop_column('question', 'create_time')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('create_time', sa.DATETIME(), nullable=False))
    op.drop_column('question', 'create_date')
    # ### end Alembic commands ###