import os

DIFFICULTY_MAP = {
    "1": {"name": "Beginner", "color": "#5faf8e"},
    "2": {"name": "Intermediate", "color": "#d6a33f"},
    "3": {"name": "Hard", "color": "#c43161"}
}
MAX_NUMBER_OF_DIFFICULTY = len(DIFFICULTY_MAP)

SLACK_WEB_HOOK_URL = "https://hooks.slack.com/services/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"

DATABASE = {
    "mongodb": {
        "username": os.environ.get("MONGODB_USER", "questions-bot"),
        "password": os.environ.get("MONGODB_PASSWORD", "GkwC2IZMEbSHd7po"),
        "host": "mongodb+srv://cluster1-upeac.mongodb.net/questionsdb?retryWrites=true"
    }
}
