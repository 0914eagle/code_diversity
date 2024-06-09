
import sys
import math

def get_input():
    n = int(input())
    edges = []
    for i in range(n-1):
        edges.append(list(map(int, input().split())))
    return n, edges

def paint_graph(n, edges):
    # Initialize the graph as an adjacency list
    graph = [[] for _ in range(n+1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Initialize the niceness of each vertex as 0
    niceness = [0] * (n+1)
    
    # Recursively paint the graph and calculate the niceness
    paint_graph_util(graph, niceness, 1, 1)
    
    # Return the sum of the niceness of all the ways of painting the graph
    return sum(niceness) % (10**9 + 7)

def paint_graph_util(graph, niceness, curr_vertex, color):
    # Base case: if the current vertex is the last vertex, return
    if curr_vertex == len(graph):
        return
    
    # Recursive case: paint the current vertex with the given color and recursively paint the adjacent vertices
    niceness[curr_vertex] = color
    for adjacent_vertex in graph[curr_vertex]:
        if niceness[adjacent_vertex] == 0:
            paint_graph_util(graph, niceness, adjacent_vertex, 3 - color)
    
    # Return the niceness of the current vertex
    return niceness[curr_vertex]

if __name__ == '__main__':
    n, edges = get_input()
    print(paint_graph(n, edges))

