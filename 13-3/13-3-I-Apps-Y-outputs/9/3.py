
def get_maximum_edges(n, edges):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for edge in edges:
        graph[edge[0] - 1].append(edge[1])
        graph[edge[1] - 1].append(edge[0])

    # Initialize the maximum number of edges to 0
    max_edges = 0

    # Initialize the vertices a, b, and c
    a = 1
    b = 2
    c = 3

    # Iterate over all possible combinations of vertices
    for i in range(1, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # If the number of edges in the path between a and b is greater than the current maximum, update the maximum and the vertices
                if len(get_path(graph, a, b, i, j)) > max_edges:
                    max_edges = len(get_path(graph, a, b, i, j))
                    a = i
                    b = j
                    c = k

    return max_edges, a, b, c

def get_path(graph, a, b, c, d):
    # Initialize a set to store the edges in the path
    path = set()

    # If the edge between a and b is in the graph, add it to the path
    if a in graph[b - 1]:
        path.add((a, b))

    # If the edge between b and c is in the graph, add it to the path
    if b in graph[c - 1]:
        path.add((b, c))

    # If the edge between a and c is in the graph, add it to the path
    if a in graph[c - 1]:
        path.add((a, c))

    # If the edge between d and c is in the graph, add it to the path
    if d in graph[c - 1]:
        path.add((d, c))

    return path

if __name__ == '__main__':
    n = int(input())
    edges = []

    for i in range(n - 1):
        edges.append(list(map(int, input().split())))

    max_edges, a, b, c = get_maximum_edges(n, edges)

    print(max_edges)
    print(a, b, c)

