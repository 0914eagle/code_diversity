
from collections import namedtuple

Student = namedtuple('Student', 'id marks class name')

def get_average_marks(my_list):
    total = 0
    for student in my_list:
        total += student.marks
    return total / len(my_list)

def main():
    n = int(input())
    column_names = input().split()
    my_list = []
    for _ in range(n):
        values = input().split()
        student = Student(id=values[column_names.index('ID')], marks=int(values[column_names.index('MARKS')]), class=values[column_names.index('CLASS')], name=values[column_names.index('NAME')])
        my_list.append(student)
    print(f"{get_average_marks(my_list):.2f}")

if __name__ == '__main__':
    main()

