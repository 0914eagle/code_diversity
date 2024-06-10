
def get_diameter(n, m, edges):
    # Create a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for i in range(m):
        graph[edges[i][0] - 1].append(edges[i][1] - 1)
        graph[edges[i][1] - 1].append(edges[i][0] - 1)

    # Find the diameter of the graph
    diameter = 0
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] == 1:
                diameter = max(diameter, 2)
            else:
                diameter = max(diameter, bfs(graph, i, j))

    return diameter

def bfs(graph, start, end):
    queue = [start]
    visited = [False] * len(graph)
    visited[start] = True

    while queue:
        vertex = queue.pop(0)
        if vertex == end:
            return 2
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

    return 0

def add_edges(n, m, edges):
    # Create a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for i in range(m):
        graph[edges[i][0] - 1].append(edges[i][1] - 1)
        graph[edges[i][1] - 1].append(edges[i][0] - 1)

    # Find the diameter of the graph
    diameter = get_diameter(n, m, edges)

    # Add edges to the graph to make it a tree
    added_edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] == 0 and bfs(graph, i, j) == 2:
                added_edges.append([i + 1, j + 1])
                graph[i][j] = 1
                graph[j][i] = 1
                diameter = get_diameter(n, m + 1, edges + added_edges)

    return diameter, added_edges

def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    diameter, added_edges = add_edges(n, m, edges)
    print(diameter)
    for edge in added_edges:
        print(*edge)

if __name__ == '__main__':
    main()

