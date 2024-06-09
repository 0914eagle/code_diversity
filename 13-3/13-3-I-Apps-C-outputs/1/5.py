
def kahn_algorithm(graph):
    in_degree = [0] * len(graph)
    for u in range(len(graph)):
        for v in graph[u]:
            in_degree[v] += 1
    queue = [u for u in range(len(graph)) if in_degree[u] == 0]
    order = []
    while queue:
        u = queue.pop(0)
        order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    return order

def largest_s(graph):
    order = kahn_algorithm(graph)
    if order:
        return len(order)
    else:
        return 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    print(largest_s(graph))

