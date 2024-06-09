
def is_valid_position(position, maze):
    r, c = position
    return 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] != '#'

def is_on_fire(position, maze):
    r, c = position
    return maze[r][c] == 'F'

def is_exit(position, maze):
    r, c = position
    return r == 0 or r == len(maze) - 1 or c == 0 or c == len(maze[0]) - 1

def bfs(maze, start, goal):
    queue = [(start, 0)]
    visited = set()
    while queue:
        position, time = queue.pop(0)
        if position == goal:
            return time
        if position in visited:
            continue
        visited.add(position)
        for neighbor in [(position[0] + 1, position[1]), (position[0] - 1, position[1]), (position[0], position[1] + 1), (position[0], position[1] - 1)]:
            if is_valid_position(neighbor, maze) and not is_on_fire(neighbor, maze) and neighbor not in visited:
                queue.append((neighbor, time + 1))
    return -1

def f1(maze):
    start = None
    goal = None
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'J':
                start = (r, c)
            elif maze[r][c] == 'F':
                goal = (r, c)
    return bfs(maze, start, goal)

def f2(...):
    ...

if __name__ == '__main__':
    maze = []
    for _ in range(int(input())):
        maze.append(list(input()))
    print(f1(maze))

