
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
            graph[u] = []
        graph[u].append((v, w))
    return graph

def dfs(graph, u, visited, max_weight):
    if u in visited:
        return
    visited.add(u)
    for v, w in graph[u]:
        if w <= max_weight:
            dfs(graph, v, visited, max_weight)

def count_pairs(graph, queries):
    answers = []
    for q in queries:
        visited = set()
        count = 0
        for u in graph:
            if u not in visited:
                dfs(graph, u, visited, q)
                count += len(visited) - 1
        answers.append(count)
    return answers

def main():
    n, m, edges, queries = read_data()
    graph = build_graph(edges)
    answers = count_pairs(graph, queries)
    print(*answers)

if __name__ == '__main__':
    main()

