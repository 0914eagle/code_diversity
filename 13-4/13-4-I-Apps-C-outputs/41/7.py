
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
    
    # DFS to find the distances between white and black vertices
    white_distances = [0] * (n+1)
    black_distances = [0] * (n+1)
    visited = [False] * (n+1)
    def dfs(node, parent, distance, is_white):
        visited[node] = True
        if is_white:
            white_distances[node] = distance
        else:
            black_distances[node] = distance
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, node, distance+1, not is_white)
    
    # DFS starting from each vertex to find the niceness of each way of painting the graph
    niceness = [0] * (2**n)
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i, -1, 0, True)
        for j in range(i+1, n+1):
            if not visited[j]:
                dfs(j, -1, 0, False)
        for k in range(2**n):
            niceness[k] += max(white_distances[i] + white_distances[j], black_distances[i] + black_distances[j])
    
    return niceness

def f2(niceness):
    # Modular arithmetic to avoid overflow
    mod = 10**9 + 7
    result = 0
    for i in range(len(niceness)):
        result += niceness[i]
        result %= mod
    
    return result

if __name__ == '__main__':
    n, edges = get_input()
    niceness = f1(n, edges)
    print(f2(niceness))

