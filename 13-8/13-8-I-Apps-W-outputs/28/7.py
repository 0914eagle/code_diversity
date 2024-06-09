
def get_minimal_bdd_size(n, function_values):
    # Initialize the BDD with a single vertex representing the root
    bdd = [0]

    # Iterate over the function values
    for i in range(len(function_values)):
        # Get the current vertex and the function value for the current input
        vertex = bdd[0]
        value = function_values[i]

        # If the current vertex is a leaf vertex, create a new leaf vertex with the current function value
        if vertex == 0:
            bdd.append(value)
        # If the current vertex is an internal vertex, create a new internal vertex and two child vertices
        else:
            bdd.append(1 - value)
            bdd.append(value)

    # Return the number of vertices in the minimal BDD
    return len(bdd)

