
def get_finalists(results, k):
    # Sort the results in ascending order
    results.sort()
    
    # Get the top k results from each semifinal
    top_k_results = results[:k]
    
    # Get the bottom n - 2k results from each semifinal
    bottom_n_minus_2k_results = results[n - 2k:]
    
    # Get the finalists by combining the top k results from each semifinal and the bottom n - 2k results
    finalists = top_k_results + bottom_n_minus_2k_results
    
    return finalists

def main():
    n = int(input())
    results = []
    for i in range(n):
        results.append(int(input()))
    
    k = int(input())
    finalists = get_finalists(results, k)
    
    print(" ".join(str(finalist) for finalist in finalists))

if __name__ == '__main__':
    main()

