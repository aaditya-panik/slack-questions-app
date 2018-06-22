import logging
import lib.response as response

from models.question import Question

log = logging.getLogger()
log.setLevel(logging.DEBUG)


def main(event, context):
    return response.success(list_questions())


def list_questions():
    query = Question.objects()
    return_list = []
    for question in query:
        return_list.append(question.to_dict())
    return return_list
