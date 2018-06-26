import logging
import requests
import datetime
import lib.response as response

from models.question import Question
from mongoengine.queryset.visitor import Q
from config import MAX_NUMBER_OF_DIFFICULTY, DIFFICULTY_MAP, SLACK_WEBHOOK_URL, BUFFER_DURATION

log = logging.getLogger()
log.setLevel(logging.DEBUG)


def main(event, context):
    questions = collect_questions()
    if questions:
        message_dict = frame_message(questions)
        if message_dict["attachments"]:
            r = requests.post(url=SLACK_WEBHOOK_URL, json=message_dict)
            if r.text == "ok":
                log.debug("## QoTW Posted")
                for question in questions:
                    question.update_timestamp()
                log.debug("## QoTW posted on {}".format(datetime.date.today()))
                return response.success({"status": "true"})
            log.error("## QotW Error Occurred")
            return response.failure({"status": "false"})
    else:
        log.error("## QotW Error Occurred")
        return response.failure({"status": "false"})


def collect_questions():
    questions = []
    older_than = datetime.datetime.utcnow() - datetime.timedelta(days=BUFFER_DURATION)
    for qt_id in range(1, MAX_NUMBER_OF_DIFFICULTY + 1):
        question = Question.objects(
            Q(question_type=qt_id) &
            Q(modified_at__lte=older_than)
        ).order_by('modified_at').first()
        if question:
            questions.append(question)
    return questions


def frame_message(questions):
    message_dict = {}
    current_date = datetime.date.today().__str__()
    message_dict["text"] = "Some more food for the brains :zombie-gif:. Here are the Questions of the Week for *{}*!"\
        .format(current_date)
    message_dict["attachments"] = []
    for index, question in enumerate(questions):
        if question:
            question_dict = {}
            question_dict["fallback"] = "{} Questions".format(DIFFICULTY_MAP.get(str(index+1)).get("name"))
            question_dict["color"] = DIFFICULTY_MAP.get(str(index+1)).get("color")
            question_dict["title"] = "{} Question".format(DIFFICULTY_MAP.get(str(index+1)).get("name"))
            question_dict["text"] = question.question_text
            fields_list = []
            if question.sample_input:
                sample_input = {}
                sample_input["title"] = "Sample Input"
                sample_input["value"] = "```"+question.sample_input+"```"
                sample_input["short"] = False
                fields_list.append(sample_input)
            if question.sample_output:
                sample_output = {}
                sample_output["title"] = "Sample Output"
                sample_output["value"] = "```"+question.sample_output+"```"
                sample_output["short"] = False
                fields_list.append(sample_output)
            if question.explanation:
                explanation = {}
                explanation["title"] = "Explanation"
                explanation["value"] = "```"+question.explanation+"```"
                explanation["short"] = False
                fields_list.append(explanation)
            if fields_list:
                question_dict["fields"] = fields_list
            message_dict["attachments"].append(question_dict)
    return message_dict
