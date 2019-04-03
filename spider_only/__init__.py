# coding: utf8
import logging

from flask import Flask
from flask_compress import Compress


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    # http://flask.pocoo.org/docs/1.0/config/#configuring-from-files
    app.config.from_object('scrapydweb.default_settings')

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import index, api, log, logs, schedule, spiders

    app.register_blueprint(index.bp)
    app.register_blueprint(api.bp)
    app.register_blueprint(log.bp)
    app.register_blueprint(logs.bp)
    app.register_blueprint(schedule.bp)
    app.register_blueprint(spiders.bp)

    compress = Compress()
    compress.init_app(app)

    app.jinja_env.variable_start_string = '{{ '
    app.jinja_env.variable_end_string = ' }}'

    app.logger.setLevel(logging.DEBUG)

    return app
