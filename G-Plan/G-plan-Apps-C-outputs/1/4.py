
def is_valid_string_exists(n, m, edges):
    graph = [[False] * n for _ in range(n)]
    for u, v in edges:
        graph[u - 1][v - 1] = True
        graph[v - 1][u - 1] = True

    def is_valid_string(s):
        for i in range(n):
            for j in range(i + 1, n):
                if abs(ord(s[i]) - ord(s[j])) <= 1 and not graph[i][j]:
                    return False
                if abs(ord(s[i]) - ord(s[j])) > 1 and graph[i][j]:
                    return False
        return True

    def generate_strings(curr, length):
        if length == n:
            if is_valid_string(curr):
                return True, curr
            return False, ""
        for char in ['a', 'b', 'c']:
            found, result = generate_strings(curr + char, length + 1)
            if found:
                return True, result
        return False, ""

    found, result = generate_strings("", 0)
    if found:
        return "Yes", result
    return "No", ""

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    result, string = is_valid_string_exists(n, m, edges)
    print(result)
    if result == "Yes":
        print(string)
