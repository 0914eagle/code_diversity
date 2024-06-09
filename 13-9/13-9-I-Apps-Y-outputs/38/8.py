
def get_final_score(n):
    answers = input().split()
    return sum([1 for i, ans in enumerate(answers, 1) if ans == "A" and i <= n])

