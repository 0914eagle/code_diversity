
import math

def shortest_paths(D, q, queries):
    # Initialize a dictionary to store the number of shortest paths between each pair of vertices
    shortest_paths = {}

    # Iterate over each query
    for v, u in queries:
        # If the query is for the same vertex, the number of shortest paths is 1
        if v == u:
            shortest_paths[(v, u)] = 1
        # If the query is for two different vertices, calculate the number of shortest paths
        else:
            # Initialize the number of shortest paths to 0
            num_shortest_paths = 0
            # Iterate over each divisor of D
            for divisor in range(1, int(math.sqrt(D)) + 1):
                # If the divisor is a common divisor of v and u, increment the number of shortest paths
                if v % divisor == 0 and u % divisor == 0:
                    num_shortest_paths += 1
            # Add the number of shortest paths to the dictionary
            shortest_paths[(v, u)] = num_shortest_paths

    # Return the number of shortest paths for each query
    return [shortest_paths[(v, u)] for v, u in queries]

