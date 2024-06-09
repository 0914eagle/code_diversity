
def solve(n, a):
    # Initialize a list to store the components
    components = []

    # Iterate over the input array
    for i in range(n):
        # If the current vertex is not already in any component, create a new component
        if not any(a[i] in component for component in components):
            components.append([a[i]])
        # Otherwise, add the current vertex to the existing component
        else:
            components[components.index(a[i])].append(a[i])

    # Return the sum of the sizes of all components
    return sum(len(component) for component in components)

