from app import ma
from models.user import *

class UserSchema(ma.ModelSchema):
    class Meta:
        model: User