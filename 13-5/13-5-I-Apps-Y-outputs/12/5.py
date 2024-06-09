
from collections import namedtuple

Student = namedtuple('Student', 'id, marks, class, name')

def get_average_marks(student_list):
    total_marks = 0
    for student in student_list:
        total_marks += student.marks
    return total_marks / len(student_list)

def main():
    num_students = int(input())
    column_names = input().split()
    student_list = []
    for _ in range(num_students):
        student_info = input().split()
        student_list.append(Student(id=student_info[column_names.index('ID')], marks=int(student_info[column_names.index('MARKS')]), class=student_info[column_names.index('CLASS')], name=student_info[column_names.index('NAME')]))
    average_marks = get_average_marks(student_list)
    print(f'{average_marks:.2f}')

if __name__ == '__main__':
    main()

