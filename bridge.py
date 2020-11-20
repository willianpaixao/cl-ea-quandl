import os

import quandl

if 'QUANDL_API_KEY' in os.environ:
    quandl.ApiConfig.api_key = os.environ['QUANDL_API_KEY']


class Bridge:

    def request(self, data):
        try:
            df = quandl.get(dataset=data.get('dataset'), rows=1)
            return df.iloc[0]['Value']
        except Exception as e:
            raise e
