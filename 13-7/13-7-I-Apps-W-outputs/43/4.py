
def get_graph(n, f, w):
    graph = {}
    for i in range(n):
        graph[i] = {f[i]: w[i]}
    return graph

def get_path_weights(graph, k):
    s = [0] * len(graph)
    m = [float('inf')] * len(graph)
    for i in range(len(graph)):
        if k == 1:
            s[i] = w[i]
            m[i] = w[i]
        else:
            for j in graph[i]:
                s[i] += s[j]
                m[i] = min(m[i], m[j] + w[i])
    return s, m

def main():
    n, k = map(int, input().split())
    f = list(map(int, input().split()))
    w = list(map(int, input().split()))
    graph = get_graph(n, f, w)
    s, m = get_path_weights(graph, k)
    for i in range(n):
        print(s[i], m[i])

if __name__ == '__main__':
    main()

