
def is_relatively_prime(v, u):
    return gcd(v, u) == 1

def construct_relatively_prime_graph(n, m):
    edges = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if is_relatively_prime(i, j) and len(edges) < m:
                edges.append((i, j))
    if len(edges) == m:
        return edges
    else:
        return "Impossible"

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(construct_relatively_prime_graph(n, m))

