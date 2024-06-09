
def get_finalists(n, results):
    # Sort the results in ascending order
    results.sort()
    
    # Initialize variables to keep track of the finalists
    finalists_1 = []
    finalists_2 = []
    
    # Loop through the results and identify the finalists
    for i in range(n):
        if i < n - 2*k:
            finalists_1.append(results[i])
        elif i < n - k:
            finalists_2.append(results[i])
    
    # Return the finalists for both semifinals
    return finalists_1, finalists_2

