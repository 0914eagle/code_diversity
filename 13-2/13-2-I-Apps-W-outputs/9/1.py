
import sys
import math

def get_expected_number_of_passages(n, m, s, t):
    # Initialize the probability of reaching room N from each room
    probabilities = [1 for _ in range(n)]

    # Loop through each passage
    for i in range(m):
        # Get the current passage
        current_s = s[i]
        current_t = t[i]

        # Update the probability of reaching room N from the current passage's start room
        probabilities[current_s-1] += probabilities[current_t-1] / n

    # Return the expected number of passages
    return sum(probabilities)

n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

# Get the expected number of passages for each possible passage blocking
expected_numbers = []
for i in range(m):
    # Block the current passage
    blocked_s = s[:i] + s[i+1:]
    blocked_t = t[:i] + t[i+1:]

    # Get the expected number of passages for the blocked passage
    expected_numbers.append(get_expected_number_of_passages(n, m-1, blocked_s, blocked_t))

# Print the minimum expected number of passages
print(min(expected_numbers))

