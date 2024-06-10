
from collections import namedtuple

def get_column_indices(column_names):
    return {name: i for i, name in enumerate(column_names)}

def get_average_marks(marks):
    return sum(marks) / len(marks)

def solve(student_data):
    column_names = student_data[0]
    column_indices = get_column_indices(column_names)
    marks = [int(row[column_indices['MARKS']]) for row in student_data[1:]]
    average_marks = get_average_marks(marks)
    return average_marks

def main():
    student_data = [line.strip().split() for line in input().splitlines()]
    average_marks = solve(student_data)
    print(f"{average_marks:.2f}")

if __name__ == '__main__':
    main()

