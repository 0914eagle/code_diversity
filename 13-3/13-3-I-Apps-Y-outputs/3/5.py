
def f1(n, m, k, x_y_w, a_b):
    # Initialize graph with costs
    graph = {i: {} for i in range(1, n + 1)}
    for x, y, w in x_y_w:
        graph[x][y] = w
        graph[y][x] = w

    # Floyd-Warshall algorithm to find shortest paths
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # Find the minimum total cost
    total_cost = float('inf')
    for a, b in a_b:
        total_cost = min(total_cost, graph[a][b])

    return total_cost

def f2(n, m, k, x_y_w, a_b):
    # Initialize graph with costs
    graph = {i: {} for i in range(1, n + 1)}
    for x, y, w in x_y_w:
        graph[x][y] = w
        graph[y][x] = w

    # Floyd-Warshall algorithm to find shortest paths
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # Find the minimum total cost
    total_cost = float('inf')
    for a, b in a_b:
        total_cost = min(total_cost, graph[a][b])

    return total_cost

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    x_y_w = []
    for _ in range(m):
        x, y, w = map(int, input().split())
        x_y_w.append((x, y, w))
    a_b = []
    for _ in range(k):
        a, b = map(int, input().split())
        a_b.append((a, b))
    print(f1(n, m, k, x_y_w, a_b))
    print(f2(n, m, k, x_y_w, a_b))

