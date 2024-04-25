import json
import math
import sys


def hello(event, context):
    body = {
        "message": ("Hello from {}! Your function executed successfully!".format(sys.argv[0].split("/")[-1])),
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response


def primes(event, context):
    primes = [x for x in range(2, 200000) if [y for y in range(2, int(math.sqrt(x))) if x%y == 0] == []]
    body = {
        "message": ("Hello from {}! Your function executed successfully!".format(sys.argv[0].split("/")[-1])),
        "number of primes": str(len(primes)),
    }

    response = {
        "statusCode": 200,
        "headers": {'Content-Type': 'application/json'},
        "body": json.dumps(body)
    }

    return response
