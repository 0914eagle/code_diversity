
def read_input():
    N, Q = map(int, input().split())
    edges = []
    for _ in range(N - 1):
        a, b = map(int, input().split())
        edges.append((a, b))
    operations = []
    for _ in range(Q):
        p, x = map(int, input().split())
        operations.append((p, x))
    return N, Q, edges, operations

def build_tree(edges):
    tree = [[] for _ in range(len(edges) + 1)]
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    return tree

def dfs(tree, node, counter, counters):
    counters[node] += counter
    for neighbor in tree[node]:
        dfs(tree, neighbor, counter, counters)

def solve(N, Q, edges, operations):
    tree = build_tree(edges)
    counters = [0] * (N + 1)
    for p, x in operations:
        dfs(tree, p, x, counters)
    return counters

def main():
    N, Q, edges, operations = read_input()
    counters = solve(N, Q, edges, operations)
    print(*counters[1:], sep=' ')

if __name__ == '__main__':
    main()

