
def f1(n, x, edges):
    # Initialize the graph with the given edges
    graph = {i + 1: set() for i in range(n)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    # Initialize the ancestor dictionary
    ancestors = {i + 1: set() for i in range(n)}
    ancestors[1] = set(range(2, n + 1))

    # Iterate through the vertices and update the ancestor dictionary
    for u in range(2, n + 1):
        for v in graph[u]:
            if v not in ancestors[u]:
                ancestors[u].add(v)
                ancestors[v].add(u)

    # Calculate the sum of the beauties on all paths
    sum_beauties = 0
    for u in range(1, n + 1):
        for v in ancestors[u]:
            if u != v:
                path = [u, v]
                beauty = x[u - 1]
                while v != 1:
                    v = min(ancestors[v]) - 1
                    path.append(v + 1)
                    beauty = gcd(beauty, x[v])
                sum_beauties = (sum_beauties + beauty) % 1000000007

    return sum_beauties

def f2(n, x, edges):
    # Initialize the graph with the given edges
    graph = {i + 1: set() for i in range(n)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    # Initialize the ancestor dictionary
    ancestors = {i + 1: set() for i in range(n)}
    ancestors[1] = set(range(2, n + 1))

    # Iterate through the vertices and update the ancestor dictionary
    for u in range(2, n + 1):
        for v in graph[u]:
            if v not in ancestors[u]:
                ancestors[u].add(v)
                ancestors[v].add(u)

    # Calculate the sum of the beauties on all paths
    sum_beauties = 0
    for u in range(1, n + 1):
        for v in ancestors[u]:
            if u != v:
                path = [u, v]
                beauty = x[u - 1]
                while v != 1:
                    v = min(ancestors[v]) - 1
                    path.append(v + 1)
                    beauty = gcd(beauty, x[v])
                sum_beauties = (sum_beauties + beauty) % 1000000007

    return sum_beauties

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(f1(n, x, edges))
    print(f2(n, x, edges))

