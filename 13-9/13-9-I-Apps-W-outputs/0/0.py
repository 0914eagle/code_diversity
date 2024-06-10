
def dfs(graph, node, visited, order):
    visited[node] = True
    order.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, order)
    return order

def build_graph(n, edges):
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph

def get_grade(graph, k, times):
    visited = [False] * (len(graph) + 1)
    order = []
    dfs(graph, 1, visited, order)
    return min(times[node] for node in order[:k])

def main():
    n, k = map(int, input().split())
    times = list(map(int, input().split()))
    edges = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    graph = build_graph(n, edges)
    print(get_grade(graph, k, times))

if __name__ == '__main__':
    main()

