
import sys
import itertools

def get_input():
    n = int(input())
    edges = []
    for _ in range(n-1):
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
    
    # Compute the niceness of each vertex
    for vertex in range(1, n+1):
        # If the vertex is white, compute the niceness as the maximum distance to a black vertex
        if niceness[vertex] == 0:
            niceness[vertex] = max(get_distance(graph, vertex, black_vertex) for black_vertex in range(1, n+1) if niceness[black_vertex] == 1)
        # If the vertex is black, compute the niceness as the maximum distance to a white vertex
        else:
            niceness[vertex] = max(get_distance(graph, vertex, white_vertex) for white_vertex in range(1, n+1) if niceness[white_vertex] == 0)
    
    # Return the sum of the nicenesses
    return sum(niceness) % (10**9 + 7)

def get_distance(graph, start, end):
    # Initialize the distance of the start vertex as 0
    distance = {start: 0}
    
    # Initialize the queue with the start vertex
    queue = [start]
    
    # Breadth-first search to find the shortest distance from the start vertex to the end vertex
    while queue:
        current = queue.pop(0)
        if current == end:
            return distance[current]
        for neighbor in graph[current]:
            if neighbor not in distance:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
    
    # If the end vertex is not found, return -1
    return -1

def f2(n, edges):
    # Initialize the graph as an adjacency list
    graph = [[] for _ in range(n+1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Initialize the niceness of each vertex as 0
    niceness = [0] * (n+1)
    
    # Compute the niceness of each vertex
    for vertex in range(1, n+1):
        # If the vertex is white, compute the niceness as the maximum distance to a black vertex
        if niceness[vertex] == 0:
            niceness[vertex] = max(get_distance(graph, vertex, black_vertex) for black_vertex in range(1, n+1) if niceness[black_vertex] == 1)
        # If the vertex is black, compute the niceness as the maximum distance to a white vertex
        else:
            niceness[vertex] = max(get_distance(graph, vertex, white_vertex) for white_vertex in range(1, n+1) if niceness[white_vertex] == 0)
    
    # Return the sum of the nicenesses
    return sum(niceness) % (10**9 + 7)

def main():
    n, edges = get_input()
    print(f1(n, edges))
    print(f2(n, edges))

if __name__ == '__main__':
    main()

