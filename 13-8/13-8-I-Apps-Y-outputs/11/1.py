
from collections import namedtuple

def get_data(n):
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

def main():
    n = int(input())
    students = get_data(n)
    average = calculate_average(students)
    print(round(average, 2))

if __name__ == '__main__':
    main()

