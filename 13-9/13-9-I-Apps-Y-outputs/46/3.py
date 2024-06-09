
def solve(N, M):
    # Initialize a list to store the results
    results = []

    # Iterate over the range of numbers from 1 to N+M
    for i in range(1, N+M+1):
        # Check if the current number is even
        if i % 2 == 0:
            # If the current number is even, add it to the results list
            results.append(i)

    # Return the length of the results list
    return len(results)

