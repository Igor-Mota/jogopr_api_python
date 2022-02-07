from datetime import datetime
from lib2to3.pgen2 import token
import jwt
import datetime


def create(user):
    if isinstance(user, str):
        return 0
    user_control = user[0]
    payload = {
        "id": user_control[0],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
    }

    token = jwt.encode(payload, 'miranha')
    return token


def authorization(user):
    return 0
