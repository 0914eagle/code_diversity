
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

        # Update the probability of reaching room N from the current room
        probabilities[current_s-1] *= 1 / (current_t - current_s + 1)

    # Calculate the expected number of passages
    expected_number_of_passages = 0
    for probability in probabilities:
        expected_number_of_passages += probability

    return expected_number_of_passages

n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

# Find the minimum expected number of passages by trying all possible passage combinations
min_expected_number_of_passages = math.inf
for i in range(m):
    # Block the current passage
    blocked_s = s[i]
    blocked_t = t[i]
    s.pop(i)
    t.pop(i)
    m -= 1

    # Calculate the expected number of passages
    expected_number_of_passages = get_expected_number_of_passages(n, m, s, t)

    # Restore the passage
    s.insert(i, blocked_s)
    t.insert(i, blocked_t)
    m += 1

    # Update the minimum expected number of passages
    if expected_number_of_passages < min_expected_number_of_passages:
        min_expected_number_of_passages = expected_number_of_passages

# Print the minimum expected number of passages
print(min_expected_number_of_passages)

