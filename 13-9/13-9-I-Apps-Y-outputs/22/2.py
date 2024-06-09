
def max_grade(scores):
    max_grade = 0
    for score in scores:
        if score % 10 != 0:
            max_grade += score
    return max_grade

