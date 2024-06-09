
def f1(maze):
    # Convert the maze to a graph
    graph = {}
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == '.':
                graph[(i, j)] = []
    # Add neighbors to the graph
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
    return graph

def f2(graph, start, end):
    # Breadth-first search
    queue = [(start, 0)]
    visited = set()
    while queue:
        node, distance = queue.pop(0)
        if node == end:
            return distance
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, distance+1))
    return -1

if __name__ == '__main__':
    H, W = map(int, input().split())
    maze = [input() for _ in range(H)]
    graph = f1(maze)
    start = tuple(int(x) for x in input().split())
    end = tuple(int(x) for x in input().split())
    print(f2(graph, start, end))

