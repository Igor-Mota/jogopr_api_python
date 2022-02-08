from ..models import questions
from ..models import activity
from ..helpers.skeletons import question_skeleton
from ..helpers.serializer import serializer


def create(body):
    try:
        activity_id = activity.get_a_activity_from_code(body['code'])
        response = questions.create_a_question(body, activity_id[0])
        return {"main": serializer.serialize(question_skeleton.question_skeleton(), response[0])}
    except:
        return 'deu problema'
