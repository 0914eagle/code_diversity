
def get_final_score(n, answers):
    return sum(i for i, ans in enumerate(answers, 1) if ans == "A")

