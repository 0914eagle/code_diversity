
def f1(n, x, edges):
    # Initialize the graph with the given edges
    graph = {i + 1: set() for i in range(n)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    # Initialize the ancestor dictionary
    ancestors = {i + 1: set() for i in range(n)}
    ancestors[1].add(1)

    # Find all ancestors for each vertex
    for u in range(2, n + 1):
        for v in graph[u]:
            ancestors[u] |= ancestors[v]
            ancestors[u].add(u)

    # Calculate the sum of the beauties on all paths
    sum_beauties = 0
    for u in range(1, n + 1):
        for v in ancestors[u]:
            if u != v:
                path = [u, v]
                while path[0] != path[-1]:
                    path.append(path[0])
                    path[0] = graph[path[0]].pop()
                sum_beauties += x[path[0]]

    return sum_beauties % (10**9 + 7)

def f2(...):
    ...

if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(f1(n, x, edges))

