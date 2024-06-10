
from collections import defaultdict, deque

def add_edges_to_tree(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    visited[1] = True
    queue = deque([(1, 0)])  # (vertex, distance from vertex 1)
    
    while queue:
        vertex, distance = queue.popleft()
        if distance == 2:
            break
        
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, distance + 1))
    
    return n - sum(visited) + 1

if __name__ == "__main__":
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    
    result = add_edges_to_tree(n, edges)
    print(result)
