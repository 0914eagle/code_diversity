
def get_maze_size(maze_string):
    return tuple(map(int, maze_string.split()))

def get_maze_squares(maze_string):
    return maze_string.split()

def get_starting_square(maze_squares):
    for i, square in enumerate(maze_squares):
        if square == '..':
            return i

def get_goal_square(maze_squares):
    for i, square in enumerate(maze_squares):
        if square == '..':
            return i

def get_moves_to_goal(starting_square, goal_square):
    moves = 0
    current_square = starting_square
    while current_square != goal_square:
        moves += 1
        current_square = (current_square + 1) % len(maze_squares)
    return moves

def get_maximum_moves(maze_string):
    maze_size = get_maze_size(maze_string)
    maze_squares = get_maze_squares(maze_string)
    starting_square = get_starting_square(maze_squares)
    goal_square = get_goal_square(maze_squares)
    return get_moves_to_goal(starting_square, goal_square)

if __name__ == '__main__':
    maze_string = input()
    print(get_maximum_moves(maze_string))

