
def find_diameter(n, edges):
    adj_list = {i: [] for i in range(1, n+1)}
    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    def bfs(start):
        visited = [False] * (n+1)
        dist = [-1] * (n+1)
        queue = [(start, 0)]
        visited[start] = True
        max_dist = 0
        max_node = start
        
        while queue:
            node, d = queue.pop(0)
            if d > max_dist:
                max_dist = d
                max_node = node
            
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dist[neighbor] = d + 1
                    queue.append((neighbor, d + 1))
        
        return max_node, max_dist
    
    farthest_node, _ = bfs(1)
    _, diameter = bfs(farthest_node)
    
    return diameter

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

if m == n - 1:
    print(find_diameter(n, edges))
else:
    print(2)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if i not in adj_list[j]:
                print(i, j)
                break
