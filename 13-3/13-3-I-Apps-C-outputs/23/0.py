
def f1(n, m, s, t):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Breadth-first search from s and t to find the shortest path between them
    queue = [(s, [s])]
    visited = set([s])
    while queue:
        node, path = queue.pop(0)
        if node == t:
            return len(path)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return -1

def f2(n, m, s, t):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Breadth-first search from s and t to find the shortest path between them
    queue = [(s, [s])]
    visited = set([s])
    while queue:
        node, path = queue.pop(0)
        if node == t:
            return len(path)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return -1

if __name__ == '__main__':
    n, m = map(int, input().split())
    s, t = map(int, input().split())
    print(f1(n, m, s, t))
    print(f2(n, m, s, t))

