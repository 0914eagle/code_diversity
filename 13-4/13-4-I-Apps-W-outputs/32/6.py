
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
        node, dist = queue.pop(0)
        if node not in visited:
            visited.add(node)
            if dist == k:
                return node
            for neighbor, weight in graph[node]:
                queue.append((neighbor, dist + weight))
    return -1

def solve(n, k, f, w):
    graph = get_graph(n, f, w)
    result = []
    for i in range(n):
        node = bfs(graph, i, k)
        if node != -1:
            result.append((sum(w[i:node+1]), min(w[i:node+1])))
        else:
            result.append((0, 0))
    return result

if __name__ == '__main__':
    n, k = map(int, input().split())
    f = list(map(int, input().split()))
    w = list(map(int, input().split()))
    result = solve(n, k, f, w)
    for i in range(n):
        print(result[i][0], result[i][1])

