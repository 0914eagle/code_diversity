
def solve(n, m, c_l, c_e, v, queries):
    # Initialize the graph with the dimensions of the hotel
    graph = [[0] * (m + 1) for _ in range(n + 1)]

    # Add the stairs and elevators to the graph
    for i in range(c_l):
        graph[l_i][l_i] = 1
    for i in range(c_e):
        graph[e_i][e_i] = 1

    # Fill in the graph with the distances between sections
    for i in range(n):
        for j in range(m):
            if i + 1 < n:
                graph[i][j] = graph[i + 1][j] = 1
            if j + 1 < m:
                graph[i][j] = graph[i][j + 1] = 1

    # Solve the queries
    results = []
    for query in queries:
        x1, y1, x2, y2 = query
        results.append(graph[x1][y1] + graph[x2][y2])

    return results

