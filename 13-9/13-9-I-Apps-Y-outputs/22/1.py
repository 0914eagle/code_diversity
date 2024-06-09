
def find_max_grade(scores):
    max_grade = sum(scores)
    if max_grade % 10 == 0:
        max_grade -= 10
    return max_grade

