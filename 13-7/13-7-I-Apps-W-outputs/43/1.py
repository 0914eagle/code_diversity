
def get_graph(n, f, w):
    graph = {}
    for i in range(n):
        graph[i] = []
    for i in range(n):
        graph[f[i]].append((i, w[i]))
    return graph

def get_path(graph, k):
    path = []
    for i in range(k):
        path.append(graph[i])
    return path

def get_sum_min(graph, k):
    path = get_path(graph, k)
    s = 0
    m = float('inf')
    for i in range(k):
        s += graph[i][0][1]
        m = min(m, graph[i][0][1])
    return s, m

def main():
    n, k = map(int, input().split())
    f = list(map(int, input().split()))
    w = list(map(int, input().split()))
    graph = get_graph(n, f, w)
    for i in range(n):
        s, m = get_sum_min(graph[i], k)
        print(s, m)

if __name__ == '__main__':
    main()

