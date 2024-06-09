
def solve(n, scores):
    # Sort the scores in descending order
    scores.sort(reverse=True)

    # Initialize the number of ways to choose a subset of participants to be awarded with diplomas
    ways = 0

    # Loop through the scores and count the number of ways to choose a subset of participants to be awarded with diplomas
    for i in range(n):
        # If the current score is non-zero, increment the number of ways
        if scores[i] != 0:
            ways += 1

    # Return the number of ways
    return ways

