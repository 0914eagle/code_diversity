
from typing import List

def numerical_letter_grade(grades: List[float]) -> List[str]:
    
    grade_list = []
    for grade in grades:
        if grade >= 4.0:
            grade_list.append("A+")
        elif grade > 3.7:
            grade_list.append("A")
        elif grade > 3.3:
            grade_list.append("A-")
        elif grade > 3.0:
            grade_list.append("B+")
        elif grade > 2.7:
            grade_list.append("B")
        elif grade > 2.3:
            grade_list.append("B-")
        elif grade > 2.0:
            grade_list.append("C+")
        elif grade > 1.7:
            grade_list.append("C")
        elif grade > 1.3:
            grade_list.append("C-")
        elif grade > 1.0:
            grade_list.append("D+")
        elif grade > 0.7:
            grade_list.append("D")
        elif grade > 0.0:
            grade_list.append("D-")
        else:
            grade_list.append("E")
    return grade_list

