
def solve(N, M):
    # Initialize a list to store the results
    results = []

    # Iterate over the even numbers from 0 to 2N
    for i in range(0, 2*N+1, 2):
        # Check if the current number is odd
        if i % 2 == 1:
            # If the current number is odd, we can add it to the list of results
            results.append(i)

    # Return the length of the list of results
    return len(results)

