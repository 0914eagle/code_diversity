
def find_score(answers):
    n = len(answers)
    score = 0
    for i, answer in enumerate(answers):
        if answer == "A":
            score += 1
    return score

