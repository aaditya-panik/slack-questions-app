import json


def failure(body):
    return build_response(500, body)


def not_found(body):
    return build_response(404, body)


def bad_request(body):
    return build_response(400, body)


def no_content():
    return build_response(204, None)


def success(body):
    return build_response(200, body)


def build_response(status_code, body):
    return {
        "statusCode": status_code,
        "body": json.dumps(body)
    }
