
def get_maze_size(maze_string):
    return tuple(map(int, maze_string.split()))

def get_maze_matrix(maze_string):
    maze_size = get_maze_size(maze_string)
    maze_matrix = []
    for i in range(maze_size[0]):
        maze_matrix.append(list(maze_string[i * maze_size[1] + 1:(i + 1) * maze_size[1] + 1]))
    return maze_matrix

def get_starting_and_goal_squares(maze_matrix):
    for i in range(len(maze_matrix)):
        for j in range(len(maze_matrix[i])):
            if maze_matrix[i][j] == 'S':
                starting_square = (i, j)
            if maze_matrix[i][j] == 'G':
                goal_square = (i, j)
    return starting_square, goal_square

def get_moves_to_goal(maze_matrix, starting_square, goal_square):
    moves = 0
    queue = [(starting_square, 0)]
    visited = set()
    while queue:
        current_square, moves = queue.pop(0)
        if current_square == goal_square:
            return moves
        for i in range(len(maze_matrix)):
            for j in range(len(maze_matrix[i])):
                if maze_matrix[i][j] == '.' and (i, j) not in visited:
                    queue.append(((i, j), moves + 1))
                    visited.add((i, j))
    return -1

def get_maximum_possible_moves(maze_string):
    maze_matrix = get_maze_matrix(maze_string)
    starting_square, goal_square = get_starting_and_goal_squares(maze_matrix)
    return get_moves_to_goal(maze_matrix, starting_square, goal_square)

if __name__ == '__main__':
    maze_string = input()
    print(get_maximum_possible_moves(maze_string))

