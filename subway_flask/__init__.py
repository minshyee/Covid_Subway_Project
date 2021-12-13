import os
from flask import Flask
from flask import Blueprint, render_template, request


def create_app(config):

    # app name = subway_flask
    app = Flask(__name__)

    from subway_flask.views.main_views import main_bp
    # from project.subway_flask.user_views import user_bp

    app.register_blueprint(main_bp)
    # app.register_blueprint(user_bp, url_prefix='/api')


    return app


if __name__ == "__main__":
    app.debug=True
    app.run()
