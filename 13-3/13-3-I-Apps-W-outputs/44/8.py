
def solve(n, m, c_l, c_e, v, q, queries):
    # Initialize the graph with the number of floors and sections
    graph = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Add the stairs and elevators to the graph
    for i in range(c_l):
        graph[l_i][l_i] = 1
    for i in range(c_e):
        graph[e_i][e_i] = 1
    
    # Fill in the rest of the graph with the time it takes to move between sections
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
            if j < m - 1 and graph[i][j + 1] == 0:
                graph[i][j + 1] = 1
            if i < n - 1 and graph[i + 1][j] == 0:
                graph[i + 1][j] = 1
    
    # Solve the queries
    answers = []
    for query in queries:
        x1, y1, x2, y2 = query
        answers.append(graph[x1][y1] + graph[x2][y2])
    
    return answers

