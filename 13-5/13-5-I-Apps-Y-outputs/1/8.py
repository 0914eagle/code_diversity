
def read_data():
    n, m = map(int, input().split())
    edges = []
    for i in range(n - 1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    queries = list(map(int, input().split()))
    return n, m, edges, queries

def build_graph(edges):
    graph = {}
    for u, v, w in edges:
        if u not in graph:
            graph[u] = {}
        graph[u][v] = w
    return graph

def dfs(graph, u, visited, parent, max_weight):
    if u in visited:
        return
    visited.add(u)
    for v in graph[u]:
        if v != parent and graph[u][v] <= max_weight:
            dfs(graph, v, visited, u, max_weight)

def count_pairs(graph, queries):
    pairs = [0] * len(queries)
    for i, q in enumerate(queries):
        visited = set()
        for u in graph:
            if u not in visited:
                visited.add(u)
                dfs(graph, u, visited, -1, q)
                pairs[i] += len(visited) - 1
    return pairs

def main():
    n, m, edges, queries = read_data()
    graph = build_graph(edges)
    pairs = count_pairs(graph, queries)
    print(*pairs)

if __name__ == '__main__':
    main()

