
def solve(n):
    correct_answers = input().split()
    score = 0
    for i in range(n):
        if correct_answers[i] == input():
            score += 1
    return score

