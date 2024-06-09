
import sys

def get_input():
    N = int(input())
    edges = []
    for i in range(N - 1):
        x, y = map(int, input().split())
        edges.append((x, y))
    return N, edges

def f1(N, edges):
    # Initialize the number of ways to divide the vertices into pairs as 0
    ways = 0
    # Loop through each edge
    for edge in edges:
        # If the edge is not part of a cycle, increment the number of ways
        if edge[0] != edge[1]:
            ways += 1
    return ways

def f2(N, edges):
    # Initialize the number of ways to divide the vertices into pairs as 0
    ways = 0
    # Loop through each edge
    for edge in edges:
        # If the edge is part of a cycle, increment the number of ways
        if edge[0] == edge[1]:
            ways += 1
    return ways

if __name__ == '__main__':
    N, edges = get_input()
    print(f2(N, edges))

