
def solve(N, A, B):
    # Initialize a list to store the permutation
    perm = [0] * (N + 1)
    # Initialize a list to keep track of the values that have been used
    used = [False] * (N + 1)
    # Initialize the first value in the permutation
    perm[1] = 1
    used[1] = True
    # Iterate from 2 to N
    for i in range(2, N + 1):
        # If A is available, use it
        if not used[A]:
            perm[i] = A
            used[A] = True
        # Otherwise, use B
        else:
            perm[i] = B
            used[B] = True
        # Update A and B for the next iteration
        if A == N:
            A = 1
        else:
            A += 1
        if B == N:
            B = 1
        else:
            B += 1
    # Check if a permutation is possible
    if not used[1]:
        return [-1]
    # Return the permutation
    return perm[1:]

