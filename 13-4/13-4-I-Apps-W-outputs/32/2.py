
def get_graph(n, k, f, w):
    graph = {}
    for i in range(n):
        graph[i] = []
    for i in range(n):
        graph[i].append((f[i], w[i]))
    return graph

def get_path(graph, start, k):
    if k == 0:
        return 0, 0
    if start not in graph:
        return 0, 0
    paths = []
    for next, weight in graph[start]:
        s, m = get_path(graph, next, k-1)
        paths.append((s+weight, m+weight))
    return min(paths)

def get_s_m(graph, k):
    s_m = []
    for i in range(len(graph)):
        s, m = get_path(graph, i, k)
        s_m.append((s, m))
    return s_m

def main():
    n, k = map(int, input().split())
    f = list(map(int, input().split()))
    w = list(map(int, input().split()))
    graph = get_graph(n, k, f, w)
    s_m = get_s_m(graph, k)
    for s, m in s_m:
        print(s, m)

if __name__ == '__main__':
    main()

