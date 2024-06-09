
def solve(N, K, A, F):
    # Sort the members by their consumption coefficient in descending order
    sorted_members = sorted(range(N), key=lambda i: A[i], reverse=True)

    # Initialize the minimum score to 0
    min_score = 0

    # Loop through each member and their corresponding food
    for i, j in enumerate(sorted_members):
        # Calculate the time it takes for the member to finish the food
        time = (A[j] - min(K, A[j])) * F[i]

        # Update the minimum score if the time is greater than the current minimum score
        min_score = max(min_score, time)

        # Decrement the number of training sets available for the member
        K -= min(K, A[j])

    return min_score

