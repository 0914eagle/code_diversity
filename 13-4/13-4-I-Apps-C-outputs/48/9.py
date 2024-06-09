
import sys

def f1(n, edges):
    # Calculate the number of pairs that contain each vertex
    pairs = [0] * (n + 1)
    for edge in edges:
        pairs[edge[0]] += 1
        pairs[edge[1]] += 1

    # Calculate the number of pairs that are connected by an edge
    connected_pairs = 0
    for i in range(1, n + 1):
        if pairs[i] == 2:
            connected_pairs += 1

    # Calculate the number of ways to divide the vertices into pairs
    ways = 1
    for i in range(1, n + 1):
        if pairs[i] == 1:
            ways *= connected_pairs
        else:
            ways *= connected_pairs - 1

    return ways % (10**9 + 7)

def f2(n, edges):
    # Calculate the number of pairs that contain each vertex
    pairs = [0] * (n + 1)
    for edge in edges:
        pairs[edge[0]] += 1
        pairs[edge[1]] += 1

    # Calculate the number of pairs that are connected by an edge
    connected_pairs = 0
    for i in range(1, n + 1):
        if pairs[i] == 2:
            connected_pairs += 1

    # Calculate the number of ways to divide the vertices into pairs
    ways = 1
    for i in range(1, n + 1):
        if pairs[i] == 1:
            ways *= connected_pairs
        else:
            ways *= connected_pairs - 1

    return ways % (10**9 + 7)

if __name__ == '__main__':
    n = int(input())
    edges = []
    for i in range(n - 1):
        x, y = map(int, input().split())
        edges.append((x, y))
    print(f1(n, edges))
    print(f2(n, edges))

