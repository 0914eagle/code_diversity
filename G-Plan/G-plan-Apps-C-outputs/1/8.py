
from itertools import product

def is_valid_string(graph, n, m, s):
    def construct_graph(s):
        graph_s = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if abs(ord(s[i]) - ord(s[j])) <= 1:
                    graph_s[i][j] = graph_s[j][i] = 1
        return graph_s

    def is_same_graph(graph1, graph2):
        for i in range(n):
            for j in range(n):
                if graph1[i][j] != graph2[i][j]:
                    return False
        return True

    for string in product('abc', repeat=n):
        if is_same_graph(graph, construct_graph(string), n):
            return "Yes", ''.join(string)
    return "No", ""

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[0] * n for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u-1][v-1] = graph[v-1][u-1] = 1

    result, string = is_valid_string(graph, n, m, 'abc')
    print(result)
    if result == "Yes":
        print(string)
