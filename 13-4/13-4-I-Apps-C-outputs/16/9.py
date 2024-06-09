
def longest_interesting_subsequence(A, S):
    # Initialize variables
    N = len(A)
    longest = [0] * N

    # Loop through each element in the array
    for i in range(N):
        # Loop through each possible length of the subsequence
        for k in range(1, N-i+1):
            # Check if the sum of the first k elements is less than or equal to S
            if sum(A[i:i+k]) <= S:
                # Update the longest subsequence length
                longest[i] = max(longest[i], k)

    return longest

