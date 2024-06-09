
def get_path_cost(graph, start, end):
    visited = set()
    queue = [(start, 0)]
    while queue:
        node, cost = queue.pop(0)
        if node == end:
            return cost
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node].items():
                queue.append((neighbor, cost | weight))
    return 0

def solve(n, m, roads, q, queries):
    graph = {i: {} for i in range(1, n + 1)}
    for a, b, w in roads:
        graph[a][b] = w
        graph[b][a] = w
    results = []
    for s, t in queries:
        results.append(get_path_cost(graph, s, t))
    return results

if __name__ == '__main__':
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        a, b, w = map(int, input().split())
        roads.append((a, b, w))
    q = int(input())
    queries = []
    for _ in range(q):
        s, t = map(int, input().split())
        queries.append((s, t))
    print(*solve(n, m, roads, q, queries))

