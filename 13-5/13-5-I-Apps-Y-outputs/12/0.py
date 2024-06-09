
from collections import namedtuple

def get_column_indexes(columns):
    return {column: index for index, column in enumerate(columns)}

def get_student_info(line):
    columns = line.split()
    return namedtuple('Student', 'id marks class name')(columns[0], columns[1], columns[2], columns[3])

def calculate_average_marks(students):
    total_marks = sum(student.marks for student in students)
    return total_marks / len(students)

def main():
    columns = input().split()
    column_indexes = get_column_indexes(columns)
    students = []
    for _ in range(int(input())):
        line = input()
        student = get_student_info(line)
        students.append(student)
    average_marks = calculate_average_marks(students)
    print(f'{average_marks:.2f}')

if __name__ == '__main__':
    main()

