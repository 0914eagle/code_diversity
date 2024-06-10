
from itertools import product

def construct_graph(s, n):
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if abs(ord(s[i]) - ord(s[j])) <= 1:
                graph[i][j] = 1
                graph[j][i] = 1
    return graph

def check_graph(graph, edges):
    n = len(graph)
    for u, v in edges:
        if graph[u-1][v-1] == 0:
            return False
    return True

def generate_strings(n):
    letters = ['a', 'b', 'c']
    for s in product(letters, repeat=n):
        yield ''.join(s)

def solve():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    for s in generate_strings(n):
        graph = construct_graph(s, n)
        if check_graph(graph, edges):
            print("Yes")
            print(s)
            return

    print("No")

if __name__ == "__main__":
    solve()
