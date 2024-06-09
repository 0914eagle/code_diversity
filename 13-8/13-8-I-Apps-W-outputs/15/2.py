
def solve(n, a):
    # Initialize a dictionary to store the number of connected components for each range of values
    counts = {}

    # Iterate over the range of values
    for l in range(1, n + 1):
        for r in range(l, n + 1):
            # Initialize a set to store the vertices that are included in the range
            included = set()

            # Iterate over the vertices
            for i in range(n):
                # If the vertex value is in the range, add it to the included set
                if l <= a[i] <= r:
                    included.add(i)

            # Initialize a set to store the connected components
            components = set()

            # Iterate over the included vertices
            for i in included:
                # If the vertex is not already in a component, create a new component
                if i not in components:
                    components.add(i)
                    queue = [i]

                    # Breadth-first search to find all connected components
                    while queue:
                        vertex = queue.pop(0)
                        for neighbor in get_neighbors(vertex, n):
                            if neighbor in included and neighbor not in components:
                                components.add(neighbor)
                                queue.append(neighbor)

            # Add the number of connected components to the dictionary
            counts[f"{l}-{r}"] = len(components)

    # Calculate the sum of the function values
    result = sum(counts.values())

    return result

# Function to get the neighbors of a vertex
def get_neighbors(vertex, n):
    neighbors = []
    for i in range(vertex + 1, n + 1):
        neighbors.append(i)
    return neighbors

n = 4
a = [2, 1, 1, 3]
print(solve(n, a))

