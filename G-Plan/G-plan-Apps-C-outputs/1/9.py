
def is_valid_string_exists(n, m, edges):
    def construct_graph(s):
        graph = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if abs(ord(s[i]) - ord(s[j])) <= 1:
                    graph[i][j] = graph[j][i] = 1
        return graph

    def is_valid_string(s):
        graph = construct_graph(s)
        for u, v in edges:
            if not graph[u - 1][v - 1]:
                return False
        return True

    for s in ['a', 'b', 'c']:
        for s2 in ['a', 'b', 'c']:
            if is_valid_string(s * (n // 2) + s2 * (n - n // 2)):
                return "Yes", s * (n // 2) + s2 * (n - n // 2)
    return "No", ""

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    result, string = is_valid_string_exists(n, m, edges)
    print(result)
    if result == "Yes":
        print(string)
