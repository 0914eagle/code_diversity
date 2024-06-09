
from collections import namedtuple

Student = namedtuple('Student', 'id marks class name')

def get_average_marks(n, columns, *data):
    students = []
    for i in range(n):
        student_data = data[i]
        students.append(Student(student_data[0], student_data[1], student_data[2], student_data[3]))
    total_marks = sum(student.marks for student in students)
    average_marks = total_marks / n
    return round(average_marks, 2)

