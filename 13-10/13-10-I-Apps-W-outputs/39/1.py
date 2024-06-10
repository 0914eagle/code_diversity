
def add_edge(tree, x, y):
    tree.add_edge(x, y)
    tree.add_edge(y, x)


def has_path(tree, a, b, k):
    if a == b:
        return k == 0
    if k == 0:
        return False
    for neighbor in tree.neighbors(a):
        if has_path(tree, neighbor, b, k - 1):
            return True
    return False


def solve(n, edges, q, queries):
    tree = Graph(n)
    for edge in edges:
        tree.add_edge(edge[0], edge[1])
        tree.add_edge(edge[1], edge[0])
    for query in queries:
        x, y, a, b, k = query
        add_edge(tree, x, y)
        result = "YES" if has_path(tree, a, b, k) else "NO"
        print(result)
        add_edge(tree, y, x)


if __name__ == '__main__':
    n = int(input())
    edges = []
    for _ in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(tuple(map(int, input().split())))
    solve(n, edges, q, queries)

