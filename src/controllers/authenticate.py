from ..models.teachers_model import create_new_teacher, get_all_teachers
from ..utils import hash_str


def register(body):

    name = body['name']
    password = body['password']

    if len(name) < 3:
        return 'name is very small'
    if len(password) < 6:
        return 'password is very small'

    name = name.lower()
    password = hash_str.hash_str(password)

    return create_new_teacher(name, password)


def teachers_list():
    return get_all_teachers
