
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
    parents = {i: [] for i in range(1, len(edges) + 2)}
    for a, b in edges:
        parents[a].append(b)
        parents[b].append(a)
    return parents

def update_counters(parents, operation, counters):
    p, x = operation
    if p in counters:
        counters[p] += x
    for child in parents[p]:
        update_counters(parents, (child, x), counters)

def solve(N, Q, edges, operations):
    parents = build_tree(edges)
    counters = {i: 0 for i in range(1, N + 1)}
    for operation in operations:
        update_counters(parents, operation, counters)
    return [counters[i] for i in range(1, N + 1)]

def main():
    N, Q, edges, operations = read_input()
    counters = solve(N, Q, edges, operations)
    print(' '.join(map(str, counters)))

if __name__ == '__main__':
    main()

