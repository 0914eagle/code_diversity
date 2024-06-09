
import math

def solve(n, m, edges, s, t):
    # Initialize the probability of meeting at each station
    prob = [0] * n
    prob[s] = 1
    prob[t] = 1

    # Loop until the probability of meeting at each station is the same
    while True:
        # Calculate the probability of meeting at each neighboring station
        for i in range(n):
            for j in range(n):
                if i != j and edges[i][j] == 1:
                    prob[i] += prob[j] / (n - 1)

        # Check if the probability of meeting at each station is the same
        if all(prob[i] == prob[0] for i in range(1, n)):
            break

    # Return the expected time of meeting
    return sum(i * prob[i] for i in range(n))

