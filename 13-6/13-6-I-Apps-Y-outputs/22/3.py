
from collections import namedtuple

def get_average_marks(my_list):
    # create a namedtuple to represent a student
    Student = namedtuple('Student', 'id marks class name')

    # create an empty list to store the students
    students = []

    # iterate over the input list
    for line in my_list:
        # split the line into columns
        cols = line.split()

        # create a Student object from the columns
        student = Student(id=cols[0], marks=cols[1], class=cols[2], name=cols[3])

        # add the student to the list
        students.append(student)

    # calculate the sum of all marks
    sum_marks = sum(student.marks for student in students)

    # calculate the average marks
    average_marks = sum_marks / len(students)

    # return the average marks
    return average_marks

