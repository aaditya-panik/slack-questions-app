from mongoengine import *
from datetime import datetime, timedelta
import uuid
from config import DATABASE

connect(host=DATABASE["mongodb"]["host"],
        username=DATABASE["mongodb"]["username"],
        password=DATABASE["mongodb"]["password"])


class Question(Document):
    question_id = UUIDField(required=True, unique=True, default=uuid.uuid4())
    question_text = StringField(required=True)
    sample_input = StringField(required=False)
    sample_output = StringField(required=False)
    explanation = StringField(required=False)
    question_type = IntField(required=True)
    created_at = DateTimeField(required=True, default=datetime.utcnow())
    modified_at = DateTimeField(required=True, default=datetime.utcnow())

    def update_timestamp(self):
        self.modified_at = datetime.utcnow()
        self.save()

    def is_valid(self):
        return (self.modified_at - datetime.utcnow()) > timedelta(days=30)
