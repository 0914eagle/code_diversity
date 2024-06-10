
def add_edge(graph, x, y):
    graph[x].add(y)
    graph[y].add(x)

def has_path(graph, a, b, k, visited):
    if a == b:
        return k == 0
    if a not in graph or b not in graph:
        return False
    if a in visited:
        return False
    visited.add(a)
    for neighbor in graph[a]:
        if has_path(graph, neighbor, b, k-1, visited):
            return True
    return False

def tree_queries(n, edges, queries):
    graph = {i: set() for i in range(1, n+1)}
    for edge in edges:
        add_edge(graph, edge[0], edge[1])
    for query in queries:
        if has_path(graph, query[0], query[1], query[2], set()):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    n = int(input())
    edges = []
    for i in range(n-1):
        edges.append(list(map(int, input().split())))
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    tree_queries(n, edges, queries)

