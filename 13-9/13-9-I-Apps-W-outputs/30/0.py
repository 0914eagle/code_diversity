
def num_ways_to_choose_subset(n, scores):
    # Sort the scores in descending order
    sorted_scores = sorted(scores, reverse=True)
    # Initialize the number of ways to choose a subset as 0
    num_ways = 0
    # Loop through the sorted scores and count the number of ways to choose a subset
    for i in range(n):
        # If the current score is not zero, increment the number of ways
        if sorted_scores[i] != 0:
            num_ways += 1
    # Return the number of ways
    return num_ways

