
def round_dances(n):
    # Initialize a list to store the results
    results = []

    # Iterate over each possible combination of round dances
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # Check if the combination is valid
            if i + j == n:
                # Add the combination to the results list
                results.append([i, j])

    # Return the length of the results list
    return len(results)

