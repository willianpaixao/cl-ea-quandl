import os

import quandl
from flask import Flask, jsonify, request

app = Flask(__name__)

if 'QUANDL_API_KEY' in os.environ:
    quandl.ApiConfig.api_key = os.environ['QUANDL_API_KEY']
else:
    app.logger.info("Quandl's API key not found")


@app.route('/', methods=['GET'])
def index():
    df = quandl.get(dataset=request.args.get('dataset'), rows=1)
    return jsonify(df.iloc[0]['Value'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')
