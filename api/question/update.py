import logging
import json
import lib.response as response

from models.question import Question
from config import MAX_NUMBER_OF_DIFFICULTY

log = logging.getLogger()
log.setLevel(logging.DEBUG)


def main(event, context):
    post_data = event.get("body")
    post_data = json.loads(post_data)
    q_id = event.get("pathParameters").get("id")
    (is_valid, validation_error) = validate(post_data)
    if is_valid:
        return update(post_data, q_id)
    else:
        return response.bad_request({"error": validation_error})


def update(post_data, q_id):
    query = Question.objects(question_id=q_id)
    if query:
        question = query[0]
        question.question_text = post_data.get("question_text")
        question.sample_input = post_data.get("sample_input")
        question.sample_output = post_data.get("sample_output")
        question.explanation = post_data.get("explanation")
        question.question_type = post_data.get("question_type")
        try:
            question.update_timestamp()
        except Exception as e:
            return response.failure({"status": "Failure occured.",
                                     "error": str(e)})
        log.debug("## Question Updated: ID {}".format(question.question_id))
        return response.success(question.to_dict())
    else:
        return response.failure({"error": "Question not found"})


def validate(post_data):
    if not post_data:
        return False, "missing data"
    question_text = post_data.get("question_text")
    try:
        question_type = int(post_data.get("question_type"))
        if question_type > MAX_NUMBER_OF_DIFFICULTY or question_type < 1:
            return False, "question_type is invalid"
    except ValueError:
        return False, "question_type is not an integer"
    if question_text is None:
        return False, "question_text is missing"
    return True, None
