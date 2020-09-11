from flask import Flask
from api import student_api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(student_api.student)

    return app

