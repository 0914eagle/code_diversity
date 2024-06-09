
def solve(n, arr):
    # Initialize a dictionary to store the components
    components = {}

    # Iterate over the array
    for i in range(n):
        # If the current vertex is not in any component, create a new component
        if i not in components:
            components[i] = set([i])
        # If the current vertex is in a component, add it to that component
        else:
            components[i].add(i)

        # If the current vertex is not the last vertex, check if the next vertex is in the component
        if i != n - 1:
            # If the next vertex is not in the component, create a new component
            if i + 1 not in components:
                components[i + 1] = set([i + 1])
            # If the next vertex is in the component, add it to that component
            else:
                components[i + 1].add(i + 1)

    # Initialize a variable to store the sum
    sum = 0

    # Iterate over the components
    for component in components.values():
        # If the component has more than one vertex, add it to the sum
        if len(component) > 1:
            sum += 1

    # Return the sum
    return sum

