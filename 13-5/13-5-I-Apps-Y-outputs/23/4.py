
def get_final_score(n, answers):
    correct_answers = answers.split()
    score = 0
    for i in range(n):
        if correct_answers[i] == 'A':
            score += 1
    return score

