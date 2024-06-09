
def solve(N, u, p):
    # Initialize variables
    L = 0
    M = 0
    parents = [-1] + p
    depth = [0] * (N + 1)
    nondecreasing = [True] * (N + 1)

    # Compute the depth of each vertex and check if the labels are nondecreasing
    for i in range(1, N + 1):
        depth[i] = depth[parents[i]] + 1
        nondecreasing[i] = nondecreasing[parents[i]] and u[i] >= u[parents[i]]

    # Iterate over all vertices and check if they are part of a jumping path
    for i in range(1, N + 1):
        # If the vertex is not part of a jumping path, skip it
        if nondecreasing[i]:
            continue

        # Initialize the length of the jumping path and the current vertex
        length = 1
        curr = i

        # Iterate over the ancestors of the current vertex
        while parents[curr] != -1:
            # If the ancestor is not part of a jumping path, break
            if not nondecreasing[parents[curr]]:
                break

            # Update the length of the jumping path and the current vertex
            length += 1
            curr = parents[curr]

        # If the length of the jumping path is greater than the current maximum, update the maximum
        if length > L:
            L = length
            M = 1

        # If the length of the jumping path is equal to the current maximum, increment the number of jumping paths
        elif length == L:
            M += 1

    # Return the maximum length and the number of jumping paths modulo the prime
    return L, M % 11092019

