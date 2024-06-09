
def solve(n, a):
    # Initialize the number of connected components to 0
    num_components = 0

    # Iterate over each pair of vertices (l, r)
    for l in range(1, n + 1):
        for r in range(l, n + 1):
            # Initialize a set to store the vertices that are left in the tree
            vertices_left = set()

            # Iterate over each vertex in the tree
            for i in range(1, n + 1):
                # If the vertex value is between l and r, include it in the set of vertices left in the tree
                if l <= a[i - 1] <= r:
                    vertices_left.add(i)

            # If there is at least one vertex left in the tree, increment the number of connected components
            if len(vertices_left) > 0:
                num_components += 1

    # Return the total number of connected components
    return num_components

