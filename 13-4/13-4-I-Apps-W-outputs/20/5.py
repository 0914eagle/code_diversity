
def f1(n, b, x, y):
    # Initialize a matrix to keep track of the bombs
    bombs = [[0] * n for _ in range(n)]
    for i in range(b):
        bombs[x[i] - 1][y[i] - 1] += 1

    # Initialize a queue to keep track of the cells to be processed
    queue = [(0, 0)]

    # Initialize a dictionary to keep track of the number of moves required to defuse each cell
    moves = {(0, 0): 0}

    # Loop until the queue is empty
    while queue:
        # Get the current cell from the queue
        x, y = queue.pop(0)

        # Check if the current cell is a bomb
        if bombs[x][y] > 0:
            # If the current cell is a bomb, decrement the number of bombs and update the moves required for the current cell
            bombs[x][y] -= 1
            moves[(x, y)] += 1

            # Add the neighboring cells to the queue if they are not already in the queue or have not been processed
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in queue and (nx, ny) not in moves:
                    queue.append((nx, ny))
                    moves[(nx, ny)] = moves[(x, y)] + 1

    # Return the minimum number of moves required to defuse all the bombs
    return moves[(n - 1, n - 1)]

def f2(n, b, x, y):
    # Initialize a matrix to keep track of the bombs
    bombs = [[0] * n for _ in range(n)]
    for i in range(b):
        bombs[x[i] - 1][y[i] - 1] += 1

    # Initialize a queue to keep track of the cells to be processed
    queue = [(0, 0)]

    # Initialize a dictionary to keep track of the number of moves required to defuse each cell
    moves = {(0, 0): 0}

    # Loop until the queue is empty
    while queue:
        # Get the current cell from the queue
        x, y = queue.pop(0)

        # Check if the current cell is a bomb
        if bombs[x][y] > 0:
            # If the current cell is a bomb, decrement the number of bombs and update the moves required for the current cell
            bombs[x][y] -= 1
            moves[(x, y)] += 1

            # Add the neighboring cells to the queue if they are not already in the queue or have not been processed
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in queue and (nx, ny) not in moves:
                    queue.append((nx, ny))
                    moves[(nx, ny)] = moves[(x, y)] + 1

    # Return the minimum number of moves required to defuse all the bombs
    return moves[(n - 1, n - 1)]

if __name__ == '__main__':
    n, b = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    print(f1(n, b, x, y))
    print(f2(n, b, x, y))

