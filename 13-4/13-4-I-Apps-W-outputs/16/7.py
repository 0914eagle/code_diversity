
def get_finalists(results, k):
    # Sort the results in ascending order
    sorted_results = sorted(results)

    # Get the indices of the top k results
    top_k_indices = sorted_results[:k]

    # Get the indices of the bottom n - 2k results
    bottom_n_indices = sorted_results[n - 2k:]

    # Get the finalists by combining the top k and bottom n - 2k results
    finalists = top_k_indices + bottom_n_indices

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

