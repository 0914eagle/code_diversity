
def solve(N, A, B):
    # Initialize a list to store the permutation
    perm = list(range(1, N+1))
    # Initialize a list to store the values of g(i) for each i
    g = [0] * (N+1)
    # Initialize a set to keep track of the values of g(i) that have been used
    used = set()
    # Loop through each i from 1 to N
    for i in range(1, N+1):
        # If the value of g(i) has not been used before, use it
        if g[i] not in used:
            # If the value of g(i) is A or B, use it
            if g[i] in [A, B]:
                used.add(g[i])
            # Otherwise, find the next unused value of g(i)
            else:
                for j in range(i+1, N+1):
                    if g[j] not in used:
                        g[i] = g[j]
                        used.add(g[i])
                        break
    # If all the values of g(i) have been used, return the permutation
    if len(used) == N:
        return perm
    # Otherwise, return -1
    else:
        return -1

