
def solve(n, a):
    # Initialize a dictionary to store the components
    components = {}

    # Iterate over the vertices
    for i in range(n):
        # If the current vertex is not in any component, create a new component
        if i not in components:
            components[i] = set([i])

        # If the current vertex is in the range [l, r] and its value is less than or equal to the value of the current vertex, add it to the current component
        for j in range(i+1, n):
            if l <= a[j] <= r and a[j] <= a[i]:
                components[i].add(j)

    # Return the number of components
    return len(components)

