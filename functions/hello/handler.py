import json
import os


def hello(event, context):
    body = {
        "message": "Hello lambda",
        "input": event,
        "secret":  os.getenv('SOME_VAR', 'nada')
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }


    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """