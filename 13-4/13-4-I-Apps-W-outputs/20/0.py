
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
        current_cell = queue.pop(0)

        # Get the number of bombs at the current cell
        num_bombs = matrix[current_cell[0]][current_cell[1]]

        # If the current cell has no bombs, we can move to the next cell
        if num_bombs == 0:
            continue

        # If the current cell has only one bomb, we can defuse it and move to the next cell
        if num_bombs == 1:
            matrix[current_cell[0]][current_cell[1]] -= 1
            continue

        # If the current cell has more than one bomb, we need to move one bomb to a corner cell
        for corner in [(0, 0), (0, n - 1), (n - 1, 0), (n - 1, n - 1)]:
            # If the corner cell has no bombs, we can move a bomb to it and defuse it
            if matrix[corner[0]][corner[1]] == 0:
                matrix[current_cell[0]][current_cell[1]] -= 1
                matrix[corner[0]][corner[1]] += 1
                moves[corner] = moves[current_cell] + 1
                queue.append(corner)
                break

    # Return the minimum number of moves required to defuse all the bombs
    return moves[(n - 1, n - 1)]

def main():
    n, b = map(int, input().split())
    bombs = []
    for _ in range(b):
        x, y = map(int, input().split())
        bombs.append((x, y))
    print(get_min_moves(n, bombs))

if __name__ == '__main__':
    main()

