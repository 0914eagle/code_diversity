
def get_final_score(answers):
    n = len(answers)
    score = 0
    for i in range(n):
        if answers[i] == "A":
            score += 1
    return score

