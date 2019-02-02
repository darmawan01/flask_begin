from app import ma
from models.user import *

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email')
