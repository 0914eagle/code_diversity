
from itertools import product

def construct_graph(s, n):
    graph = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and abs(ord(s[i]) - ord(s[j])) <= 1:
                graph[i][j] = True
    return graph

def check_string(graph, n):
    for s in product("abc", repeat=n):
        if construct_graph(s, n) == graph:
            return "Yes", "".join(s)
    return "No", ""

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[False] * n for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1][v - 1] = True
        graph[v - 1][u - 1] = True

    result, string = check_string(graph, n)
    print(result)
    if result == "Yes":
        print(string)
