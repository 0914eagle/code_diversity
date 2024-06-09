
from collections import namedtuple

def solve(n, columns, *rows):
    Student = namedtuple('Student', columns)
    students = [Student(*row) for row in rows]
    total_marks = sum(student.MARKS for student in students)
    return round(total_marks / n, 2)

