
def solve(n, results):
    # Sort the results in ascending order
    results.sort()

    # Initialize the strings for the two semifinals
    semifinal1 = "0" * n
    semifinal2 = "0" * n

    # Determine the k value based on the results
    k = 0
    while k < n and results[k] <= results[n - 1 - k]:
        k += 1

    # Mark the finalists in each semifinal
    for i in range(k):
        semifinal1 = semifinal1[:i] + "1" + semifinal1[i + 1:]
        semifinal2 = semifinal2[:i] + "1" + semifinal2[i + 1:]

    # Mark the other places in each semifinal
    for i in range(k, n):
        if results[i] <= results[n - 1 - k]:
            semifinal1 = semifinal1[:i] + "1" + semifinal1[i + 1:]
        else:
            semifinal2 = semifinal2[:i] + "1" + semifinal2[i + 1:]

    return semifinal1, semifinal2

