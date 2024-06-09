
def get_graph(n, f, w):
    graph = {}
    for i in range(n):
        graph[i] = []
    for i in range(n):
        graph[f[i]].append((i, w[i]))
    return graph

def find_path(graph, start, end, k):
    if start == end:
        return k * [0], k * [0]
    if start not in graph:
        return None, None
    min_weight = float('inf')
    min_path = []
    for node, weight in graph[start]:
        path, weight = find_path(graph, node, end, k-1)
        if path is not None:
            path = [weight] + path
            if weight < min_weight:
                min_weight = weight
                min_path = path
    return min_path, min_weight

def get_s_m(graph, start, end, k):
    path, weight = find_path(graph, start, end, k)
    if path is None:
        return 0, 0
    return sum(path), min(path)

def main():
    n, k = map(int, input().split())
    f = list(map(int, input().split()))
    w = list(map(int, input().split()))
    graph = get_graph(n, f, w)
    for i in range(n):
        s, m = get_s_m(graph, i, i, k)
        print(s, m)

if __name__ == '__main__':
    main()

