
def solve(N, K, A, F):
    # Sort the members by their consumption coefficient in descending order
    A.sort(reverse=True)
    # Initialize the minimum score to 0
    min_score = 0
    # Loop through each member and their corresponding food
    for i, a in enumerate(A):
        # Calculate the time it takes for the member to finish the food
        time = (a - 1) * F[i]
        # If the time is greater than the minimum score, update the minimum score
        if time > min_score:
            min_score = time
        # If the member has done all the training possible, break the loop
        if a - 1 == 0:
            break
    # Return the minimum score
    return min_score

