
from collections import namedtuple

def get_average_marks(my_tuple):
    Student = namedtuple('Student', 'id, marks, class, name')
    total_marks = 0
    for student in my_tuple:
        total_marks += student.marks
    average_marks = total_marks / len(my_tuple)
    return round(average_marks, 2)

