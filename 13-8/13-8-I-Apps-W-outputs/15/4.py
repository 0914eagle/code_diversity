
def solve(n, a):
    # Initialize a list to store the results
    results = [0] * (n + 1)
    # Iterate over the input array
    for i in range(n):
        # Get the current value
        curr = a[i]
        # Iterate over the previous values
        for j in range(i):
            # If the current value is between the previous value and the current value, increment the result
            if a[j] < curr and curr <= a[i]:
                results[i + 1] += 1
    # Return the sum of the results
    return sum(results)

