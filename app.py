from flask import Flask, jsonify, request

from adapter import Adapter

app = Flask(__name__)


@app.route('/', methods=['POST'])
def call_adapter():
    data = request.get_json()
    if data == '':
        data = {}
    adapter = Adapter(data)
    return jsonify(adapter.result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')
