
def solve(n, scores):
    # Sort the scores in non-decreasing order
    scores.sort()

    # Initialize the number of ways to choose a subset as 0
    ways = 0

    # Iterate over the scores
    for i in range(n):
        # Check if the current score is non-zero
        if scores[i] != 0:
            # Increment the number of ways to choose a subset
            ways += 1

            # Iterate over the remaining scores
            for j in range(i+1, n):
                # Check if the current score is greater than or equal to the previous score
                if scores[j] >= scores[i]:
                    # Increment the number of ways to choose a subset
                    ways += 1

    # Return the number of ways to choose a subset
    return ways

