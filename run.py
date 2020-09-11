import json

from flask import Flask, jsonify
from flask import request
from flask_swagger import swagger
from factory import create_app
from sigit_course import SigitCourse
from sigit_student import SigitStudent

app = create_app()

sigit_course = SigitCourse()


@app.route('/spec', methods=['GET'])
def home():
    swag = swagger(app)
    swag['info']['title'] = "Sigit Quarantine"
    return jsonify(swag)


@app.route('/quarantine', methods=['GET'])
def quarantine():
    """
    Get all Students in quarantine
    :return:
    """
    return jsonify(sigit_course.get_quarantine_students()), 200


@app.route('/quarantine', methods=['POST'])
def add_student_to_quarantine():
    details = json.loads(request.data)
    student = SigitStudent(name=details["name"], quarantine_days_left=details["quarantine_days_left"],
                           has_symptoms=details["has_symptoms"])
    try:
        sigit_course.add_student_to_quarantine(student)
    except Exception:
        return "Student already in quarantine", 409
    return jsonify(student.__dict__), 200


@app.route('/quarantine/<student_name>', methods=['DELETE'])
def remove_student_from_quatantine(student_name):
    sigit_course.remove_student_from_quarantine(student_name)
    return student_name, 200


@app.route('/quarantine', methods=['PUT'])
def update_student():
    details = json.loads(request.data)
    sigit_course.update_students_details(details=details)
    return details, 200


if __name__ == '__main__':
    app.run()
