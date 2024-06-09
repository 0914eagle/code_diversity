
import math

def solve(D, q, queries):
    # Initialize a dictionary to store the number of shortest paths between each pair of vertices
    num_paths = {}

    # Iterate over each query
    for v, u in queries:
        # If the query is for the same vertex, the number of shortest paths is 1
        if v == u:
            num_paths[(v, u)] = 1
            continue

        # If the query has already been processed, return the cached result
        if (v, u) in num_paths:
            continue

        # Initialize the number of shortest paths to 0
        num_paths[(v, u)] = 0

        # Iterate over each divisor of D
        for d in range(1, int(math.sqrt(D)) + 1):
            # If d is not a divisor of v or u, skip it
            if v % d != 0 or u % d != 0:
                continue

            # If d is a divisor of both v and u, increment the number of shortest paths
            num_paths[(v, u)] += 1

        # Print the number of shortest paths modulo 998244353
        print(num_paths[(v, u)] % 998244353)

    return num_paths

