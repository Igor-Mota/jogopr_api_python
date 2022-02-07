from dataclasses import replace
import json
from ..models.teachers_model import create_new_teacher, get_all_teachers

def register(body):
    create_new_teacher(body)
    return body
def teachers_list():
    return get_all_teachers