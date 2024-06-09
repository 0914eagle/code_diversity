
def is_problem_easy(n, responses):
    easy_count = 0
    for response in responses:
        if response == 0:
            easy_count += 1
    if easy_count == n:
        return "EASY"
    else:
        return "HARD"

