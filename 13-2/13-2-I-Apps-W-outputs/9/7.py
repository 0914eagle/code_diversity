
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
        probabilities[current_s-1] *= 1 / (current_t - current_s + 1)

        # Update the probability of reaching room N from the current passage's end room
        probabilities[current_t-1] *= 1 / (current_t - current_s + 1)

    # Calculate the expected number of passages
    expected_number_of_passages = 0
    for probability in probabilities:
        expected_number_of_passages += probability

    return expected_number_of_passages

n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

# Get the expected number of passages when Aoki blocks the passage from Room 1 to Room 2
expected_number_of_passages = get_expected_number_of_passages(n, m, s, t)

# Print the expected number of passages
print(expected_number_of_passages)

