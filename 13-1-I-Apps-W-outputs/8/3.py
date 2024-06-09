
def get_finalists(n, results):
    # Sort the results in ascending order
    results.sort()
    
    # Initialize the finalists array
    finalists = [0] * n
    
    # Loop through the results and mark the finalists
    for i in range(n):
        if results[i] <= results[n-1-i]:
            finalists[i] = 1
    
    return finalists

