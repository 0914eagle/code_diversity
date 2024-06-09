
def solve(n, m, a, b, roads):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for i in range(m):
        graph[roads[i][0] - 1].append(roads[i][1] - 1)
        graph[roads[i][1] - 1].append(roads[i][0] - 1)
    
    # Check if the conditions can be met
    for i in range(n):
        if a[i] != b[i]:
            return "NO"
    
    # If the conditions can be met, return a solution
    solution = [[0] * n for _ in range(n)]
    for i in range(n):
        solution[i][i] = a[i]
    
    return "YES\n" + "\n".join([" ".join(map(str, row)) for row in solution])

