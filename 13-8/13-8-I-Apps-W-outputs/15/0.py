
def solve(n, a):
    # Initialize a dictionary to store the components
    components = {}

    # Iterate over the inputs
    for i in range(n):
        # Get the current vertex value
        vertex_value = a[i]

        # If the vertex value is not in the components dictionary, add it to the dictionary with a count of 1
        if vertex_value not in components:
            components[vertex_value] = 1

        # If the vertex value is in the components dictionary, increment the count by 1
        else:
            components[vertex_value] += 1

    # Initialize a variable to store the sum
    sum = 0

    # Iterate over the components
    for component in components:
        # Get the count of vertices with the current component value
        count = components[component]

        # Add the count to the sum
        sum += count

    # Return the sum
    return sum

