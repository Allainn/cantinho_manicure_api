from flask import jsonify, request, url_for, current_app, abort
from .. import db
from ..models import Tipo_Usuario, Permissao
from . import api
from .errors import forbidden
from sqlalchemy.exc import IntegrityError
#from .decorators import permission_required

@api.route('/tipos_usuario/', methods=['POST'])
#@permission_required(Permissao.ADMIN)
def new_tipo_usuario():
    tipo_usuario = Tipo_Usuario.from_json(request.json)
    try:
        db.session.add(tipo_usuario)
        db.session.commit()
    except IntegrityError as err:
        print(err)
        abort(400, description="Bad Resquest")
    return jsonify(tipo_usuario.to_json()), 201, \
        {'Location':url_for('api.get_tipo_usuario', id=tipo_usuario.id)}

#@auth.login_required
@api.route('/tipos_usuario/')
def get_tipos_usuario():
    tipos_usuario = Tipo_Usuario.query.all()
    return jsonify({'tipos_usuario': [tipo_usuario.to_json() for tipo_usuario in tipos_usuario]})

@api.route('/tipos_usuario/<int:id>')
def get_tipo_usuario(id):
    tipo_usuario = Tipo_Usuario.query.get_or_404(id)
    return jsonify(tipo_usuario.to_json())