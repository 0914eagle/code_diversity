
def f1(n, x, edges):
    # Initialize the graph with the given edges
    graph = {i: set() for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    # Initialize the beauty of each vertex to be its own beauty
    beauty = {i: x[i - 1] for i in range(1, n + 1)}

    # Iterate through all vertices and update the beauty of their ancestors
    for u in range(1, n + 1):
        for v in graph[u]:
            if v != u:
                beauty[u] = gcd(beauty[u], beauty[v])

    # Calculate the sum of the beauties of all paths
    sum_beauty = 0
    for u in range(1, n + 1):
        for v in graph[u]:
            if v != u:
                sum_beauty += beauty[u]

    return sum_beauty % (10**9 + 7)

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(f1(n, x, edges))

