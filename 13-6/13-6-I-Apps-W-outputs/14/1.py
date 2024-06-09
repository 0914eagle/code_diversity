
import sys

def read_list_int():
    return list(map(int, sys.stdin.readline().strip().split()))

def read_list_int2():
    return list(map(lambda x: list(map(int, x)), sys.stdin.readline().strip().split()))

def get_graph(D, v, u):
    graph = [[] for _ in range(D+1)]
    for i in range(1, D+1):
        for j in range(1, D+1):
            if i % j == 0 and is_prime(i//j):
                graph[i].append(j)
    return graph

def get_shortest_paths(graph, v, u):
    queue = [(0, v)]
    visited = set()
    while queue:
        dist, node = queue.pop(0)
        if node == u:
            return dist
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            queue.append((dist+1, neighbor))
    return -1

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solve(D, q, queries):
    graph = get_graph(D, v, u)
    result = []
    for v, u in queries:
        result.append(get_shortest_paths(graph, v, u))
    return result

def main():
    D, q = read_list_int()
    queries = read_list_int2()
    result = solve(D, q, queries)
    print(*result, sep='\n')

if __name__ == '__main__':
    main()

