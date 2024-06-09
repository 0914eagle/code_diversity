
def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    divisors.sort()
    return divisors

def get_prime_divisors(n):
    prime_divisors = []
    for d in get_divisors(n):
        if is_prime(d):
            prime_divisors.append(d)
    return prime_divisors

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_graph(D):
    graph = {}
    for v in range(1, D + 1):
        graph[v] = []
        for d in get_divisors(v):
            if is_prime(d):
                graph[v].append(d)
    return graph

def get_shortest_paths(graph, v, u):
    queue = [(0, v)]
    visited = set()
    while queue:
        distance, node = queue.pop(0)
        if node == u:
            return distance
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((distance + 1, neighbor))
    return -1

def get_number_of_shortest_paths(graph, v, u):
    number_of_paths = 0
    for node in range(1, u + 1):
        if get_shortest_paths(graph, v, node) != -1:
            number_of_paths += 1
    return number_of_paths

def main():
    D = int(input())
    q = int(input())
    graph = get_graph(D)
    for _ in range(q):
        v, u = map(int, input().split())
        print(get_number_of_shortest_paths(graph, v, u) % 998244353)

if __name__ == '__main__':
    main()

