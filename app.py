import logging
import os

from flask import Flask, jsonify, request

from adapter import Adapter


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        configure_app(app)
    else:
        app.config.update(test_config)

    @app.before_request
    def log_request_info():
        app.logger.debug('Headers: %s', request.headers)
        app.logger.debug('Body: %s', request.get_data())

    @app.route('/', methods=['POST'])
    def call_adapter():
        data = request.get_json()
        if data == '':
            data = {}
        adapter = Adapter(data)
        return jsonify(adapter.result), adapter.result['statusCode']

    @app.route('/healthcheck', methods=['GET'])
    def healthcheck():
        return 'OK'

    return app


def configure_app(app):
    """  Loads a different set of configurations depending on the desired environment

    :param app: Flask app instance
    """
    if app.config['ENV'] == 'production':
        app.config.from_object('config.ProductionConfig')
    if app.config['ENV'] == 'development':
        app.config.from_object('config.DevelopmentConfig')
    if app.config['ENV'] == 'testing':
        app.config.from_object('config.TestingConfig')

    if 'SECRETS_FILE' in os.environ:
        try:
            app.config.from_envvar('SECRETS_FILE')
        except SyntaxError:
            app.logger.error("Invalid secret file '{}', aborting...", os.environ['SECRETS_FILE'])
    elif 'QUANDL_API_KEY' in os.environ:
        try:
            app.config['QUANDL_API_KEY'] = os.environ['QUANDL_API_KEY']
        except SyntaxError:
            app.logger.error("Invalid Quandl API key '{}', aborting...", os.environ['QUANDL_API_KEY'])
    else:
        app.logger.error("Required Quandl API key not provided, aborting...")

    app.logger.info("Configuration loaded successfully")

    # The following libraries gives excessive logging, so fine tuning is needed
    logging.getLogger("urllib3").setLevel(logging.WARNING)


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0")
