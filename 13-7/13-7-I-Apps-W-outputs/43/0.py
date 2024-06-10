
def get_path_info(graph, k):
    n = len(graph)
    s = [0] * n
    m = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if graph[i][j] != 0:
                s[i] += graph[i][j]
                m[i] = min(m[i], graph[i][j])
    return s, m

def get_path_info_from_file(filename, k):
    with open(filename, "r") as f:
        n, m = map(int, f.readline().split())
        graph = []
        for i in range(n):
            graph.append(list(map(int, f.readline().split())))
    return get_path_info(graph, k)

if __name__ == '__main__':
    s, m = get_path_info_from_file("graph.txt", 3)
    for i in range(len(s)):
        print(s[i], m[i])

