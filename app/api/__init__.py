from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, usuarios, tipos_usuario, errors, estados, cidades, \
    bairros, enderecos, funcionarios, clientes, fornecedores, tipos_quantidade, \
    produtos, equipamentos, compras, tipos_servico, servicos, agendas