
def solve(n, results):
    # Sort the results in ascending order
    results.sort()
    
    # Initialize the two strings for the finalists
    finalists1 = "0" * n
    finalists2 = "0" * n
    
    # Loop through each result and check if it is a finalist
    for i in range(n):
        if results[i] <= results[n - 1 - i]:
            finalists1 = finalists1[:i] + "1" + finalists1[i + 1:]
        if results[i] <= results[n - 1 - i]:
            finalists2 = finalists2[:i] + "1" + finalists2[i + 1:]
    
    return finalists1, finalists2

