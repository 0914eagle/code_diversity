
import sys
import math

def f1(N, edges):
    # Calculate the number of pairs
    num_pairs = N // 2
    
    # Create a graph with N vertices and N-1 edges
    graph = [[] for _ in range(N)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)
    
    # Initialize the number of ways to divide the vertices into pairs
    num_ways = 0
    
    # Iterate over all possible pairs
    for i in range(num_pairs):
        for j in range(i + 1, num_pairs):
            # Check if there is a path between the two vertices in the pair
            if bfs(graph, i, j):
                num_ways += 1
    
    return num_ways % (10**9 + 7)

def bfs(graph, start, end):
    # Initialize the queue with the start vertex
    queue = [start]
    
    # Initialize the visited array with False values
    visited = [False] * len(graph)
    
    # Mark the start vertex as visited
    visited[start] = True
    
    # Loop until the queue is empty
    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.pop(0)
        
        # If the vertex is the end vertex, return True
        if vertex == end:
            return True
        
        # Iterate over the neighbors of the vertex
        for neighbor in graph[vertex]:
            # If the neighbor has not been visited, mark it as visited and enqueue it
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    # If the end vertex has not been visited, return False
    return False

def f2(N, edges):
    # Calculate the number of pairs
    num_pairs = N // 2
    
    # Create a graph with N vertices and N-1 edges
    graph = [[] for _ in range(N)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)
    
    # Initialize the number of ways to divide the vertices into pairs
    num_ways = 0
    
    # Iterate over all possible pairs
    for i in range(num_pairs):
        for j in range(i + 1, num_pairs):
            # Check if there is a path between the two vertices in the pair
            if dfs(graph, i, j):
                num_ways += 1
    
    return num_ways % (10**9 + 7)

def dfs(graph, start, end):
    # Initialize the visited array with False values
    visited = [False] * len(graph)
    
    # Mark the start vertex as visited
    visited[start] = True
    
    # Recursive function to search for a path between the start and end vertices
    def search(vertex):
        # If the vertex is the end vertex, return True
        if vertex == end:
            return True
        
        # Iterate over the neighbors of the vertex
        for neighbor in graph[vertex]:
            # If the neighbor has not been visited, mark it as visited and search for a path
            if not visited[neighbor]:
                visited[neighbor] = True
                if search(neighbor):
                    return True
        
        # If no path was found, return False
        return False
    
    # Search for a path between the start and end vertices
    return search(start)

if __name__ == '__main__':
    N = int(input())
    edges = []
    for _ in range(N - 1):
        edges.append(list(map(int, input().split())))
    print(f1(N, edges))
    print(f2(N, edges))

