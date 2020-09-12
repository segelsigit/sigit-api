from core.models.sigit_student import SigitStudent


class SigitCourse:

    def __init__(self):
        self.quarantine_students = []

    def add_student_to_quarantine(self, new_student: SigitStudent):
        in_list = [stud for stud in self.quarantine_students if stud.name == new_student.name]

        if in_list:
            raise Exception("Student already exists in list")
        else:
            self.quarantine_students.append(new_student)

    def remove_student_from_quarantine(self, student_name: str):
        for student in self.quarantine_students:
            if student.name == student_name:
                self.quarantine_students.remove(student)

    def get_quarantine_students(self):
        return {"students": [stud.__dict__ for stud in self.quarantine_students]}

    def update_students_details(self, details: dict):
        for student in self.quarantine_students:
            if student.name == details["name"]:
                student.quarantine_days_left = details["quarantine_days_left"]
                student.has_symptoms = details["has_symptoms"]

    def get_student(self, student_name):
        for student in self.quarantine_students:
            if student.name == student_name:
                return student
        raise Exception("No student")
