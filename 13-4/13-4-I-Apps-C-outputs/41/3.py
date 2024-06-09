
import sys
import itertools

def get_input():
    n = int(input())
    edges = []
    for i in range(n-1):
        a, b = map(int, input().split())
        edges.append((a, b))
    return n, edges

def f1(n, edges):
    # Initialize the graph as a dictionary with keys as vertices and values as lists of neighbors
    graph = {i: [] for i in range(1, n+1)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # Initialize the niceness of each vertex as 0
    niceness = {i: 0 for i in range(1, n+1)}
    
    # Iterate through each vertex and calculate the niceness of each vertex
    for v in range(1, n+1):
        for u in graph[v]:
            if niceness[v] < niceness[u] + 1:
                niceness[v] = niceness[u] + 1
    
    # Return the sum of the niceness of all vertices
    return sum(niceness.values()) % (10**9 + 7)

def f2(n, edges):
    # Initialize the graph as a dictionary with keys as vertices and values as lists of neighbors
    graph = {i: [] for i in range(1, n+1)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # Initialize the niceness of each vertex as 0
    niceness = {i: 0 for i in range(1, n+1)}
    
    # Iterate through each vertex and calculate the niceness of each vertex
    for v in range(1, n+1):
        for u in graph[v]:
            if niceness[v] < niceness[u] + 1:
                niceness[v] = niceness[u] + 1
    
    # Return the sum of the niceness of all vertices
    return sum(niceness.values()) % (10**9 + 7)

if __name__ == '__main__':
    n, edges = get_input()
    print(f1(n, edges))
    print(f2(n, edges))

