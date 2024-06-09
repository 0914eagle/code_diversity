
from collections import namedtuple

def get_average_marks(my_list):
    # create a namedtuple to represent a student
    Student = namedtuple('Student', 'id marks class name')

    # create a list to store the students
    students = []

    # iterate over the input list
    for line in my_list:
        # split the line into columns
        columns = line.split()

        # create a Student object from the columns
        student = Student(id=columns[0], marks=columns[1], class=columns[2], name=columns[3])

        # add the student to the list
        students.append(student)

    # calculate the sum of all marks
    sum_marks = sum(student.marks for student in students)

    # calculate the average marks
    average_marks = sum_marks / len(students)

    # return the average marks
    return average_marks

