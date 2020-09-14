from flask import Flask
from api import student_api
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(student_api.student)

    return app

