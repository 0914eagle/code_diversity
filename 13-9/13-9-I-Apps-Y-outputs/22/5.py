
def get_max_score(scores):
    max_score = sum(scores)
    while max_score % 10 == 0:
        max_score -= 1
    return max_score

