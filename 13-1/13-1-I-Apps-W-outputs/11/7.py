
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

    # Print the expected holeyness modulo 10^9 + 7
    print(int(expected_holeyness * (10**9 + 7)))

if __name__ == '__main__':
    N = int(input())
    edges = []
    for _ in range(N):
        edges.append(list(map(int, input().split())))
    solve(N, edges)

