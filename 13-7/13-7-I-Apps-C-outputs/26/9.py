
def solve(N, A, B):
    # Initialize a list to store the permutation
    perm = [0] * (N + 1)
    # Initialize a list to keep track of the values that have been used
    used = [False] * (N + 1)
    # Initialize the current index
    curr_index = 1
    # Loop until we have used all the values from 1 to N
    while curr_index <= N:
        # If the current index is A or B, add it to the permutation and mark it as used
        if curr_index == A or curr_index == B:
            perm[curr_index] = curr_index
            used[curr_index] = True
            # Increment the current index
            curr_index += 1
        # Otherwise, find the next unused index that is not A or B
        else:
            for i in range(1, N + 1):
                if not used[i] and i != A and i != B:
                    perm[curr_index] = i
                    used[i] = True
                    break
        # If we reach the end of the list and there are still unused indices, return -1
        if curr_index > N:
            for i in range(1, N + 1):
                if not used[i]:
                    return -1
    # Return the permutation
    return perm

