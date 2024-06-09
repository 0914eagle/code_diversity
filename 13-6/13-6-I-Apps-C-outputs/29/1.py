
def read_maze(R, C):
    maze = []
    for _ in range(R):
        maze.append(list(input()))
    return maze

def find_joe(maze):
    for row in maze:
        for col in row:
            if col == 'J':
                return (row.index(col), maze.index(row))
    return None

def find_fire(maze):
    for row in maze:
        for col in row:
            if col == 'F':
                return (row.index(col), maze.index(row))
    return None

def is_safe(maze, joe_pos, fire_pos):
    R, C = len(maze), len(maze[0])
    dr, dc = fire_pos[0] - joe_pos[0], fire_pos[1] - joe_pos[1]
    if abs(dr) > abs(dc):
        if dr > 0:
            dr = 1
        else:
            dr = -1
        dc = 0
    else:
        if dc > 0:
            dc = 1
        else:
            dc = -1
        dr = 0
    for i in range(1, max(abs(dr), abs(dc)) + 1):
        r, c = joe_pos[0] + i * dr, joe_pos[1] + i * dc
        if r < 0 or r >= R or c < 0 or c >= C or maze[r][c] == '#':
            return False
    return True

def escape_time(maze):
    joe_pos = find_joe(maze)
    fire_pos = find_fire(maze)
    if not is_safe(maze, joe_pos, fire_pos):
        return 'IMPOSSIBLE'
    return abs(fire_pos[0] - joe_pos[0]) + abs(fire_pos[1] - joe_pos[1])

if __name__ == '__main__':
    R, C = map(int, input().split())
    maze = read_maze(R, C)
    print(escape_time(maze))

