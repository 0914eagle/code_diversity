
def solve(n, m, c_l, c_e, v, queries):
    # Initialize the graph with the dimensions of the hotel
    graph = [[0] * (m + 1) for _ in range(n + 1)]

    # Add the stairs to the graph
    for i in range(c_l):
        graph[i][l_i] = 1
        graph[i + 1][l_i] = 1

    # Add the elevators to the graph
    for i in range(c_e):
        graph[i][e_i] = 1
        graph[i + 1][e_i] = 1

    # Fill in the rest of the graph with the distances between sections
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = abs(i - j)

    # Solve the queries
    answers = []
    for query in queries:
        x1, y1, x2, y2 = query
        answers.append(graph[x1][y1] + graph[x2][y2])

    return answers

