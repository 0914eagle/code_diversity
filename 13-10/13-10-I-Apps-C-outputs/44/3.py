
import sys

def world_to_graph(n):
    # Create an empty graph with n vertices and no edges
    graph = {i: set() for i in range(n)}
    return graph

def add_edge(graph, u, v):
    # Add an edge between vertices u and v in the graph
    graph[u].add(v)
    graph[v].add(u)

def remove_edge(graph, u, v):
    # Remove the edge between vertices u and v in the graph
    graph[u].remove(v)
    graph[v].remove(u)

def add_vertex(graph, w):
    # Add a new vertex w to the graph
    graph[w] = set()

def add_edge_between(graph, u, v, w):
    # Add edges between vertices u, v, and w in the graph
    add_edge(graph, u, w)
    add_edge(graph, v, w)

def count_similar_worlds(graph, n, m):
    # Count the number of non-similar worlds that can be built under the constraints
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if graph[i][j] and graph[j][k] and graph[k][i]:
                    count += 1
    return count % (10**9 + 7)

def main():
    n, m = map(int, input().split())
    graph = world_to_graph(2)
    add_edge(graph, 0, 1)
    for _ in range(n-1):
        w = len(graph)
        add_vertex(graph, w)
        for u in range(w):
            for v in range(u+1, w):
                if graph[u][v]:
                    add_edge_between(graph, u, v, w)
    print(count_similar_worlds(graph, w+1, m))

if __name__ == '__main__':
    main()

