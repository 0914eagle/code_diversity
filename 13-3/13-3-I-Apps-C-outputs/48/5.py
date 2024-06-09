
import math

def f1(N, M, nodes, edges):
    # Initialize variables
    turning_required = 0
    visited = [False] * N
    visited[0] = True
    queue = [0]

    # Breadth-first search to find Eulerian circuit
    while queue:
        node = queue.pop(0)
        for edge in edges:
            if edge[0] == node and not visited[edge[1]]:
                visited[edge[1]] = True
                queue.append(edge[1])
                turning_required += math.pi

    # Calculate total turning required
    for i in range(N):
        for j in range(i+1, N):
            if not visited[i] or not visited[j]:
                turning_required += math.pi

    return turning_required

def f2(N, M, nodes, edges):
    # Initialize variables
    turning_required = 0
    visited = [False] * N
    visited[0] = True
    queue = [0]

    # Breadth-first search to find Eulerian circuit
    while queue:
        node = queue.pop(0)
        for edge in edges:
            if edge[0] == node and not visited[edge[1]]:
                visited[edge[1]] = True
                queue.append(edge[1])
                turning_required += math.pi

    # Calculate total turning required
    for i in range(N):
        for j in range(i+1, N):
            if not visited[i] or not visited[j]:
                turning_required += math.pi

    return turning_required

if __name__ == '__main__':
    N, M = map(int, input().split())
    nodes = []
    edges = []
    for i in range(N):
        x, y = map(int, input().split())
        nodes.append((x, y))
    for i in range(M):
        a, b = map(int, input().split())
        edges.append((a, b))
    print(f1(N, M, nodes, edges))
    print(f2(N, M, nodes, edges))

