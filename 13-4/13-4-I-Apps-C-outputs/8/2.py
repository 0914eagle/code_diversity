
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

    # While there are still elements to be added to the sequence
    while A > 0 and B > 0:
        # If the current element is less than or equal to the previous element, it is part of the longest increasing subsequence
        if seq[-1] <= N:
            seq.append(seq[-1] + 1)
            A -= 1
        # If the current element is greater than the previous element, it is part of the longest decreasing subsequence
        else:
            seq.append(seq[-1] - 1)
            B -= 1

    # If there are still elements to be added to the sequence, it is not possible to construct a valid sequence
    if A > 0 or B > 0:
        return -1

    return seq

