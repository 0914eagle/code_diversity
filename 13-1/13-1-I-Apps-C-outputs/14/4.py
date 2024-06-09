
def f1(N, L):
    # Initialize a graph with N nodes and no edges
    graph = [[] for _ in range(N + 1)]

    # Add edges to the graph
    for i in range(1, N):
        for j in range(1, N):
            if a[i][j] > 0:
                graph[i].append(j)

    # Breadth-first search from node 1 to node N
    queue = [1]
    visited = set()
    while queue:
        node = queue.pop(0)
        if node == N:
            return L
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return -1

def f2(...):
    ...

if __name__ == '__main__':
    N, L = map(int, input().split())
    a = []
    for _ in range(N):
        a.append(list(map(int, input().split())))
    print(f1(N, L))

