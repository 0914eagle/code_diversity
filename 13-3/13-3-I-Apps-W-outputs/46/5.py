
def get_finalists(results, k):
    # Sort the results in ascending order
    sorted_results = sorted(results)

    # Find the k-th smallest element in the sorted results
    kth_smallest = sorted_results[k]

    # Find the indices of the results that are less than or equal to the k-th smallest element
    finalists = [i for i, x in enumerate(results) if x <= kth_smallest]

    return finalists

def main():
    n = int(input())
    results = []
    for i in range(n):
        results.append(int(input()))

    k = int(input())
    finalists = get_finalists(results, k)

    print(" ".join([str(int(i in finalists)) for i in range(n)]))

if __name__ == '__main__':
    main()

