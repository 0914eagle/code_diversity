
def get_path_info(graph, k):
    n = len(graph)
    s = [0] * n
    m = [0] * n
    for i in range(n):
        s[i], m[i] = get_path_info_util(graph, i, k, set())
    return s, m

def get_path_info_util(graph, curr, k, visited):
    if k == 0:
        return 0, 0
    if curr == -1:
        return float('inf'), float('inf')
    if curr in visited:
        return float('inf'), float('inf')
    visited.add(curr)
    next_ = graph[curr]
    s, m = get_path_info_util(graph, next_, k-1, visited)
    return s + graph[curr], min(m, graph[curr])

def main():
    n, k = map(int, input().split())
    graph = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    for i in range(n):
        graph[i] -= 1
    s, m = get_path_info(graph, k)
    for i in range(n):
        print(s[i], m[i])

if __name__ == '__main__':
    main()

