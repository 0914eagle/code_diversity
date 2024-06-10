
def get_diameter(graph):
    diameter = 0
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] == 1:
                diameter += 1
    return diameter

def add_edges(graph):
    added_edges = []
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] == 0:
                added_edges.append((i, j))
    return added_edges

def main():
    n, m = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        v, u = map(int, input().split())
        graph[v][u] = 1
        graph[u][v] = 1
    print(get_diameter(graph))
    added_edges = add_edges(graph)
    for edge in added_edges:
        print(edge[0], edge[1])

if __name__ == '__main__':
    main()

