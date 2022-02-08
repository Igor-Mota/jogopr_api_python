from ..models import activity
from ..helpers.serializer import serializer
from ..helpers.skeletons import activity_skeleton


def create(data):
    try:
        activity_create = activity.create_activity(data)
        response = serializer.serialize(
            activity_skeleton.activity_skeleton(), activity_create[0])
        response['headers'] = data['headers']
        return response
    except:
        return {'message': 'erro'}
