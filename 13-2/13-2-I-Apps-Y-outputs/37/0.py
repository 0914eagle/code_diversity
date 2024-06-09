
def f1(n, k, art_installation):
    # Initialize a graph with n*n nodes
    graph = [[] for _ in range(n*n)]

    # Populate the graph with edges
    for i in range(n):
        for j in range(n):
            tile = art_installation[i][j]
            if tile != 0:
                graph[tile-1].append((i, j))

    # Find the shortest path from node 0 to node k-1
    visited = [False] * n*n
    queue = [(0, 0, 0)]
    while queue:
        node, dist, parent = queue.pop(0)
        if node == k-1:
            return dist
        if visited[node]:
            continue
        visited[node] = True
        for neighbor in graph[node]:
            queue.append((neighbor[0]*n + neighbor[1], dist+1, node))

    return -1

def f2(n, k, art_installation):
    # Initialize a graph with n*n nodes
    graph = [[] for _ in range(n*n)]

    # Populate the graph with edges
    for i in range(n):
        for j in range(n):
            tile = art_installation[i][j]
            if tile != 0:
                graph[tile-1].append((i, j))

    # Find the shortest path from node 0 to node k-1
    visited = [False] * n*n
    queue = [(0, 0, 0)]
    while queue:
        node, dist, parent = queue.pop(0)
        if node == k-1:
            return dist
        if visited[node]:
            continue
        visited[node] = True
        for neighbor in graph[node]:
            queue.append((neighbor[0]*n + neighbor[1], dist+1, node))

    return -1

if __name__ == '__main__':
    n, k = map(int, input().split())
    art_installation = []
    for _ in range(n):
        art_installation.append(list(map(int, input().split())))
    print(f1(n, k, art_installation))
    print(f2(n, k, art_installation))

