
def solve(n, values):
    # Initialize the BDD with a single vertex representing the root
    bdd = [0]

    # Iterate over the input values
    for i in range(len(values)):
        # Convert the input value to binary
        binary = "{0:b}".format(i)

        # Iterate over the bits of the binary representation
        for j in range(n):
            # Get the current vertex and its label
            vertex = bdd[len(bdd) - 1]
            label = binary[j]

            # If the vertex is a leaf vertex, create a new vertex and add it to the BDD
            if vertex == 0 or vertex == 1:
                bdd.append(int(label))
                vertex = len(bdd) - 1

            # If the vertex is not a leaf vertex, follow the edge labelled with the current bit
            else:
                vertex = vertex + 1 if label == "1" else vertex + 2

            # Set the current vertex as the parent of the new vertex
            bdd[len(bdd) - 1] = vertex

    # Return the number of vertices in the minimal BDD
    return len(bdd)

