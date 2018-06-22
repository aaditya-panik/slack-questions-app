from tests.mocks.create import event
from api.question.create import main

context = None


def run():
    result = main(event, context)
    print(result)


if __name__ == '__main__':
    run()
