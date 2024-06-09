
import sys
import math

def get_input():
    n = int(input())
    edges = []
    for i in range(n-1):
        edges.append(list(map(int, input().split())))
    return n, edges

def paint_graph(n, edges):
    # Initialize the graph with all vertices white
    graph = [0] * (n+1)

    # Paint the first vertex black
    graph[1] = 1

    # Iterate through the edges and paint the adjacent vertices
    for i in range(n-1):
        a, b = edges[i]
        graph[a] = 1 - graph[a]
        graph[b] = 1 - graph[b]

    # Return the niceness of the graph
    return get_niceness(graph)

def get_niceness(graph):
    # Initialize the niceness to 0
    niceness = 0

    # Iterate through the graph and calculate the maximum distance between white and black vertices
    for i in range(1, len(graph)):
        if graph[i] == 0:
            continue
        for j in range(i+1, len(graph)):
            if graph[j] == graph[i]:
                continue
            niceness = max(niceness, abs(i-j))

    # Return the niceness
    return niceness

def main():
    n, edges = get_input()
    print(paint_graph(n, edges))

if __name__ == '__main__':
    main()

