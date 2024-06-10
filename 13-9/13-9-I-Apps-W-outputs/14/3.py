
def get_input():
    n, m = map(int, input().split())
    roads = []
    for i in range(m):
        a, b, d = map(int, input().split())
        roads.append((a, b, d))
    return n, m, roads

def find_shortest_path(n, m, roads):
    # Create a graph with the given roads
    graph = [[] for _ in range(n)]
    for a, b, d in roads:
        graph[a].append((b, d))
        graph[b].append((a, d))
    
    # Find the shortest path from Delft (0) to Amsterdam (1)
    visited = [False] * n
    queue = [(0, 0, [0])]
    while queue:
        node, distance, path = queue.pop(0)
        if node == 1:
            return path
        visited[node] = True
        for neighbor, d in graph[node]:
            if not visited[neighbor]:
                queue.append((neighbor, distance + d, path + [neighbor]))
    
    return []

def solve(n, m, roads):
    path = find_shortest_path(n, m, roads)
    if not path:
        return "impossible"
    return str(len(path)) + " " + " ".join(map(str, path))

if __name__ == '__main__':
    n, m, roads = get_input()
    print(solve(n, m, roads))

