
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

def get_prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def get_graph(n):
    graph = {}
    divisors = get_divisors(n)
    for i in range(len(divisors)):
        for j in range(i + 1, len(divisors)):
            x = divisors[i]
            y = divisors[j]
            if x % y == 0 and len(get_prime_factors(x // y)) == 1:
                if x not in graph:
                    graph[x] = []
                graph[x].append((y, x // y))
    return graph

def get_shortest_paths(graph, v, u):
    queue = [(0, v)]
    visited = set()
    while queue:
        dist, node = queue.pop(0)
        if node == u:
            return dist
        if node not in visited:
            visited.add(node)
            if node in graph:
                for neighbor, weight in graph[node]:
                    queue.append((dist + weight, neighbor))
    return -1

def number_of_shortest_paths(graph, v, u):
    count = 0
    queue = [(0, v)]
    visited = set()
    while queue:
        dist, node = queue.pop(0)
        if node == u:
            count += 1
        if node not in visited:
            visited.add(node)
            if node in graph:
                for neighbor, weight in graph[node]:
                    queue.append((dist + weight, neighbor))
    return count

def main():
    d, q = map(int, input().split())
    graph = get_graph(d)
    for _ in range(q):
        v, u = map(int, input().split())
        print(number_of_shortest_paths(graph, v, u) % 998244353)

if __name__ == '__main__':
    main()

