
def f1(n, A, B):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the input
    for i in range(n):
        l, r, t = map(int, input().split())
        if l != -1:
            graph[i].append(l)
        if r != -1:
            graph[i].append(r)

    # Breadth-first search from both starting points to find the shortest path to the tower
    queue = [(A, 0)]
    visited = set()
    while queue:
        node, dist = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if t[node] == 1:
                return dist
            for neighbor in graph[node]:
                queue.append((neighbor, dist + 1))

    return -1

def f2(n, A, B):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the input
    for i in range(n):
        l, r, t = map(int, input().split())
        if l != -1:
            graph[i].append(l)
        if r != -1:
            graph[i].append(r)

    # Breadth-first search from both starting points to find the shortest path to the tower
    queue = [(A, 0)]
    visited = set()
    while queue:
        node, dist = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if t[node] == 1:
                return dist
            for neighbor in graph[node]:
                queue.append((neighbor, dist + 1))

    return -1

if __name__ == '__main__':
    n, A, B = map(int, input().split())
    t = [int(input()) for _ in range(n)]
    print(f1(n, A, B))
    print(f2(n, A, B))

