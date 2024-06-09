
def get_graph(n, f, w):
    graph = {}
    for i in range(n):
        graph[i] = [w[i], f[i]]
    return graph

def get_path(graph, start, k):
    if k == 0:
        return 0, 0
    if start not in graph:
        return 0, 0
    weight, next_node = graph[start]
    s, m = get_path(graph, next_node, k-1)
    return s + weight, min(m, weight)

def get_s_and_m(graph, k):
    result = []
    for node in graph:
        s, m = get_path(graph, node, k)
        result.append((s, m))
    return result

def main():
    n, k = map(int, input().split())
    f = list(map(int, input().split()))
    w = list(map(int, input().split()))
    graph = get_graph(n, f, w)
    result = get_s_and_m(graph, k)
    for s, m in result:
        print(s, m)

if __name__ == '__main__':
    main()

