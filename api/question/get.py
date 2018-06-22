import logging
import lib.response as response

from models.question import Question

log = logging.getLogger()
log.setLevel(logging.DEBUG)


def main(event, context):
    q_id = event.get("pathParameters").get("id")
    question = get(q_id)
    if question:
        return response.success(question)
    else:
        return response.not_found({"error": "Question not found."})


def get(q_id):
    query = Question.objects(question_id=q_id)
    if query:
        question = query[0]
        return question.to_dict()
    else:
        return None
