
def is_problem_easy(responses):
    easy_count = responses.count(0)
    hard_count = responses.count(1)
    if hard_count == 0 and easy_count == len(responses):
        return "EASY"
    else:
        return "HARD"

