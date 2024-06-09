
def get_maximum_grade(scores):
    maximum_grade = 0
    for score in scores:
        maximum_grade += score
        if maximum_grade % 10 == 0:
            maximum_grade -= 1
    return maximum_grade

