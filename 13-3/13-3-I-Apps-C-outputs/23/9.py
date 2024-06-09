
def f1(n, m, s, t):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Breadth-first search from s and t to find the shortest path between them
    queue = [(s, [s])]
    visited = set()
    while queue:
        node, path = queue.pop(0)
        if node == t:
            return len(path) - 1
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
    
    return "never meet"

def f2(...):
    # Your code here
    pass

if __name__ == '__main__':
    n, m = map(int, input().split())
    s, t = map(int, input().split())
    print(f1(n, m, s, t))

