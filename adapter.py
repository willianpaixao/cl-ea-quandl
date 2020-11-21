from schema import Schema, And, Optional
from bridge import Bridge


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
                         Optional('rows'): And(int, lambda n: 0 < n)})
        return schema.is_valid(self.request_data)

    def create_request(self):
        try:
            self.result = self.bridge.request(self.request_data)
            self.result_success(self.request_data)
        except Exception as e:
            self.result_error(e)

    def result_success(self, data):
        self.result = {
            'jobRunID': self.id,
            'data': data,
            'result': self.result,
            'statusCode': 200,
        }

    def result_error(self, error):
        self.result = {
            'jobRunID': self.id,
            'status': 'errored',
            'error': f'There was an error: {error}',
            'statusCode': 500,
        }
