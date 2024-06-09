
import math

def solve(n, m, edges, s, t):
    # Initialize the probability matrix
    prob = [[0] * n for _ in range(n)]

    # Set the initial probability of being at the same station to 1
    prob[s][t] = 1

    # Loop through each minute
    for i in range(1, n):
        # Loop through each station
        for u in range(n):
            # Loop through each neighbouring station
            for v in range(n):
                # Check if u and v are neighbours
                if edges[u][v] == 1:
                    # Add the probability of being at the same station from the previous minute
                    prob[u][v] += prob[u][v]

                    # Add the probability of being at the same station from the previous minute
                    prob[v][u] += prob[u][v]

    # Calculate the expected time to meet
    expected_time = 0
    for u in range(n):
        for v in range(n):
            if edges[u][v] == 1:
                expected_time += prob[u][v] * (i + 1)

    return expected_time

