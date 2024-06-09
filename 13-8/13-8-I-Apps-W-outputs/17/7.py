
def get_maximum_clique(A):
    # Initialize a dictionary to store the divisibility graph
    graph = {}

    # Iterate over the elements of A
    for i in range(len(A)):
        # Get the current element
        a_i = A[i]

        # Initialize a list to store the divisible elements
        divisible_elements = []

        # Iterate over the remaining elements of A
        for j in range(i+1, len(A)):
            # Get the current element
            a_j = A[j]

            # Check if a_i is divisible by a_j or vice versa
            if a_i % a_j == 0 or a_j % a_i == 0:
                # If so, add a_j to the list of divisible elements
                divisible_elements.append(a_j)

        # Add the list of divisible elements to the graph
        graph[a_i] = divisible_elements

    # Find the maximum clique in the graph
    maximum_clique = max(networkx.find_cliques(networkx.Graph(graph)))

    # Return the size of the maximum clique
    return len(maximum_clique)

