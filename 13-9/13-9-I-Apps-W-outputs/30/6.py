
def solve(n, scores):
    # Sort the scores in descending order
    scores.sort(reverse=True)
    
    # Initialize the number of ways to choose a subset as 0
    ways = 0
    
    # Loop through the scores and check if the current score is greater than or equal to the previous score
    for i in range(n-1):
        if scores[i] >= scores[i+1]:
            # If the current score is greater than or equal to the previous score, increment the number of ways
            ways += 1
    
    # Return the number of ways
    return ways

