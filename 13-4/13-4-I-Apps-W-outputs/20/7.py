
def f1(N, B, x, y):
    # Initialize a 2D array to represent the matrix
    matrix = [[0] * N for _ in range(N)]

    # Place the bombs in the matrix
    for i in range(B):
        matrix[x[i] - 1][y[i] - 1] += 1

    # Initialize a queue to store the positions of the bombs to be defused
    queue = [(x[i], y[i]) for i in range(B)]

    # Initialize a variable to store the number of moves required
    moves = 0

    # Loop until the queue is empty
    while queue:
        # Get the position of the current bomb from the queue
        x, y = queue.pop(0)

        # Check if the current bomb is in the corner of the matrix
        if x in [1, N] and y in [1, N]:
            # If it is, defuse it and continue to the next bomb
            matrix[x - 1][y - 1] -= 1
            continue

        # Check if the current bomb has already been defused
        if matrix[x - 1][y - 1] == 0:
            # If it has, continue to the next bomb
            continue

        # Otherwise, find the four adjacent cells that can be reached from the current bomb
        adjacents = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

        # Loop through the adjacent cells
        for adjacent in adjacents:
            # Check if the current cell is within the bounds of the matrix
            if 0 < adjacent[0] <= N and 0 < adjacent[1] <= N:
                # If it is, check if the current cell has a bomb
                if matrix[adjacent[0] - 1][adjacent[1] - 1] > 0:
                    # If it does, add it to the queue
                    queue.append(adjacent)

        # Increment the number of moves required
        moves += 1

        # Defuse the current bomb
        matrix[x - 1][y - 1] -= 1

    return moves

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    N, B = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    print(f1(N, B, x, y))

