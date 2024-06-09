
import math

def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    divisors.sort()
    return divisors

def get_prime_divisors(n):
    prime_divisors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            prime_divisors.append(i)
    return prime_divisors

def get_graph(n):
    graph = {}
    divisors = get_divisors(n)
    for i in range(len(divisors)):
        for j in range(i, len(divisors)):
            x = divisors[i]
            y = divisors[j]
            if x % y == 0 and len(get_prime_divisors(x // y)) == 1:
                if x not in graph:
                    graph[x] = {}
                graph[x][y] = len(get_divisors(x)) - len(get_divisors(y))
    return graph

def get_shortest_paths(graph, v, u):
    visited = set()
    queue = [(0, v)]
    while queue:
        dist, node = queue.pop(0)
        if node == u:
            return dist
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node].items():
                queue.append((dist + weight, neighbor))
    return -1

def solve(D, q):
    graph = get_graph(D)
    for _ in range(q):
        v, u = map(int, input().split())
        print(get_shortest_paths(graph, v, u) % 998244353)

if __name__ == '__main__':
    D, q = map(int, input().split())
    solve(D, q)

