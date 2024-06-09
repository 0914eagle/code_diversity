
def solve(N, A, B):
    # Initialize a list to store the sequence
    seq = []

    # If A is 1, we can just fill the sequence with increasing numbers
    if A == 1:
        for i in range(1, N+1):
            seq.append(i)
        return seq

    # If B is 1, we can just fill the sequence with decreasing numbers
    if B == 1:
        for i in range(N, 0, -1):
            seq.append(i)
        return seq

    # If A is 2, we can fill the sequence with increasing numbers and then reverse it
    if A == 2:
        for i in range(1, N+1):
            seq.append(i)
        seq.reverse()
        return seq

    # If B is 2, we can fill the sequence with decreasing numbers and then reverse it
    if B == 2:
        for i in range(N, 0, -1):
            seq.append(i)
        seq.reverse()
        return seq

    # If A is greater than 2, we can fill the sequence with increasing numbers and then insert B-2 numbers in the middle
    if A > 2:
        # Fill the sequence with increasing numbers
        for i in range(1, N+1):
            seq.append(i)

        # Insert B-2 numbers in the middle
        for i in range(B-2):
            seq.insert(N//2, N//2+i)

        return seq

    # If B is greater than 2, we can fill the sequence with decreasing numbers and then insert A-2 numbers in the middle
    if B > 2:
        # Fill the sequence with decreasing numbers
        for i in range(N, 0, -1):
            seq.append(i)

        # Insert A-2 numbers in the middle
        for i in range(A-2):
            seq.insert(N//2, N//2+i)

        return seq

    # If none of the above conditions are met, return -1
    return -1

