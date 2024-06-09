
def solve_world_programming_championship(n, m, c_l, c_e, v, queries):
    # Initialize the graph as a dictionary of dictionaries
    graph = {}
    for i in range(1, n+1):
        graph[i] = {}
        for j in range(1, m+1):
            graph[i][j] = 0
    
    # Fill in the graph with the information about the stairs and elevators
    for i in range(1, c_l+1):
        graph[i][l_i] = 1
    for i in range(1, c_e+1):
        graph[i][e_i] = 1
    
    # Solve the queries
    answers = []
    for query in queries:
        x1, y1, x2, y2 = query
        answers.append(bfs(graph, x1, y1, x2, y2))
    
    return answers

def bfs(graph, x1, y1, x2, y2):
    # Initialize the queue and visited set
    queue = [(x1, y1, 0)]
    visited = set()
    
    # Loop until the queue is empty
    while queue:
        # Get the current node and its distance from the starting node
        node, distance = queue.pop(0)
        x, y = node
        
        # If the current node is the destination, return the distance
        if x == x2 and y == y2:
            return distance
        
        # If the current node has not been visited before, mark it as visited and add its neighbors to the queue
        if node not in visited:
            visited.add(node)
            for neighbor in get_neighbors(graph, x, y):
                queue.append((neighbor[0], neighbor[1], distance+1))
    
    # If the destination is not reachable, return -1
    return -1

def get_neighbors(graph, x, y):
    # Get the neighbors of the current node
    neighbors = []
    if x-1 >= 1 and graph[x-1][y] == 0:
        neighbors.append((x-1, y))
    if x+1 <= n and graph[x+1][y] == 0:
        neighbors.append((x+1, y))
    if y-1 >= 1 and graph[x][y-1] == 0:
        neighbors.append((x, y-1))
    if y+1 <= m and graph[x][y+1] == 0:
        neighbors.append((x, y+1))
    
    # Return the neighbors
    return neighbors

