
def get_graph(n, f, w):
    graph = {}
    for i in range(n):
        graph[i] = []
        for j in range(n):
            if f[i] == j:
                graph[i].append((j, w[i]))
    return graph

def bfs(graph, start, k):
    queue = [(start, 0)]
    visited = set()
    while queue:
        vertex, distance = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            if distance == k:
                return vertex
            for neighbor, weight in graph[vertex]:
                queue.append((neighbor, distance + weight))
    return -1

def solve(n, k, f, w):
    graph = get_graph(n, f, w)
    result = []
    for i in range(n):
        vertex = bfs(graph, i, k)
        if vertex != -1:
            result.append((i, vertex))
    return result

if __name__ == '__main__':
    n, k = map(int, input().split())
    f = list(map(int, input().split()))
    w = list(map(int, input().split()))
    result = solve(n, k, f, w)
    for i, j in result:
        print(i, j)

