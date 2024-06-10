
from collections import namedtuple

def get_student_info(n):
    columns = input().split()
    Student = namedtuple('Student', columns)
    students = []
    for _ in range(n):
        student = Student(*input().split())
        students.append(student)
    return students

def calculate_average(students):
    total = 0
    for student in students:
        total += int(student.MARKS)
    return total / len(students)

if __name__ == '__main__':
    n = int(input())
    students = get_student_info(n)
    average = calculate_average(students)
    print(f'{average:.2f}')

