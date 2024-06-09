
def f1(n):
    # Calculate the number of independent sets in the graph
    num_independent_sets = (1 << n) - 1
    return num_independent_sets

def f2(n, edges):
    # Calculate the sum of the number of independent sets in all except null edge-induced subgraphs
    sum_independent_sets = 0
    for i in range(1, n):
        for subset in itertools.combinations(range(n), i):
            if not any(edge[0] in subset and edge[1] in subset for edge in edges):
                sum_independent_sets += 1
    return sum_independent_sets

if __name__ == '__main__':
    n = int(input())
    edges = []
    for i in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(f2(n, edges) % 998244353)

