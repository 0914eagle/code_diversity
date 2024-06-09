
def get_maximum_grade(scores):
    grade = sum(scores)
    return grade if grade % 10 != 0 else grade - 10

