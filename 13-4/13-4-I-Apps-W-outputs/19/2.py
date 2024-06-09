
def get_maze_size(maze_str):
    return tuple(map(int, maze_str.split()))

def get_maze_matrix(maze_str):
    maze_size = get_maze_size(maze_str)
    maze_matrix = []
    for i in range(maze_size[0]):
        maze_matrix.append(list(maze_str[i * maze_size[1] + 1:(i + 1) * maze_size[1] + 1]))
    return maze_matrix

def get_starting_and_goal_squares(maze_matrix):
    for i in range(len(maze_matrix)):
        for j in range(len(maze_matrix[i])):
            if maze_matrix[i][j] == 'S':
                return (i, j), (len(maze_matrix) - 1 - i, len(maze_matrix[i]) - 1 - j)
    return None, None

def get_moves_to_goal(maze_matrix, starting_square, goal_square):
    visited = set()
    queue = [(starting_square, 0)]
    while queue:
        current_square, moves = queue.pop(0)
        if current_square == goal_square:
            return moves
        for i in range(max(current_square[0] - 1, 0), min(current_square[0] + 2, len(maze_matrix))):
            for j in range(max(current_square[1] - 1, 0), min(current_square[1] + 2, len(maze_matrix[0]))):
                if (i, j) not in visited and maze_matrix[i][j] == '.':
                    visited.add((i, j))
                    queue.append(((i, j), moves + 1))
    return -1

def solve(maze_str):
    maze_matrix = get_maze_matrix(maze_str)
    starting_square, goal_square = get_starting_and_goal_squares(maze_matrix)
    return get_moves_to_goal(maze_matrix, starting_square, goal_square)

if __name__ == '__main__':
    maze_str = input()
    print(solve(maze_str))

