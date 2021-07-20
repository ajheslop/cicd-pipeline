import sys
"""System module."""
import json


def my_func(string):
    """System module."""
    print('hello from lambda')
    print(sys.version)
    return string.upper()

"""System module."""
def lambda_handler(event, context):
    print(my_func("foo"))

    return {

        'statusCode': 200,
        'headers': {},
        'body': json.dumps(event)
    }
