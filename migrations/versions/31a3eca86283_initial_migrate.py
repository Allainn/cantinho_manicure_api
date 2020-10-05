"""Initial migrate

Revision ID: 31a3eca86283
Revises: 
Create Date: 2020-09-22 07:43:52.714237

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31a3eca86283'
down_revision = None
branch_labels = None
depends_on = None

def seed_data():
    tb_tipo_usuario = sa.sql.table('tipo_usuario', sa.sql.column('descricao', sa.String))
    op.bulk_insert(
        tb_tipo_usuario,
        [
            {'id': 1, 'descricao': 'Administrador'},
            {'id': 2, 'descricao': 'Cliente'},
            {'id': 3, 'descricao': 'Funcionário'},
            {'id': 4, 'descricao': 'Convidado'},
        ]
    )


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('equipamento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=64), nullable=False),
    sa.Column('tempo', sa.Integer(), nullable=False),
    sa.Column('preco_tempo', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('observacao', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('estado',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=2), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('descricao')
    )
    op.create_table('tipo_quantidade',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=64), nullable=True),
    sa.Column('sigla', sa.String(length=2), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tipo_servico',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=64), nullable=False),
    sa.Column('tempo', sa.Integer(), nullable=False),
    sa.Column('valor', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('observacao', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tipo_usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('descricao')
    )
    op.create_table('cidade',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=64), nullable=False),
    sa.Column('estado_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['estado_id'], ['estado.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('equipamento_tipo_servico',
    sa.Column('equipamento_id', sa.Integer(), nullable=False),
    sa.Column('tipo_servico_id', sa.Integer(), nullable=False),
    sa.Column('tempo', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['equipamento_id'], ['equipamento.id'], ),
    sa.ForeignKeyConstraint(['tipo_servico_id'], ['tipo_servico.id'], )
    )
    op.create_table('produto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=64), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.Column('tipo_quantidade_id', sa.Integer(), nullable=False),
    sa.Column('preco_un', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('observacao', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['tipo_quantidade_id'], ['tipo_quantidade.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('senha_hash', sa.String(length=256), nullable=False),
    sa.Column('confirmado', sa.Boolean(), nullable=False),
    sa.Column('tipo_usuario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tipo_usuario_id'], ['tipo_usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usuario_email'), 'usuario', ['email'], unique=True)
    op.create_index(op.f('ix_usuario_login'), 'usuario', ['login'], unique=True)
    op.create_table('bairro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=64), nullable=False),
    sa.Column('cidade_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cidade_id'], ['cidade.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('produto_tipo_servico',
    sa.Column('produto_id', sa.Integer(), nullable=False),
    sa.Column('tipo_servico_id', sa.Integer(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['produto_id'], ['produto.id'], ),
    sa.ForeignKeyConstraint(['tipo_servico_id'], ['tipo_servico.id'], )
    )
    op.create_table('endereco',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rua', sa.String(length=64), nullable=False),
    sa.Column('complemento', sa.String(length=64), nullable=True),
    sa.Column('bairro_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['bairro_id'], ['bairro.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=64), nullable=False),
    sa.Column('endereco_id', sa.Integer(), nullable=False),
    sa.Column('numero', sa.String(length=10), nullable=True),
    sa.Column('telefone1', sa.String(length=20), nullable=False),
    sa.Column('telefone2', sa.String(length=20), nullable=True),
    sa.Column('data_nascimento', sa.Date(), nullable=True),
    sa.Column('instagram', sa.String(length=64), nullable=True),
    sa.Column('facebook', sa.String(length=64), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['endereco_id'], ['endereco.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fornecedor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('endereco_id', sa.Integer(), nullable=False),
    sa.Column('numero', sa.String(length=10), nullable=True),
    sa.Column('telefone1', sa.String(length=20), nullable=False),
    sa.Column('telefone2', sa.String(length=20), nullable=True),
    sa.Column('data_nascimento', sa.Date(), nullable=True),
    sa.Column('site', sa.String(length=64), nullable=True),
    sa.Column('instagram', sa.String(length=64), nullable=True),
    sa.Column('facebook', sa.String(length=64), nullable=True),
    sa.Column('observacao', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['endereco_id'], ['endereco.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('funcionario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=64), nullable=False),
    sa.Column('telefone1', sa.String(length=20), nullable=True),
    sa.Column('telefone2', sa.String(length=20), nullable=True),
    sa.Column('data_nascimento', sa.Date(), nullable=True),
    sa.Column('endereco_id', sa.Integer(), nullable=False),
    sa.Column('numero', sa.String(length=10), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['endereco_id'], ['endereco.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('compra',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fornecedor_id', sa.Integer(), nullable=False),
    sa.Column('valor', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('data', sa.Date(), nullable=False),
    sa.Column('observacao', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['fornecedor_id'], ['fornecedor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('servico',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cliente_id', sa.Integer(), nullable=False),
    sa.Column('valor', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('tempo', sa.Integer(), nullable=False),
    sa.Column('observacao', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['cliente_id'], ['cliente.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('agenda',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cliente_id', sa.Integer(), nullable=False),
    sa.Column('servico_id', sa.Integer(), nullable=False),
    sa.Column('data', sa.DateTime(), nullable=False),
    sa.Column('observacao', sa.String(length=256), nullable=True),
    sa.ForeignKeyConstraint(['cliente_id'], ['cliente.id'], ),
    sa.ForeignKeyConstraint(['servico_id'], ['servico.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('equipamento_compra',
    sa.Column('equipamento_id', sa.Integer(), nullable=False),
    sa.Column('compra_id', sa.Integer(), nullable=False),
    sa.Column('valor', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['compra_id'], ['compra.id'], ),
    sa.ForeignKeyConstraint(['equipamento_id'], ['equipamento.id'], )
    )
    op.create_table('equipamento_servico',
    sa.Column('equipamento_id', sa.Integer(), nullable=False),
    sa.Column('servico_id', sa.Integer(), nullable=False),
    sa.Column('tempo', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['equipamento_id'], ['equipamento.id'], ),
    sa.ForeignKeyConstraint(['servico_id'], ['servico.id'], )
    )
    op.create_table('produto_compra',
    sa.Column('produto_id', sa.Integer(), nullable=False),
    sa.Column('compra_id', sa.Integer(), nullable=False),
    sa.Column('valor', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['compra_id'], ['compra.id'], ),
    sa.ForeignKeyConstraint(['produto_id'], ['produto.id'], )
    )
    op.create_table('produto_servico',
    sa.Column('produto_id', sa.Integer(), nullable=False),
    sa.Column('servico_id', sa.Integer(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['produto_id'], ['produto.id'], ),
    sa.ForeignKeyConstraint(['servico_id'], ['servico.id'], )
    )
    op.create_table('tipo_servico_servico',
    sa.Column('tipo_servico_id', sa.Integer(), nullable=False),
    sa.Column('servico_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['servico_id'], ['servico.id'], ),
    sa.ForeignKeyConstraint(['tipo_servico_id'], ['tipo_servico.id'], )
    )

    seed_data()
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tipo_servico_servico')
    op.drop_table('produto_servico')
    op.drop_table('produto_compra')
    op.drop_table('equipamento_servico')
    op.drop_table('equipamento_compra')
    op.drop_table('agenda')
    op.drop_table('servico')
    op.drop_table('compra')
    op.drop_table('funcionario')
    op.drop_table('fornecedor')
    op.drop_table('cliente')
    op.drop_table('endereco')
    op.drop_table('produto_tipo_servico')
    op.drop_table('bairro')
    op.drop_index(op.f('ix_usuario_login'), table_name='usuario')
    op.drop_index(op.f('ix_usuario_email'), table_name='usuario')
    op.drop_table('usuario')
    op.drop_table('produto')
    op.drop_table('equipamento_tipo_servico')
    op.drop_table('cidade')
    op.drop_table('tipo_usuario')
    op.drop_table('tipo_servico')
    op.drop_table('tipo_quantidade')
    op.drop_table('estado')
    op.drop_table('equipamento')
    # ### end Alembic commands ###
