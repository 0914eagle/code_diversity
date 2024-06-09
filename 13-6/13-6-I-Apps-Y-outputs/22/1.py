
from collections import namedtuple

Student = namedtuple('Student', 'id marks class name')

def get_average_marks(n, columns, *data):
    students = []
    for i in range(n):
        students.append(Student._make(data[i]))
    return sum(student.marks for student in students) / n

