
import sys
import math

def get_input():
    N = int(input())
    edges = []
    for i in range(N-1):
        a, b = map(int, input().split())
        edges.append((a, b))
    return N, edges

def f1(N, edges):
    # Initialize the graph as an adjacency list
    graph = [[] for _ in range(N+1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # Initialize the niceness of each vertex as 0
    niceness = [0] * (N+1)
    
    # Recursively compute the niceness of each vertex
    def compute_niceness(vertex, color):
        if niceness[vertex] != 0:
            return niceness[vertex]
        niceness[vertex] = color
        for neighbor in graph[vertex]:
            compute_niceness(neighbor, 1 - color)
        return niceness[vertex]
    
    # Compute the niceness of each vertex and return the sum
    return sum(compute_niceness(vertex, 0) for vertex in range(1, N+1)) % (10**9 + 7)

def f2(N, edges):
    # Initialize the graph as an adjacency list
    graph = [[] for _ in range(N+1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # Initialize the niceness of each vertex as 0
    niceness = [0] * (N+1)
    
    # Recursively compute the niceness of each vertex
    def compute_niceness(vertex, color):
        if niceness[vertex] != 0:
            return niceness[vertex]
        niceness[vertex] = color
        for neighbor in graph[vertex]:
            compute_niceness(neighbor, 1 - color)
        return niceness[vertex]
    
    # Compute the niceness of each vertex and return the sum
    return sum(compute_niceness(vertex, 0) for vertex in range(1, N+1)) % (10**9 + 7)

if __name__ == '__main__':
    N, edges = get_input()
    print(f1(N, edges))
    print(f2(N, edges))

