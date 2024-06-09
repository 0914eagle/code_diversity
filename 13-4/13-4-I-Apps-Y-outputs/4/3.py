
def round_dances(n):
    # Initialize a list to store the results
    results = []

    # Iterate over each possible combination of people for the first round dance
    for i in range(1, n + 1):
        # Get the remaining people for the second round dance
        remaining = list(range(1, n + 1))
        remaining.remove(i)

        # Check if the number of people in the second round dance is equal to n/2
        if len(remaining) == n // 2:
            # Add the combination to the results list
            results.append([i] + remaining)

    # Return the number of possible round dances
    return len(results)

