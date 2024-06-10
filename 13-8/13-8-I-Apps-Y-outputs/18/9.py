
def get_diameter(graph):
    diameter = 0
    for node in graph:
        for neighbor in graph[node]:
            if graph[node][neighbor] > diameter:
                diameter = graph[node][neighbor]
    return diameter

def add_edges(graph):
    added_edges = []
    for node in graph:
        for neighbor in graph[node]:
            if graph[node][neighbor] > 1:
                added_edges.append((node, neighbor))
    return added_edges

def main():
    n, m = map(int, input().split())
    graph = {i: {} for i in range(1, n + 1)}
    for _ in range(m):
        v, u = map(int, input().split())
        graph[v][u] = 1
        graph[u][v] = 1
    diameter = get_diameter(graph)
    added_edges = add_edges(graph)
    print(diameter)
    for edge in added_edges:
        print(*edge)

if __name__ == '__main__':
    main()

