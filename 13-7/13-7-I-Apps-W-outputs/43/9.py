
def get_graph(n, f, w):
    graph = {}
    for i in range(n):
        graph[i] = []
    for i in range(n):
        graph[i].append((f[i], w[i]))
    return graph

def bfs(graph, start, k):
    queue = [[start, 0]]
    visited = set()
    while queue:
        node, dist = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if dist == k:
                return node
            for neighbor, weight in graph[node]:
                queue.append([neighbor, dist+1])
    return -1

def get_s_m(graph, k):
    s = [0] * len(graph)
    m = [0] * len(graph)
    for i in range(len(graph)):
        node = bfs(graph, i, k)
        if node != -1:
            s[i] = graph[i][node][1]
            m[i] = graph[i][node][1]
        for j in range(len(graph[i])):
            if graph[i][j][1] < m[i]:
                m[i] = graph[i][j][1]
    return s, m

def main():
    n, k = map(int, input().split())
    f = list(map(int, input().split()))
    w = list(map(int, input().split()))
    graph = get_graph(n, f, w)
    s, m = get_s_m(graph, k)
    for i in range(n):
        print(s[i], m[i])

if __name__ == '__main__':
    main()

