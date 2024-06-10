
import sys

def add_edge(tree, x, y):
    tree[x].add(y)
    tree[y].add(x)

def count_paths(tree, a, b, k):
    queue = [(a, 0)]
    visited = set()
    while queue:
        node, distance = queue.pop(0)
        if node == b and distance == k:
            return True
        if node not in visited:
            visited.add(node)
            for neighbor in tree[node]:
                queue.append((neighbor, distance + 1))
    return False

def solve(n, q, queries):
    tree = {i: set() for i in range(1, n + 1)}
    for i in range(1, n):
        u, v = map(int, sys.stdin.readline().split())
        add_edge(tree, u, v)
    for _ in range(q):
        x, y, a, b, k = map(int, sys.stdin.readline().split())
        add_edge(tree, x, y)
        print("YES") if count_paths(tree, a, b, k) else print("NO")
        remove_edge(tree, x, y)

def remove_edge(tree, x, y):
    tree[x].remove(y)
    tree[y].remove(x)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    q = int(sys.stdin.readline())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, sys.stdin.readline().split())))
    solve(n, q, queries)

