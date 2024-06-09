
from collections import namedtuple

def get_average_marks(my_list):
    # create a namedtuple to represent a student
    Student = namedtuple('Student', 'id marks class name')

    # create a list to store the students
    students = []

    # loop through the list of lists
    for lst in my_list:
        # create a student object and add it to the students list
        students.append(Student(lst[0], lst[1], lst[2], lst[3]))

    # calculate the sum of all marks
    sum_marks = sum(student.marks for student in students)

    # calculate the average marks
    average_marks = sum_marks / len(students)

    # return the average marks rounded to 2 decimal places
    return round(average_marks, 2)

