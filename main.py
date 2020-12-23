from flask import Blueprint, jsonify, request
from schema import Schema, And, Optional

from bridge import Bridge

api = Blueprint('api', __name__)


def index(request):
    data = request.get_json()
    if data == '':
        data = {}
    adapter = Adapter(data)
    return jsonify(adapter.result), adapter.result['statusCode']


@api.route('/', methods=['POST'])
def call_adapter():
    data = request.get_json()
    if data == '':
        data = {}
    adapter = Adapter(data)
    return jsonify(adapter.result), adapter.result['statusCode']


class Adapter:

    def __init__(self, input):
        self.id = input.get('id', '1')
        self.request_data = input.get('data')
        if self.validate_request_data():
            self.bridge = Bridge()
            self.create_request()
        else:
            self.result_error('Invalid data provided')

    def validate_request_data(self):
        """ Validates the incoming data against a pre-defined schema

        :return: True if the data provided is a valid JSON containing a
        dataset key, False otherwise
        """
        schema = Schema({'dataset': str,
                         Optional('rows'): And(int, lambda n: 0 < n)},
                        ignore_extra_keys=True)
        return schema.is_valid(self.request_data)

    def create_request(self):
        try:
            data = self.request_data
            data['result'] = self.bridge.request(self.request_data)
            self.result_success(data)
        except Exception as e:
            self.result_error(e)

    def result_success(self, data):
        self.result = {
            'jobRunID': self.id,
            'data': data,
            'statusCode': 200,
        }

    def result_error(self, error):
        self.result = {
            'jobRunID': self.id,
            'status': 'errored',
            'error': f'There was an error: {error}',
            'statusCode': 500,
        }

    def __repr__(self):
        return f'Adapter({self.id!r}, {self.request_data!r})'
