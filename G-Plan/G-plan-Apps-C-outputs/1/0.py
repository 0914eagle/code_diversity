
from itertools import product

def is_adjacent(c1, c2):
    return abs(ord(c1) - ord(c2)) <= 1

def construct_graph(s):
    n = len(s)
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if is_adjacent(s[i], s[j]):
                graph[i][j] = graph[j][i] = 1
    return graph

def check_string(graph, n):
    for s in product("abc", repeat=n):
        if construct_graph(s) == graph:
            return "Yes", "".join(s)
    return "No", ""

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[0] * n for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u-1][v-1] = graph[v-1][u-1] = 1
    result, string = check_string(graph, n)
    print(result)
    if result == "Yes":
        print(string)
