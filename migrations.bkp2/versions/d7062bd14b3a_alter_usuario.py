"""alter usuario

Revision ID: d7062bd14b3a
Revises: b40ed89b35cf
Create Date: 2020-09-17 18:27:00.080482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7062bd14b3a'
down_revision = 'b40ed89b35cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'confirmed')
    # ### end Alembic commands ###
