"""remove salary column

Revision ID: 576d72a624eb
Revises: 6c731184ea28
Create Date: 2023-06-04 15:18:55.300957

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '576d72a624eb'
down_revision = '6c731184ea28'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('authors', 'salary')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('authors', sa.Column('salary', mysql.FLOAT(), nullable=True))
    # ### end Alembic commands ###
