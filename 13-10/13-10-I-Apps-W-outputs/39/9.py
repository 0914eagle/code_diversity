
def build_tree(n, edges):
    # Build a tree with n vertices and edges as the given edges
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    return graph

def add_edge(graph, x, y):
    # Add a bidirectional edge between vertices x and y in the given graph
    graph[x-1].append(y-1)
    graph[y-1].append(x-1)
    return graph

def find_path(graph, a, b, k):
    # Find a path from vertex a to vertex b with exactly k edges in the given graph
    queue = [(a, 0)]
    visited = set()
    while queue:
        vertex, count = queue.pop(0)
        if vertex == b:
            return count == k
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                queue.append((neighbor, count+1))
    return False

def solve(n, edges, queries):
    # Build a tree with n vertices and edges as the given edges
    # Add bidirectional edges for each query and check if a path exists between a and b with exactly k edges
    graph = build_tree(n, edges)
    for x, y, a, b, k in queries:
        graph = add_edge(graph, x, y)
        if find_path(graph, a, b, k):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    n = int(input())
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    q = int(input())
    queries = []
    for _ in range(q):
        x, y, a, b, k = map(int, input().split())
        queries.append((x, y, a, b, k))
    solve(n, edges, queries)

