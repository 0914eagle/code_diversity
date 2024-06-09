
def solve(n, m, edges):
    # Initialize a list to store the permutation
    permutation = [0] * n
    # Initialize a set to keep track of the vertices that have been labeled
    labeled = set()
    # Loop through the edges and assign labels based on the conditions
    for edge in edges:
        v, u = edge
        if v not in labeled:
            permutation[v] = len(labeled) + 1
            labeled.add(v)
        if u not in labeled:
            permutation[u] = len(labeled) + 1
            labeled.add(u)
    # Return the lexicographically smallest permutation
    return permutation

