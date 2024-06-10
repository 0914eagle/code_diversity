
from collections import defaultdict, deque

def add_min_edges_to_satisfy_condition(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    visited[1] = True

    q = deque([1])
    level = 0
    while q:
        level += 1
        size = len(q)
        for _ in range(size):
            node = q.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)

    return n - sum(visited)

if __name__ == "__main__":
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    print(add_min_edges_to_satisfy_condition(n, edges))
