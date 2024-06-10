
from collections import defaultdict, deque

def add_edges_to_satisfy_condition(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    visited[1] = True
    queue = deque([1])
    level2_vertices = set()

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                for next_neighbor in graph[neighbor]:
                    if not visited[next_neighbor]:
                        level2_vertices.add(next_neighbor)

    return n - len(level2_vertices) - 1

if __name__ == "__main__":
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    print(add_edges_to_satisfy_condition(n, edges))
