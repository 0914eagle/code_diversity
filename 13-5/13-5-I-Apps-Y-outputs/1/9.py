
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

def find_paths(graph, start, end, max_weight):
    if start == end:
        return 1
    if start not in graph or end not in graph[start] or graph[start][end] > max_weight:
        return 0
    return find_paths(graph, start, end, max_weight) + find_paths(graph, start, end, max_weight - graph[start][end])

def count_pairs(graph, queries):
    pairs = 0
    for query in queries:
        for u in graph:
            for v in graph[u]:
                pairs += find_paths(graph, u, v, query)
    return pairs

def main():
    n, m, edges, queries = read_data()
    graph = build_graph(edges)
    print(count_pairs(graph, queries))

if __name__ == '__main__':
    main()

