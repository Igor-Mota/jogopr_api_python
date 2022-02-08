from ..models.teachers_model import create_new_teacher, get_a_teacher, get_all_teachers
from ..utils import hash_str, render
from ..middlewares import auth_middleware


def register(body):

    name = body['name']
    password = body['password']
    email = body['email']
    confirm_password = body['confirm_password']

    if confirm_password != password:
        return 'passwords are not the same'

    if len(name) < 3:
        return 'name is very small'
    if len(password) < 6:
        return 'password is very small'

    name = name.lower()
    password = hash_str.hash_str(password)

    teacher = create_new_teacher(name, password, email)
    return render.render__one(teacher, auth_middleware.create(teacher))


def login(body):

    email = body['email']
    password = body['password']

    teacher = get_a_teacher(email)
    try:
        compare_hashs = hash_str.compare(password, teacher[0][3])
        if compare_hashs == "password is wrong":
            return compare_hashs
        else:
            return render.render__one(teacher, auth_middleware.create(teacher))
    except:
        return 'user does not exist'


def teachers_list():
    return get_all_teachers()
