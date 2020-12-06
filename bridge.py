import os

import quandl


class Bridge:

    def __init__(self):
        if 'QUANDL_API_KEY' in os.environ:
            quandl.ApiConfig.api_key = os.environ['QUANDL_API_KEY']

    def request(self, data):
        """

        :param data: JSON Object to feed Quandl API request
        :return: JSON object with the response from he API
        """
        try:
            rows = 1
            if 'rows' in data:
                rows = data.get('rows')
            df = quandl.get(dataset=data.get('dataset'), rows=rows)
            if df['Value'].size == 1:
                return df['Value'].get(0)
            else:
                return df['Value'].to_list()
        except Exception as e:
            raise e
