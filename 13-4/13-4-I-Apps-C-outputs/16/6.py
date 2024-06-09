
def longest_interesting_subsequence(sequence, s):
    # Initialize variables
    n = len(sequence)
    k = n // 2
    longest = [0] * n

    # Loop through the sequence and calculate the longest interesting subsequence
    # starting with each element
    for i in range(n):
        # If the sum of the first k elements is less than or equal to s,
        # the longest interesting subsequence starting with the i-th element
        # is the sum of the first k elements
        if sum(sequence[:k]) <= s:
            longest[i] = k
        # If the sum of the last k elements is less than or equal to s,
        # the longest interesting subsequence starting with the i-th element
        # is the sum of the last k elements
        if sum(sequence[-k:]) <= s:
            longest[i] = k
        # If the sum of the first k elements is greater than s,
        # the longest interesting subsequence starting with the i-th element
        # is the sum of the first k elements minus the i-th element
        if sum(sequence[:k]) > s:
            longest[i] = k - 1
        # If the sum of the last k elements is greater than s,
        # the longest interesting subsequence starting with the i-th element
        # is the sum of the last k elements minus the i-th element
        if sum(sequence[-k:]) > s:
            longest[i] = k - 1

    return longest

