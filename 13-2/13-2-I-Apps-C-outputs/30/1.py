
def f1(N, M, doors):
    # Initialize a graph with N nodes
    graph = [[] for _ in range(N)]

    # Add edges to the graph based on the doors
    for u, v in doors:
        graph[u].append(v)
        graph[v].append(u)

    # Find the node with the maximum number of neighbors
    max_neighbors = 0
    node = 0
    for i in range(N):
        if len(graph[i]) > max_neighbors:
            max_neighbors = len(graph[i])
            node = i

    # Return the node with the maximum number of neighbors
    return node

def f2(N, M, doors):
    # Initialize a graph with N nodes
    graph = [[] for _ in range(N)]

    # Add edges to the graph based on the doors
    for u, v in doors:
        graph[u].append(v)
        graph[v].append(u)

    # Find the node with the maximum number of neighbors that are not connected to the outside
    max_neighbors = 0
    node = 0
    for i in range(N):
        neighbors = 0
        for j in graph[i]:
            if j != -1:
                neighbors += 1
        if neighbors > max_neighbors:
            max_neighbors = neighbors
            node = i

    # Return the node with the maximum number of neighbors that are not connected to the outside
    return node

if __name__ == '__main__':
    N, M = map(int, input().split())
    doors = []
    for _ in range(M):
        u, v = map(int, input().split())
        doors.append((u, v))
    print(f2(N, M, doors))

