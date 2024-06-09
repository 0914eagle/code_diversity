
def get_final_score(answers):
    n = len(answers)
    correct_answers = [answers[i] for i in range(n)]
    final_score = 0
    for i in range(n):
        if correct_answers[i] == answers[i]:
            final_score += 1
    return final_score

