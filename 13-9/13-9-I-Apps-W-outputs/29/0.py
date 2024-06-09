
def get_finalists(results, k):
    # Sort the results in ascending order
    results.sort()
    
    # Initialize the finalists array
    finalists = [0] * len(results)
    
    # Find the k best results in each semifinal
    k_best = results[:k]
    
    # Find the index of the k-th best result in each semifinal
    k_best_index = [results.index(result) for result in k_best]
    
    # Set the finalists for the k-th best results in each semifinal
    for i in range(k):
        finalists[k_best_index[i]] = 1
    
    # Set the finalists for the other places
    for i in range(k, len(results)):
        if results[i] not in k_best:
            finalists[i] = 1
    
    return finalists

