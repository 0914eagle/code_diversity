
import math

def shortest_paths(D, q, queries):
    # Initialize a dictionary to store the number of shortest paths between each pair of vertices
    num_paths = {}

    # Loop through each query
    for v, u in queries:
        # If the query is for the same vertex, the number of shortest paths is 1
        if v == u:
            num_paths[(v, u)] = 1
        # If the query is for two different vertices, calculate the number of shortest paths
        else:
            # Initialize the number of shortest paths to 0
            num_paths[(v, u)] = 0
            # Loop through each divisor of D
            for d in range(1, int(math.sqrt(D)) + 1):
                # If d is a divisor of both v and u, and d is prime, increment the number of shortest paths
                if v % d == 0 and u % d == 0 and math.gcd(d, v) == d and math.gcd(d, u) == d:
                    num_paths[(v, u)] += 1

    # Return the number of shortest paths for each query
    return [num_paths[(v, u)] % 998244353 for v, u in queries]

