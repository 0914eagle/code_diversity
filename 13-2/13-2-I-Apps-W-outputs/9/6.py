
import sys
import math

def get_expected_number_of_passages(n, m, s, t):
    # Initialize the probability of reaching room N from each room
    probabilities = [1 for _ in range(n)]

    # Loop through each passage
    for i in range(m):
        # Get the source and destination rooms of the passage
        source = s[i]
        destination = t[i]

        # Update the probability of reaching room N from the source room
        probabilities[source-1] *= 1 / (destination - source + 1)

        # Update the probability of reaching room N from the destination room
        probabilities[destination-1] += probabilities[source-1] * (destination - source) / (destination - source + 1)

    # Return the expected number of passages
    return sum(probabilities)

n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

# Get the expected number of passages when Aoki blocks the passage from Room 1 to Room 2
expected_number_of_passages = get_expected_number_of_passages(n, m-1, s[1:], t[1:])

# Print the expected number of passages
print(expected_number_of_passages)

