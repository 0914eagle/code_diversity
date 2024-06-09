
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
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and is_prime(i):
            prime_divisors.append(i)
            if i * i != n:
                prime_divisors.append(n // i)
    prime_divisors.sort()
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
    divisors = get_divisors(D)
    for i in range(len(divisors)):
        graph[divisors[i]] = []
        for j in range(i+1, len(divisors)):
            if divisors[j] % divisors[i] == 0 and is_prime(divisors[j] // divisors[i]):
                graph[divisors[i]].append((divisors[j], divisors[j] // divisors[i]))
    return graph

def get_shortest_paths(graph, v, u):
    queue = [(v, [v], 0)]
    visited = set()
    while queue:
        (node, path, weight) = queue.pop(0)
        if node == u:
            return weight
        if node not in visited:
            visited.add(node)
            for neighbor, w in graph[node]:
                queue.append((neighbor, path + [neighbor], weight + w))
    return -1

def solve(D, q, queries):
    graph = get_graph(D)
    result = []
    for v, u in queries:
        result.append(get_shortest_paths(graph, v, u))
    return result

def main():
    D = int(input())
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(tuple(map(int, input().split())))
    result = solve(D, q, queries)
    for i in result:
        print(i)

if __name__ == '__main__':
    main()

