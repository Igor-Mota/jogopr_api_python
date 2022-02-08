from ..models import activity
from ..helpers.serializer import serializer
from ..helpers.skeletons import activity_skeleton
import re
import uuid


def create(data):
    try:
        code = uuid.uuid4().hex
        result = re.search('(.{8}$)', code)

        activity_create = activity.create_activity(data, result.groups(1))
        response = serializer.serialize(
            activity_skeleton.activity_skeleton(), activity_create[0])
        response['headers'] = data['headers']
        return response
    except:
        return {'message': 'erro'}


def login(body):
    try:
        response = activity.get_a_activity_from_code(body['code'])
        return {'activity': serializer.serialize(activity_skeleton.activity_skeleton(), response[0])}
    except:
        return 'not found'
