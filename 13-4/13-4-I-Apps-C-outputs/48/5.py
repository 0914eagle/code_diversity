
import sys

def get_input():
    N = int(input())
    edges = []
    for _ in range(N - 1):
        x, y = map(int, input().split())
        edges.append((x, y))
    return N, edges

def f1(N, edges):
    # Initialize a dictionary to store the pairs of vertices
    pairs = {}
    # Iterate through the edges and add them to the dictionary
    for edge in edges:
        pairs[edge] = pairs.get(edge, 0) + 1
    # Initialize a set to store the vertices that are not in any pair
    unpaired = set(range(1, N + 1))
    # Iterate through the pairs and remove the vertices that are in a pair
    for pair in pairs:
        unpaired.remove(pair[0])
        unpaired.remove(pair[1])
    # Return the number of ways to divide the vertices into pairs
    return len(pairs) * (N - len(unpaired))

def f2(N, edges):
    # Initialize a dictionary to store the pairs of vertices
    pairs = {}
    # Iterate through the edges and add them to the dictionary
    for edge in edges:
        pairs[edge] = pairs.get(edge, 0) + 1
    # Initialize a set to store the vertices that are not in any pair
    unpaired = set(range(1, N + 1))
    # Iterate through the pairs and remove the vertices that are in a pair
    for pair in pairs:
        unpaired.remove(pair[0])
        unpaired.remove(pair[1])
    # Return the number of ways to divide the vertices into pairs
    return len(pairs) * (N - len(unpaired)) % (10**9 + 7)

if __name__ == '__main__':
    N, edges = get_input()
    print(f2(N, edges))

