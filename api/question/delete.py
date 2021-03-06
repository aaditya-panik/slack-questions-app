import logging
import lib.response as response

from models.question import Question

log = logging.getLogger()
log.setLevel(logging.DEBUG)


def main(event, context):
    q_id = event.get("pathParameters").get("id")
    (is_deleted, deletion_errors) = delete(q_id)
    if is_deleted:
        return response.no_content()
    else:
        return response.failure({"error": deletion_errors})


def delete(q_id):
    question = Question.objects(question_id=q_id).first()
    q_id = question.question_id
    if question:
        question.delete()
        log.debug("## Question Deleted : ID {}".format(q_id))
        return True, None
    else:
        return False, "Question not found"
