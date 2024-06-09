
def solve(maze):
    # Convert the maze to a graph
    graph = {}
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == '.':
                graph[(i, j)] = []
    
    # Find all the adjacent roads
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == '.':
                if i > 0 and maze[i-1][j] == '.':
                    graph[(i, j)].append((i-1, j))
                if i < len(maze)-1 and maze[i+1][j] == '.':
                    graph[(i, j)].append((i+1, j))
                if j > 0 and maze[i][j-1] == '.':
                    graph[(i, j)].append((i, j-1))
                if j < len(maze[0])-1 and maze[i][j+1] == '.':
                    graph[(i, j)].append((i, j+1))
    
    # Find the shortest path between the starting and goal squares
    start = None
    goal = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == '.':
                if start is None:
                    start = (i, j)
                elif goal is None:
                    goal = (i, j)
    
    visited = set()
    queue = [(start, 0)]
    while queue:
        current, distance = queue.pop(0)
        if current not in visited:
            visited.add(current)
            if current == goal:
                return distance
            for neighbor in graph[current]:
                queue.append((neighbor, distance+1))
    
    return -1

