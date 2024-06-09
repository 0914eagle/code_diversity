
from collections import namedtuple

def get_input():
    n = int(input())
    column_names = input().split()
    students = []
    for _ in range(n):
        student = namedtuple('Student', 'id marks class_name name')
        student = student._make(input().split())
        students.append(student)
    return students

def calculate_average(students):
    total_marks = 0
    for student in students:
        total_marks += int(student.marks)
    average = total_marks / len(students)
    return average

def main():
    students = get_input()
    average = calculate_average(students)
    print(round(average, 2))

if __name__ == '__main__':
    main()

