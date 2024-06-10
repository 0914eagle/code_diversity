
from collections import namedtuple

def get_input():
    n = int(input())
    columns = input().split()
    return n, columns

def get_students(n, columns):
    Students = namedtuple('Students', 'ID, MARKS, CLASS, NAME')
    students = []
    for _ in range(n):
        line = input().split()
        students.append(Students(line[columns.index('ID')], line[columns.index('MARKS')], line[columns.index('CLASS')], line[columns.index('NAME')]))
    return students

def calculate_average(students):
    total_marks = 0
    for student in students:
        total_marks += int(student.MARKS)
    return total_marks / len(students)

def main():
    n, columns = get_input()
    students = get_students(n, columns)
    average = calculate_average(students)
    print(f"{average:.2f}")

if __name__ == '__main__':
    main()

