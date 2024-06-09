
def solve(n, m, edges):
    # Initialize a list to store the permutation
    permutation = list(range(1, n+1))
    # Sort the edges in non-decreasing order of their destination vertex
    edges.sort(key=lambda x: x[1])
    # Loop through the edges and update the permutation accordingly
    for edge in edges:
        # Find the index of the destination vertex in the permutation
        index = permutation.index(edge[1])
        # Swap the destination vertex with the next vertex in the permutation
        permutation[index], permutation[index+1] = permutation[index+1], permutation[index]
    return permutation

