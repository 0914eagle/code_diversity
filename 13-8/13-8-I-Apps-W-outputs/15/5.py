
def solve(n, a):
    # Initialize the number of connected components to 0
    num_components = 0

    # Iterate over each pair of vertices (l, r)
    for l in range(1, n + 1):
        for r in range(l, n + 1):
            # Initialize a set to store the vertices that are left in the tree
            vertices = set()

            # Iterate over each vertex i
            for i in range(1, n + 1):
                # If the value of vertex i is in the range [l, r]
                if l <= a[i - 1] <= r:
                    # Add vertex i to the set of vertices that are left in the tree
                    vertices.add(i)

            # If there is at least one vertex left in the tree
            if vertices:
                # Increment the number of connected components
                num_components += 1

    # Return the total number of connected components
    return num_components

