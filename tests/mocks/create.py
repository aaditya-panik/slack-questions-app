import json

event_body = {
    "question_text": "This is a question invalid",
    "question_type": 7
}
event = {
    "body": json.dumps(event_body)
}
