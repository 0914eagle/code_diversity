
def solve(n, m):
    mod = 1000000009
    # Initialize a list to store the results
    results = [0] * (n + 1)
    results[0] = 1
    
    # Iterate over the range of values for m
    for i in range(1, m + 1):
        # Iterate over the range of values for n
        for j in range(1, n + 1):
            # Calculate the number of sequences of length j and value i
            results[j] += results[j - 1]
            results[j] %= mod
    
    # Return the result
    return results[n]

