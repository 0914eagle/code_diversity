
import sys
import math

def get_input():
    n = int(input())
    edges = []
    for i in range(n-1):
        edges.append(list(map(int, input().split())))
    return n, edges

def f1(n, edges):
    # Initialize the graph as an adjacency list
    graph = [[] for _ in range(n+1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Initialize the niceness of each vertex as 0
    niceness = [0] * (n+1)
    
    # Recursively compute the niceness of each vertex
    def dfs(vertex, parent, color):
        nonlocal niceness
        niceness[vertex] = color
        for neighbor in graph[vertex]:
            if neighbor != parent and niceness[neighbor] == 0:
                dfs(neighbor, vertex, 1-color)
    
    dfs(1, 0, 0)
    
    # Return the sum of the niceness of all vertices
    return sum(niceness) % (10**9 + 7)

def f2(n, edges):
    # Initialize the graph as an adjacency list
    graph = [[] for _ in range(n+1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Initialize the niceness of each vertex as 0
    niceness = [0] * (n+1)
    
    # Recursively compute the niceness of each vertex
    def dfs(vertex, parent, color):
        nonlocal niceness
        niceness[vertex] = color
        for neighbor in graph[vertex]:
            if neighbor != parent and niceness[neighbor] == 0:
                dfs(neighbor, vertex, 1-color)
    
    dfs(1, 0, 0)
    
    # Return the sum of the niceness of all vertices
    return sum(niceness) % (10**9 + 7)

if __name__ == '__main__':
    n, edges = get_input()
    print(f1(n, edges))
    print(f2(n, edges))

