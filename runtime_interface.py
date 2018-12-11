"""
A Custom Runtime Interface for running Python code with Pypy on AWS Lambda
"""
import sys
import json
import requests
import handler

__author__ = "Ulrich Scheller"
__email__ = "mail@ulrich-scheller.de"
__website__ = "www.ulrich-scheller.de"
__status__ = "Prototype"


class RuntimeInterface(object):
    def __init__(self, api):
        url_scheme = "http://{}/2018-06-01/runtime/invocation".format(api)
        self.fetch_url = url_scheme + "/next"
        self.response_url = url_scheme + "/{}/response"
        self.error_url = url_scheme + "/{}/error"

    def fetch_next_request(self):
        response = requests.get(self.fetch_url)
        return response.headers["Lambda-Runtime-Aws-Request-Id"], response

    def post_response(self, request_id, response):
        url = self.response_url.format(request_id)
        requests.post(url, data=json.dumps(response))

    def post_error(self, request_id, error):
        url = self.error_url.format(request_id)
        print(e)
        error_response = {
            "errorMessage" : error.message,
            "errorType" : type(e)
        }
        requests.post(url, data=json.dumps(error_response))

    def process_event(self):
        request_id, r = self.fetch_next_request()
        try:
            response = handler.hello(r.json(), None)
        except Exception as e:
            self.post_error(request_id, e)
        self.post_response(request_id, response)

    def run_loop(self):
        while True:
            self.process_event()


if __name__ == "__main__":
    AWS_LAMBDA_RUNTIME_API = sys.argv[1]
    runtime = RuntimeInterface(AWS_LAMBDA_RUNTIME_API)
    runtime.run_loop()
