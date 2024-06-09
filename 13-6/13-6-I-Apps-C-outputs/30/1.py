
def get_cost(graph, s, t):
    # Use BFS to find the shortest path between s and t
    queue = [(s, 0)]
    visited = set()
    while queue:
        node, cost = queue.pop(0)
        if node == t:
            return cost
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                queue.append((neighbor, cost + weight))
    return -1

def solve(n, m, edges, q, queries):
    # Create a graph with the given edges
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # Solve the queries
    result = []
    for s, t in queries:
        result.append(get_cost(graph, s, t))
    
    return result

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    q = int(input())
    queries = []
    for _ in range(q):
        s, t = map(int, input().split())
        queries.append((s, t))
    result = solve(n, m, edges, q, queries)
    for cost in result:
        print(cost)

