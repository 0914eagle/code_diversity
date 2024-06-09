
def get_finalists(results, k):
    # Sort the results in ascending order
    results.sort()
    
    # Get the indices of the top k results
    top_k_indices = results[:k]
    
    # Get the indices of the bottom n - 2k results
    bottom_n_indices = results[n - 2k:]
    
    # Get the finalists by combining the top k and bottom n - 2k results
    finalists = top_k_indices + bottom_n_indices
    
    return finalists

def get_finalists_string(results, k):
    finalists = get_finalists(results, k)
    finalists_string = "".join([str(int(i in finalists)) for i in range(n)])
    return finalists_string

def main():
    n = int(input())
    results = []
    for i in range(n):
        results.append(int(input()))
    
    k = int(input())
    finalists_string = get_finalists_string(results, k)
    print(finalists_string)

if __name__ == '__main__':
    main()

