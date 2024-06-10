
from collections import namedtuple

def get_input():
    n = int(input())
    columns = input().split()
    students = []
    for _ in range(n):
        student = namedtuple('Student', columns)(*input().split())
        students.append(student)
    return students

def get_average_marks(students):
    total_marks = sum(student.MARKS for student in students)
    return round(total_marks / len(students), 2)

if __name__ == '__main__':
    students = get_input()
    print(get_average_marks(students))

