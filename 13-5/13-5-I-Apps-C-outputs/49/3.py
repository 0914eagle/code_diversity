
def get_minimum_path_length(n, m, roads):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for u, v in roads:
        graph[u - 1].append(v - 1)
    
    # Find all maximum length paths in the graph
    paths = []
    for i in range(n):
        path = []
        dfs(graph, i, path)
        paths.append(path)
    
    # Find the minimum length path that a winning racer would take if at most one of the roads is blocked off
    min_length = float('inf')
    for path in paths:
        length = len(path)
        for i in range(n):
            for j in range(i + 1, n):
                if (i, j) in roads or (j, i) in roads:
                    length -= 1
        min_length = min(min_length, length)
    
    return min_length

def dfs(graph, node, path):
    path.append(node)
    for neighbor in graph[node]:
        if neighbor not in path:
            dfs(graph, neighbor, path)

if __name__ == '__main__':
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        u, v = map(int, input().split())
        roads.append((u, v))
    print(get_minimum_path_length(n, m, roads))

