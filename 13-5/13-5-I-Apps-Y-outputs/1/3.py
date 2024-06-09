
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

def dfs(graph, u, visited, max_weight, pairs):
    if u in visited:
        return
    visited.add(u)
    for v in graph[u]:
        if v not in visited and graph[u][v] <= max_weight:
            pairs.add((u, v))
            dfs(graph, v, visited, max_weight, pairs)

def count_pairs(graph, queries):
    answers = []
    for q in queries:
        pairs = set()
        for u in graph:
            visited = set()
            dfs(graph, u, visited, q, pairs)
        answers.append(len(pairs))
    return answers

def main():
    n, m, edges, queries = read_data()
    graph = build_graph(edges)
    answers = count_pairs(graph, queries)
    print(*answers)

if __name__ == '__main__':
    main()

