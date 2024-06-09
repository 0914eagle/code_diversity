
def solve(n, a):
    # Initialize a dictionary to store the components
    components = {}

    # Iterate over the vertices
    for i in range(n):
        # If the current vertex is not in any component, create a new component
        if i not in components:
            components[i] = set([i])

        # If the current vertex is in a component, merge the component with the previous vertex's component
        if i-1 in components:
            components[i-1] |= components[i]
            del components[i]

        # If the current vertex is not in a component, merge it with the previous vertex's component
        if i-1 not in components and i-1 >= 0:
            components[i-1] |= set([i])

    # Initialize a set to store the values of the vertices that are left
    values = set()

    # Iterate over the components
    for component in components.values():
        # If the minimum value of the component is between l and r, include it in the set of values
        if min(component) >= l and min(component) <= r:
            values |= component

    # Return the number of components
    return len(values)

