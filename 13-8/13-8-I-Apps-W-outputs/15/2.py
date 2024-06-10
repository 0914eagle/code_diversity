
def is_relatively_prime(v, u):
    return gcd(v, u) == 1

def construct_relatively_prime_graph(n, m):
    edges = []
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if not visited[i] and not visited[j] and is_relatively_prime(i, j):
                edges.append((i, j))
                visited[i] = visited[j] = True
                if len(edges) == m:
                    return edges
    return "Impossible"

def main():
    n, m = map(int, input().split())
    print(construct_relatively_prime_graph(n, m))

if __name__ == '__main__':
    main()

