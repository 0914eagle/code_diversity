
def get_min_moves(n, bombs):
    # Initialize a matrix to keep track of the number of bombs at each cell
    matrix = [[0] * n for _ in range(n)]
    for bomb in bombs:
        matrix[bomb[0] - 1][bomb[1] - 1] += 1

    # Initialize a queue to keep track of the cells to be processed
    queue = [(0, 0)]

    # Initialize a dictionary to keep track of the number of moves required to reach each cell
    moves = {(0, 0): 0}

    # Loop until the queue is empty
    while queue:
        # Get the current cell from the queue
        curr_cell = queue.pop(0)

        # Get the number of bombs at the current cell
        num_bombs = matrix[curr_cell[0]][curr_cell[1]]

        # If the current cell has no bombs, we can move to the next cell
        if num_bombs == 0:
            continue

        # If the current cell has bombs, we need to move them to the four corners
        for i in range(4):
            # Get the next cell in the given direction
            next_cell = get_next_cell(curr_cell, i)

            # If the next cell is a corner, we can move the bombs to that cell
            if is_corner(next_cell):
                matrix[next_cell[0]][next_cell[1]] += num_bombs
                moves[next_cell] = moves[curr_cell] + 1
                queue.append(next_cell)

    # Return the minimum number of moves required to defuse all the bombs
    return min(moves.values())

def get_next_cell(cell, direction):
    # Get the next cell in the given direction
    if direction == 0:
        next_cell = (cell[0] - 1, cell[1])
    elif direction == 1:
        next_cell = (cell[0] + 1, cell[1])
    elif direction == 2:
        next_cell = (cell[0], cell[1] - 1)
    else:
        next_cell = (cell[0], cell[1] + 1)

    # Return the next cell
    return next_cell

def is_corner(cell):
    # Check if the cell is a corner
    return cell[0] == 0 or cell[0] == n - 1 or cell[1] == 0 or cell[1] == n - 1

if __name__ == '__main__':
    n, b = map(int, input().split())
    bombs = []
    for _ in range(b):
        x, y = map(int, input().split())
        bombs.append((x, y))
    print(get_min_moves(n, bombs))

