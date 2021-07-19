import sys
import json

def my_func(string):
    print('hello from lambda')
    print(sys.version)
    return string.upper()

def lambda_handler(event, context):
    print(my_func("foo"))

    return { 

        'statusCode': 200,
        'headers': {},
        'body': json.dumps(event)
    }