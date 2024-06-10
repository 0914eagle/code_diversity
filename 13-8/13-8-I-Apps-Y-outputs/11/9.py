
from collections import namedtuple

def get_student_details(n):
    columns = input().split()
    Student = namedtuple('Student', columns)
    students = []
    for _ in range(n):
        student = Student(*input().split())
        students.append(student)
    return students

def get_average_marks(students):
    total_marks = 0
    for student in students:
        total_marks += int(student.MARKS)
    return total_marks / len(students)

if __name__ == '__main__':
    n = int(input())
    students = get_student_details(n)
    average_marks = get_average_marks(students)
    print(f'{average_marks:.2f}')

