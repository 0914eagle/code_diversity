
def longest_interesting_subsequence(N, S, A):
    # Initialize the length of the longest interesting subsequence as 0
    longest = 0
    # Iterate over the elements of the array
    for i in range(N):
        # If the sum of the first K elements is less than or equal to S, update the length of the longest interesting subsequence
        if sum(A[:i+1]) <= S:
            longest = max(longest, i+1)
    # Return the length of the longest interesting subsequence
    return longest

