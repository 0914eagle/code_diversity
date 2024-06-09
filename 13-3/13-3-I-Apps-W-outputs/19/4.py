
def solve(n, arr):
    # Initialize a dictionary to store the frequency of each number
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    # Initialize the minimum number of operations to 0
    min_ops = 0

    # Iterate through the dictionary and find the minimum number of operations required to delete all elements
    for i in freq:
        min_ops += freq[i]

    return min_ops

