
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
    while A > 0 and B > 0:
        # If the longest increasing subsequence is not empty
        if A > 0:
            # Add the smallest unused element that is greater than the last element of the sequence
            for i in range(1, N+1):
                if i not in seq:
                    seq.append(i)
                    A -= 1
                    break

        # If the longest decreasing subsequence is not empty
        if B > 0:
            # Add the largest unused element that is less than the last element of the sequence
            for i in range(N, 0, -1):
                if i not in seq:
                    seq.append(i)
                    B -= 1
                    break

    # If there are still elements to add to the sequence, but we cannot find any more elements to add
    if A > 0 or B > 0:
        return -1

    # Return the sequence
    return seq

