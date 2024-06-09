
def get_finalists(n, results):
    # Sort the results in ascending order
    results.sort()
    
    # Initialize the finalists array with False values
    finalists = [False] * n
    
    # Set the first k participants as finalists
    k = (n + 1) // 2
    for i in range(k):
        finalists[i] = True
    
    # Set the remaining finalists based on the time
    for i in range(k, n):
        finalists[i] = results[i] != results[i - k]
    
    return finalists

