
def f1(n, edges):
    # Initialize the graph with N vertices and no edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    # Find the shortest path between every pair of vertices
    shortest_paths = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                shortest_paths[i][j] = bfs(graph, i, j)

    # Divide the vertices into pairs and check if the condition is satisfied
    pairs = []
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            pair = [i, j]
            for k in range(n):
                if k not in pair:
                    if shortest_paths[pair[0]][k] == 0 or shortest_paths[pair[1]][k] == 0:
                        break
            else:
                pairs.append(pair)

    return len(pairs) % (10**9 + 7)

def bfs(graph, start, end):
    queue = [start]
    visited = set([start])
    while queue:
        vertex = queue.pop(0)
        if vertex == end:
            return len(visited) - 1
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return 0

def f2(n, edges):
    # Initialize the graph with N vertices and no edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    # Find the shortest path between every pair of vertices
    shortest_paths = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                shortest_paths[i][j] = bfs(graph, i, j)

    # Divide the vertices into pairs and check if the condition is satisfied
    pairs = []
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            pair = [i, j]
            for k in range(n):
                if k not in pair:
                    if shortest_paths[pair[0]][k] == 0 or shortest_paths[pair[1]][k] == 0:
                        break
            else:
                pairs.append(pair)

    return len(pairs) % (10**9 + 7)

if __name__ == '__main__':
    n = int(input())
    edges = []
    for _ in range(n - 1):
        edges.append(list(map(int, input().split())))
    print(f1(n, edges))
    print(f2(n, edges))

