
def get_finalists(n, results):
    # Sort the results in ascending order
    sorted_results = sorted(results)

    # Initialize the finalists as all zeros
    finalists = [0] * n

    # Determine the k value based on the number of finalists needed
    k = n // 2

    # Fill the finalists list with the top k results from each semifinal
    for i in range(k):
        finalists[i] = 1
        finalists[n - 1 - i] = 1

    # Fill the remaining places with the top (n - 2k) results from each semifinal
    for i in range(k, n - k):
        finalists[i] = 1
        finalists[n - 1 - i] = 1

    return finalists

