"""Altered relationship tables

Revision ID: d3cd6f4d3fcd
Revises: 6972787fd9d7
Create Date: 2020-11-23 11:08:02.620781

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd3cd6f4d3fcd'
down_revision = '6972787fd9d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('equipamento_compra', 'valor')
    op.drop_column('equipamento_servico', 'tempo')
    op.drop_column('equipamento_tipo_servico', 'tempo')
    op.drop_column('produto_compra', 'valor')
    op.drop_column('produto_servico', 'quantidade')
    op.drop_column('produto_tipo_servico', 'quantidade')
    op.create_index(op.f('ix_tipo_usuario_default'), 'tipo_usuario', ['default'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tipo_usuario_default'), table_name='tipo_usuario')
    op.add_column('produto_tipo_servico', sa.Column('quantidade', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('produto_servico', sa.Column('quantidade', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('produto_compra', sa.Column('valor', mysql.DECIMAL(precision=10, scale=2), nullable=False))
    op.add_column('equipamento_tipo_servico', sa.Column('tempo', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('equipamento_servico', sa.Column('tempo', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.add_column('equipamento_compra', sa.Column('valor', mysql.DECIMAL(precision=10, scale=2), nullable=False))
    # ### end Alembic commands ###