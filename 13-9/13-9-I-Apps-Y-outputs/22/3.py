
def get_max_grade(scores):
    max_grade = sum(scores)
    while max_grade % 10 == 0:
        max_grade -= 1
    return max_grade

