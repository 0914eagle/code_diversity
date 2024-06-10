
from typing import List

def numerical_letter_grade(grades: List[float]) -> List[str]:
    def gpa_to_letter(gpa: float) -> str:
        if gpa == 4.0:
            return 'A+'
        elif gpa > 3.7:
            return 'A'
        elif gpa > 3.3:
            return 'A-'
        elif gpa > 3.0:
            return 'B+'
        elif gpa > 2.7:
            return 'B'
        elif gpa > 2.3:
            return 'B-'
        elif gpa > 2.0:
            return 'C+'
        elif gpa > 1.7:
            return 'C'
        elif gpa > 1.3:
            return 'C-'
        elif gpa > 1.0:
            return 'D+'
        elif gpa > 0.7:
            return 'D'
        elif gpa > 0.0:
            return 'D-'
        else:
            return 'E'

    return [gpa_to_letter(gpa) for gpa in grades]

if __name__ == "__main__":
    grades = list(map(float, input().split()))
    result = numerical_letter_grade(grades)
    print(result)
