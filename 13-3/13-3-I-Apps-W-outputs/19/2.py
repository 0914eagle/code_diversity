
def solve(n, arr):
    # Initialize a dictionary to store the frequency of each number
    freq = {}
    for i in range(n):
        if arr[i] not in freq:
            freq[arr[i]] = 1
        else:
            freq[arr[i]] += 1

    # Initialize the minimum number of operations to 0
    min_ops = 0

    # Iterate through the dictionary and find the maximum number of operations required to delete all elements
    for num, count in freq.items():
        min_ops += count // (num + 1)

    return min_ops

