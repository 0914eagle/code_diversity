
def solve(N, K, A, F):
    # Sort the members by their consumption coefficient in descending order
    sorted_members = sorted(range(N), key=lambda i: A[i], reverse=True)

    # Initialize the minimum score to 0
    min_score = 0

    # Loop through each member and their corresponding food
    for i, j in enumerate(sorted_members):
        # Calculate the time it takes for the member to finish the food
        time = (A[j] - i) * F[j]

        # If the time is greater than the minimum score, update the minimum score
        if time > min_score:
            min_score = time

    # Return the minimum score
    return min_score

