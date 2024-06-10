
def add_edge(tree, x, y):
    # Add an edge between vertices x and y in the tree
    tree[x].append(y)
    tree[y].append(x)
    return tree

def find_path(tree, a, b, k):
    # Find a path from vertex a to vertex b in the tree with exactly k edges
    queue = [(a, 0)]
    visited = set()
    while queue:
        node, count = queue.pop(0)
        if node == b and count == k:
            return True
        if node not in visited:
            visited.add(node)
            for neighbor in tree[node]:
                queue.append((neighbor, count + 1))
    return False

def solve(tree, queries):
    # Solve the queries on the tree
    results = []
    for query in queries:
        x, y, a, b, k = query
        tree = add_edge(tree, x, y)
        result = find_path(tree, a, b, k)
        results.append("YES" if result else "NO")
    return results

def main():
    n = int(input())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    results = solve(tree, queries)
    for result in results:
        print(result)

if __name__ == '__main__':
    main()

