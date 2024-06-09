
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

    # Find the shortest path from A to B using BFS
    queue = [(A, 0)]
    visited = set()
    while queue:
        node, distance = queue.pop(0)
        if node == B:
            return distance
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, distance + 1))

    # If B is not reachable from A, return -1
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

    # Find the shortest path from A to B using DFS
    stack = [(A, 0)]
    visited = set()
    while stack:
        node, distance = stack.pop()
        if node == B:
            return distance
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                stack.append((neighbor, distance + 1))

    # If B is not reachable from A, return -1
    return -1

if __name__ == '__main__':
    n, A, B = map(int, input().split())
    print(f1(n, A, B))
    print(f2(n, A, B))

