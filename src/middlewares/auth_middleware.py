from time import sleep
import jwt
import datetime
import asyncio


def create(user):
    if isinstance(user, str):
        return 0
    user_control = user[0]
    payload = {
        "id": user_control[0],
        "user": user_control[2],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
    }

    token = jwt.encode(payload, 'miranha', algorithm='HS256')
    return token


def authorization(token):

    if token.find('Bearer') == -1:
        return 'token mal formated'
    else:
        token = token.replace('Bearer ', '')

        def return__jwt():
            carga = jwt.decode(token, 'miranha', algorithms=['HS256'])
            data = []
            data.append(carga.get('id'))
            data.append(carga.get('user'))
            return data
    return return__jwt()
