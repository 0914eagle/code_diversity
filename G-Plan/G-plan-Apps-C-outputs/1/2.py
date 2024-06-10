
from itertools import product

def generate_strings(n):
    return [''.join(s) for s in product('abc', repeat=n)]

def construct_graph(s, edges):
    graph = {i: set() for i in range(1, len(s) + 1)}
    for u, v in edges:
        if abs(ord(s[u - 1]) - ord(s[v - 1])) <= 1:
            graph[u].add(v)
            graph[v].add(u)
    return graph

def check_string_exists(n, m, edges):
    for s in generate_strings(n):
        graph = construct_graph(s, edges)
        if all(v in graph[u] for u in graph for v in graph[u]):
            return "Yes", s
    return "No", ""

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    result, string = check_string_exists(n, m, edges)
    print(result)
    if result == "Yes":
        print(string)
