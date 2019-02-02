from flask import Blueprint, jsonify
from models.user import *
from .serialize import *

api = Blueprint('user', __name__)

@api.route('/')
def user_all():
    data = User.query.all()
    schema = UserSchema(many=True)
    hasil = schema.dump(data)

    return jsonify({"data": hasil})