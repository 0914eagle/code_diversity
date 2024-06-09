
import math

def solve(n, m, neighbors, s, t):
    # Initialize the probability of meeting at each station
    probabilities = [0] * n
    probabilities[s] = 1
    probabilities[t] = 1

    # Loop through each minute
    for minute in range(1, 60):
        # Find the stations that are neighbors to the current stations
        current_neighbors = set()
        for u, v in neighbors:
            if u == s or v == s:
                current_neighbors.add(v)
            if u == t or v == t:
                current_neighbors.add(u)

        # Update the probabilities of meeting at each station
        for i in range(n):
            if i not in current_neighbors:
                probabilities[i] = 0
            else:
                probabilities[i] = (probabilities[i] + probabilities[min(s, t)]) / 2

        # Check if they will meet at the same station
        if probabilities[s] > 0 and probabilities[t] > 0:
            return minute

        # Update the current stations
        s = min(s, t)
        t = max(s, t)

    # They will never meet
    return "never meet"

