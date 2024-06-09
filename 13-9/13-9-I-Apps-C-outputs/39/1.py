
def solve(n, hits):
    # Check if the number of hits is valid
    if sum(hits) % 2 != 0:
        return -1

    # Initialize the target matrix
    targets = [[0] * n for _ in range(n)]

    # Populate the target matrix with targets
    for i in range(n):
        for j in range(hits[i]):
            targets[i][j] = 1

    # Check if the target matrix is valid
    for i in range(n):
        if sum(targets[i]) > 2:
            return -1
        for j in range(n):
            if sum(targets[j]) > 2:
                return -1

    # Return the target matrix
    return targets

