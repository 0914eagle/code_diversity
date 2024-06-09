
def f1(n, A, B):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the input
    for i in range(n):
        l, r, t = map(int, input().split())
        if l != -1:
            graph[i].append(l)
        if r != -1:
            graph[i].append(r)

    # Find the shortest path from A to B
    visited = [False] * n
    queue = [(A, 0)]
    while queue:
        node, distance = queue.pop(0)
        if node == B:
            return distance
        if visited[node]:
            continue
        visited[node] = True
        for neighbor in graph[node]:
            queue.append((neighbor, distance + 1))

    # If there is no path from A to B, return -1
    return -1

def f2(n, A, B):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the input
    for i in range(n):
        l, r, t = map(int, input().split())
        if l != -1:
            graph[i].append(l)
        if r != -1:
            graph[i].append(r)

    # Find the shortest path from A to B
    visited = [False] * n
    queue = [(A, 0)]
    while queue:
        node, distance = queue.pop(0)
        if node == B:
            return distance
        if visited[node]:
            continue
        visited[node] = True
        for neighbor in graph[node]:
            queue.append((neighbor, distance + 1))

    # If there is no path from A to B, return -1
    return -1

if __name__ == '__main__':
    n, A, B = map(int, input().split())
    print(f1(n, A, B))
    print(f2(n, A, B))

