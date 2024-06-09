
def solve(n):
    # Initialize a list to store the throw scores
    throw_scores = []
    
    # Iterate through the possible throw scores (1-20)
    for i in range(1, 21):
        # Check if the current throw score is a multiple of 3
        if i % 3 == 0:
            # If the current throw score is a multiple of 3, add it to the list of throw scores
            throw_scores.append(i)
    
    # Check if the sum of the throw scores is equal to the target score
    if sum(throw_scores) == n:
        # If the sum of the throw scores is equal to the target score, return the list of throw scores
        return throw_scores
    else:
        # If the sum of the throw scores is not equal to the target score, return "impossible"
        return "impossible"

