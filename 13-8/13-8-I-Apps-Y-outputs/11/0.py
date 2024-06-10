
import collections

def get_column_indexes(header):
    column_indexes = {}
    for i, column_name in enumerate(header):
        column_indexes[column_name] = i
    return column_indexes

def get_average_marks(marks):
    total = 0
    for mark in marks:
        total += mark
    return total / len(marks)

def main():
    num_students = int(input())
    header = input().split()
    column_indexes = get_column_indexes(header)
    marks = []
    for _ in range(num_students):
        line = input().split()
        marks.append(int(line[column_indexes["MARKS"]]))
    average_marks = get_average_marks(marks)
    print(f"{average_marks:.2f}")

if __name__ == '__main__':
    main()

