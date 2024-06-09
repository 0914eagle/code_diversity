
def solve(s):
    # Calculate the maximum score that can be obtained
    max_score = sum(s)

    # If the maximum score is a multiple of 10, return 0
    if max_score % 10 == 0:
        return 0

    # Otherwise, return the maximum score
    return max_score

