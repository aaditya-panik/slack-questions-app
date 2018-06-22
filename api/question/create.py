import shortuuid
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
    (is_valid, validation_error) = validate(post_data)
    if is_valid:
        return response.success(create(post_data))
    else:
        return response.bad_request({"error": validation_error})


def create(post_data):
    question_text = post_data.get("question_text")
    sample_input = post_data.get("sample_input")
    sample_output = post_data.get("sample_output")
    explanation = post_data.get("explanation")
    question_type = post_data.get("question_type")
    q = Question(question_id=shortuuid.uuid(),
                 question_text=question_text,
                 sample_input=sample_input,
                 sample_output=sample_output,
                 explanation=explanation,
                 question_type=question_type)
    try:
        obj = q.save()
        return_dict = obj.to_dict()
        return return_dict
    except Exception as e:
        return response.failure({"status": "Failure occurred.",
                                 "error": str(e)})


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
