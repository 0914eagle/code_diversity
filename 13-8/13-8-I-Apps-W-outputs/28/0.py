
def get_minimal_bdd_vertices(n, function_values):
    # Initialize the BDD with a single vertex representing the root
    bdd = [0]

    # Iterate over the function values
    for i in range(2**n):
        # Get the current vertex and the label of the edge leading to it
        vertex, label = bdd[-1], i % 2

        # If the vertex is not a leaf vertex, create a new vertex and add it to the BDD
        if vertex != 1:
            bdd.append(vertex ^ label)

        # If the vertex is a leaf vertex, check if it is a duplicate of an existing vertex
        else:
            for j in range(len(bdd) - 1):
                if bdd[j] == vertex:
                    bdd[j] = vertex ^ label
                    break
            else:
                bdd.append(vertex ^ label)

    # Return the number of vertices in the BDD
    return len(set(bdd))

