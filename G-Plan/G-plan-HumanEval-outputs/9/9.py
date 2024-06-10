
from typing import List

def numerical_letter_grade(grades: List[float]) -> List[str]:
    def get_letter_grade(gpa: float) -> str:
        grade_table = {
            4.0: 'A+',
            3.7: 'A',
            3.3: 'A-',
            3.0: 'B+',
            2.7: 'B',
            2.3: 'B-',
            2.0: 'C+',
            1.7: 'C',
            1.3: 'C-',
            1.0: 'D+',
            0.7: 'D',
            0.0: 'D-'
        }
        for gpa_range, letter_grade in grade_table.items():
            if gpa >= gpa_range:
                return letter_grade
        return 'E'

    return [get_letter_grade(gpa) for gpa in grades]

grades = list(map(float, input().split()))
print(numerical_letter_grade(grades))
