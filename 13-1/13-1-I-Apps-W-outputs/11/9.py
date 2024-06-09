
import math

def solve(N, edges):
    # Initialize the probability of each vertex being black as 0.5
    probabilities = [0.5] * (N + 1)

    # Iterate over the edges and update the probability of the vertices
    for edge in edges:
        probabilities[edge[0]] *= probabilities[edge[1]]
        probabilities[edge[1]] *= probabilities[edge[0]]

    # Calculate the expected holeyness of the subtree
    expected_holeyness = 0
    for i in range(1, N + 1):
        expected_holeyness += probabilities[i] * (1 - probabilities[i])

    # Calculate the modular inverse of 8 and multiply it with the expected holeyness
    modular_inverse = math.pow(8, math.floor(math.log(1000000007, 8)) + 1, 1000000007)
    expected_holeyness = (expected_holeyness * modular_inverse) % 1000000007

    return expected_holeyness

