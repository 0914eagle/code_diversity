
import math

def solve(n, m, neighbors, s, t):
    # Initialize the probability of meeting at each station
    probabilities = [0] * n
    probabilities[s] = 1
    probabilities[t] = 1

    # Loop through each minute
    for minute in range(1, n * n):
        # Find the current stations of Alice and Bob
        current_stations = [s, t]

        # Check if they are at the same station
        if current_stations[0] == current_stations[1]:
            return minute

        # Update the probabilities of meeting at each station
        for i in range(n):
            if i not in current_stations:
                probabilities[i] = 0
        for i in range(n):
            if i in current_stations:
                probabilities[i] = 1

        # Move Alice and Bob to their neighbouring stations
        s = neighbors[s][0]
        t = neighbors[t][0]

    # They will never meet
    return "never meet"

