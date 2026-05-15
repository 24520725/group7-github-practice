class Student:
    def __init__(self, name, student_id, score):
        self.name = name
        self.student_id = student_id
        self.score = score
    def __str__(self):
        return f"{self.student_id} | {self.name} | {self.score}"
class StudentManager:
    def __init__(self):
        self.students = []
    def add_student(self, name, student_id, score):
        self.students.append(Student(name, student_id, score))
    def get_all(self):
        return self.students
    def search(self, keyword):
        keyword = keyword.lower()
        return [
            s for s in self.students
            if keyword in s.name.lower() or keyword in s.student_id.lower()
        ]
        def delete_student(self, student_id):
        self.students = [s for s in self.students if s.student_id != student_id]
