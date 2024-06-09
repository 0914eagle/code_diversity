
def longest_interesting_subsequence(sequence, s):
    # Initialize variables
    n = len(sequence)
    k = n // 2
    longest = [0] * n

    # Loop through the sequence and calculate the length of the longest interesting subsequence starting with each element
    for i in range(n):
        # If the sum of the first k elements is less than or equal to s, update the length of the longest interesting subsequence
        if sum(sequence[:k]) <= s:
            longest[i] = k
        # If the sum of the last k elements is less than or equal to s, update the length of the longest interesting subsequence
        if sum(sequence[-k:]) <= s:
            longest[i] = k
    
    return longest

