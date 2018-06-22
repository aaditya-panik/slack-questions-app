from mongoengine import *
from collections import OrderedDict
from datetime import datetime, timedelta
from config import DATABASE

connect(host=DATABASE["mongodb"]["host"],
        username=DATABASE["mongodb"]["username"],
        password=DATABASE["mongodb"]["password"])


class Question(Document):
    question_id = StringField(required=True, primary_key=True)
    question_text = StringField(required=True)
    sample_input = StringField()
    sample_output = StringField()
    explanation = StringField()
    question_type = IntField(required=True)
    created_at = DateTimeField(required=True, default=datetime.utcnow())
    modified_at = DateTimeField(required=True, default=datetime.utcnow())

    def update_timestamp(self):
        self.modified_at = datetime.utcnow()
        self.save()

    def is_valid(self):
        return (self.modified_at - datetime.utcnow()) > timedelta(days=30)

    def to_dict(self):
        dict = OrderedDict()
        dict["question_id"] = self.question_id
        dict["question_text"] = self.question_text
        if self.sample_input:
            dict["sample_input"] = self.sample_input
        if self.sample_output:
            dict["sample_output"] = self.sample_output
        if self.explanation:
            dict["explanation"] = self.explanation
        dict["question_type"] = self.question_type
        dict["created_at"] = self.created_at.__str__()
        dict["modified_at"] = self.modified_at.__str__()
        return dict
