
def solve(n, m):
    mod = 1000000009
    # Initialize a list to store the results
    results = [0] * (n + 1)
    results[0] = 1
    
    # Iterate over each possible length of the sequence
    for i in range(1, n + 1):
        # Iterate over each possible starting index for the sequence
        for j in range(m):
            # If the sequence is not a wool sequence, add it to the results
            if j ^ (j + i - 1) != 0:
                results[i] += results[i - 1]
        results[i] %= mod
    
    return results[n]

