
def solve(N, A, B):
    # Initialize a list to store the sequence
    seq = [0] * N
    # Set the first element of the sequence
    seq[0] = 1
    # Initialize variables to keep track of the length of the longest increasing and decreasing subsequence
    max_inc_len = 1
    max_dec_len = 1
    # Iterate over the remaining elements of the sequence
    for i in range(1, N):
        # If the length of the longest increasing subsequence is A, we can set the ith element to be A+1
        if max_inc_len == A:
            seq[i] = A + 1
        # If the length of the longest decreasing subsequence is B, we can set the ith element to be B+1
        elif max_dec_len == B:
            seq[i] = B + 1
        # If neither condition is met, we can set the ith element to be 1
        else:
            seq[i] = 1
        # Update the length of the longest increasing and decreasing subsequence
        max_inc_len = max(max_inc_len, seq[i] - seq[i-1])
        max_dec_len = max(max_dec_len, seq[i-1] - seq[i])
    # If the length of the longest increasing subsequence is not A or the length of the longest decreasing subsequence is not B, there is no sequence that satisfies the conditions
    if max_inc_len != A or max_dec_len != B:
        return -1
    return seq

