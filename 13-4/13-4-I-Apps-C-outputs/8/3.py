
def solve(N, A, B):
    # Initialize a list to store the sequence
    seq = []

    # If A is 0, then the longest increasing subsequence is empty
    if A == 0:
        return -1

    # If B is 0, then the longest decreasing subsequence is empty
    if B == 0:
        return -1

    # If A is 1, then the longest increasing subsequence is a single element
    if A == 1:
        seq.append(1)
        A -= 1

    # If B is 1, then the longest decreasing subsequence is a single element
    if B == 1:
        seq.append(N)
        B -= 1

    # While there are still elements to add to the sequence
    while A > 0 or B > 0:
        # If the longest increasing subsequence is not empty
        if A > 0:
            # Add the next element to the sequence
            seq.append(seq[-1] + 1)
            A -= 1

        # If the longest decreasing subsequence is not empty
        if B > 0:
            # Add the next element to the sequence
            seq.append(seq[-1] - 1)
            B -= 1

    # If there are still elements to add to the sequence, then it is not possible to construct a sequence that satisfies the conditions
    if A > 0 or B > 0:
        return -1

    # Return the constructed sequence
    return seq

