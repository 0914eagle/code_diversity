
def get_maze_size(maze_string):
    return tuple(map(int, maze_string.split()))

def get_maze_array(maze_string):
    return [[char for char in line] for line in maze_string.splitlines()]

def get_starting_goal_squares(maze_array):
    for i in range(len(maze_array)):
        for j in range(len(maze_array[0])):
            if maze_array[i][j] == '.':
                return (i, j), (len(maze_array) - 1 - i, len(maze_array[0]) - 1 - j)

def get_moves(maze_array, starting_square, goal_square):
    visited = set()
    queue = [(starting_square, 0)]
    while queue:
        current_square, distance = queue.pop(0)
        if current_square == goal_square:
            return distance
        visited.add(current_square)
        for neighbor in get_neighbors(maze_array, current_square):
            if neighbor not in visited and maze_array[neighbor[0]][neighbor[1]] == '.':
                queue.append((neighbor, distance + 1))
    return -1

def get_neighbors(maze_array, square):
    i, j = square
    neighbors = []
    if i > 0 and maze_array[i - 1][j] == '.':
        neighbors.append((i - 1, j))
    if i < len(maze_array) - 1 and maze_array[i + 1][j] == '.':
        neighbors.append((i + 1, j))
    if j > 0 and maze_array[i][j - 1] == '.':
        neighbors.append((i, j - 1))
    if j < len(maze_array[0]) - 1 and maze_array[i][j + 1] == '.':
        neighbors.append((i, j + 1))
    return neighbors

def solve_maze(maze_string):
    maze_size = get_maze_size(maze_string)
    maze_array = get_maze_array(maze_string)
    starting_square, goal_square = get_starting_goal_squares(maze_array)
    return get_moves(maze_array, starting_square, goal_square)

if __name__ == '__main__':
    maze_string = 
    print(solve_maze(maze_string))

