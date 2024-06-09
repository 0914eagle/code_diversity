
def solve(N, M):
    # Initialize a list to store the results
    results = []

    # Iterate over the range of possible values for the sum
    for i in range(0, N+M, 2):
        # Check if the sum is even
        if i % 2 == 0:
            # Add the result to the list
            results.append(i)

    # Return the length of the list
    return len(results)

