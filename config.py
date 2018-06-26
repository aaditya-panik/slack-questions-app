import os

DIFFICULTY_MAP = {
    "1": {"name": "Beginner", "color": "#5faf8e"},
    "2": {"name": "Intermediate", "color": "#d6a33f"},
    "3": {"name": "Hard", "color": "#c43161"}
}
MAX_NUMBER_OF_DIFFICULTY = len(DIFFICULTY_MAP)
BUFFER_DURATION = int(os.environ.get("BUFFER_DURATION", 30))

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services" + os.environ.get("SLACK_WEBHOOK_URL", "/")

DATABASE = {
    "mongodb": {
        "username": os.environ.get("MONGODB_USER"),
        "password": os.environ.get("MONGODB_PASSWORD"),
        "host": os.environ.get("MONGODB_CONN_STRING")
    }
}
