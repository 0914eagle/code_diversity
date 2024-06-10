
import collections

def get_column_index(header, column_name):
    return header.index(column_name)

def get_average_marks(marks):
    return sum(marks) / len(marks)

def main():
    num_students = int(input())
    header = input().split()
    marks_index = get_column_index(header, 'MARKS')
    names_index = get_column_index(header, 'NAME')
    classes_index = get_column_index(header, 'CLASS')
    marks = []
    for _ in range(num_students):
        student = input().split()
        marks.append(int(student[marks_index]))
    average_marks = get_average_marks(marks)
    print(average_marks)

if __name__ == '__main__':
    main()

