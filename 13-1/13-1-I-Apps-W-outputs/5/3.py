
def solve(N, K, A, F):
    # Sort the members by their consumption coefficient in descending order
    sorted_members = sorted(range(N), key=lambda i: A[i], reverse=True)

    # Initialize the minimum score to infinity
    min_score = float('inf')

    # Loop through all possible combinations of training sets
    for training_sets in range(K+1):
        # Initialize the current score to 0
        current_score = 0

        # Loop through the members and assign them to foods
        for i in range(N):
            # Calculate the time it takes for the current member to finish the food
            time_taken = (A[sorted_members[i]] - training_sets) * F[i]

            # Update the current score if the time taken is greater than the current score
            if time_taken > current_score:
                current_score = time_taken

        # Update the minimum score if the current score is less than the minimum score
        if current_score < min_score:
            min_score = current_score

    # Return the minimum score
    return min_score

