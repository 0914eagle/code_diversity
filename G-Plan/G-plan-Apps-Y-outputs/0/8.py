
from collections import defaultdict, deque

def add_edges_to_satisfy_condition(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    visited[1] = True
    queue = deque([1])
    level = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        level += 1
        if level == 2:
            break
    
    return n - sum(visited)

if __name__ == "__main__":
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    result = add_edges_to_satisfy_condition(n, edges)
    print(result)
