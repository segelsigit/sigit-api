import json
from flask import jsonify, request, Blueprint
from core.models import SigitStudent, SigitCourse

course = SigitCourse()

student = Blueprint('student_pave', __name__,
                    template_folder='templates')


@student.route('/student', methods=['GET'])
def quarantine():
    return jsonify(course.get_quarantine_students()), 200


@student.route('/student/<student_name>')
def fetch_student(student_name):
    try:
        sigit_student = course.get_student(student_name)
        return jsonify(sigit_student.__dict__), 200
    except Exception:
        return "There is no such student", 404


@student.route('/student', methods=['POST'])
def add_student_to_quarantine():
    details = json.loads(request.data)
    sigit_student = SigitStudent(name=details["name"], quarantine_days_left=details["quarantine_days_left"],
                                 has_symptoms=details["has_symptoms"])
    try:
        course.add_student_to_quarantine(sigit_student)
    except Exception:
        return "Student already in quarantine", 409
    return jsonify(sigit_student.__dict__), 200


@student.route('/student/<student_name>', methods=['DELETE'])
def remove_student_from_quatantine(student_name):
    course.remove_student_from_quarantine(student_name)
    return student_name, 200


@student.route('/student', methods=['PUT'])
def update_student():
    details = json.loads(request.data)
    try:
        course.get_student(details["name"])
        course.update_students_details(details=details)
        return details, 200
    except Exception:
        return "There is no such student", 404
