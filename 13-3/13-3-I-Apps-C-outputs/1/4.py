
def kahn_algorithm(graph):
    in_degree = {node: 0 for node in graph}
    for u, v in graph:
        in_degree[v] += 1
    queue = [node for node in graph if in_degree[node] == 0]
    sorted_nodes = []
    while queue:
        node = queue.pop(0)
        sorted_nodes.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return sorted_nodes

def largest_s(graph):
    in_degree = {node: 0 for node in graph}
    for u, v in graph:
        in_degree[v] += 1
    queue = [node for node in graph if in_degree[node] == 0]
    largest_s = 0
    while queue:
        node = queue.pop(0)
        largest_s = max(largest_s, len(queue))
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return largest_s

if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
    print(largest_s(graph))

