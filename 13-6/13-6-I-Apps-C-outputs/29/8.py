
def get_maze_size(maze):
    return len(maze), len(maze[0])

def get_starting_position(maze):
    for row in maze:
        for col in row:
            if col == "J":
                return row.index(col), maze.index(row)

def get_fire_position(maze):
    for row in maze:
        for col in row:
            if col == "F":
                return row.index(col), maze.index(row)

def is_safe_position(maze, row, col):
    return maze[row][col] != "F" and maze[row][col] != "#"

def find_path(maze, row, col, time):
    if not is_safe_position(maze, row, col):
        return -1
    if row == 0 or col == 0 or row == len(maze) - 1 or col == len(maze[0]) - 1:
        return time
    min_time = float("inf")
    for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
        if is_safe_position(maze, r, c):
            t = find_path(maze, r, c, time + 1)
            if t != -1 and t < min_time:
                min_time = t
    return min_time

def solve(maze):
    rows, cols = get_maze_size(maze)
    start_row, start_col = get_starting_position(maze)
    fire_row, fire_col = get_fire_position(maze)
    time = find_path(maze, start_row, start_col, 0)
    if time == -1:
        return "IMPOSSIBLE"
    return time

if __name__ == '__main__':
    maze = [
        list("####"),
        list("#JF#"),
        list("#..#"),
        list("#..#")
    ]
    print(solve(maze))

