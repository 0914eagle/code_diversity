
def solve(n, answers):
    score = 0
    for i, answer in enumerate(answers, start=1):
        if answer == "A":
            score += 1
    return score

