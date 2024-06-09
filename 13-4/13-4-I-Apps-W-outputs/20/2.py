
def f1(N, B, x, y):
    # Initialize a dictionary to store the positions of the bombs
    bombs = {}
    for i in range(B):
        bombs[i] = (x[i], y[i])

    # Initialize a queue to store the positions of the bombs that need to be moved
    queue = []

    # Loop through each bomb and check if it is in the corner
    for i in range(B):
        pos = bombs[i]
        if pos in [(1, 1), (1, N), (N, 1), (N, N)]:
            # If the bomb is in the corner, remove it from the dictionary
            del bombs[i]
        else:
            # If the bomb is not in the corner, add it to the queue
            queue.append(pos)

    # Initialize a variable to store the number of moves
    moves = 0

    # Loop through the queue and move the bombs to the corner
    while queue:
        pos = queue.pop(0)
        x, y = pos
        if x == 1 and y == 1:
            moves += 1
        elif x == 1 and y == N:
            moves += 1
        elif x == N and y == 1:
            moves += 1
        elif x == N and y == N:
            moves += 1
        else:
            # If the bomb is not in the corner, move it to the nearest corner
            if x == 1:
                moves += 1
                x = N
            elif x == N:
                moves += 1
                x = 1
            elif y == 1:
                moves += 1
                y = N
            else:
                moves += 1
                y = 1
            queue.append((x, y))

    return moves

def f2(N, B, x, y):
    # Initialize a dictionary to store the positions of the bombs
    bombs = {}
    for i in range(B):
        bombs[i] = (x[i], y[i])

    # Initialize a queue to store the positions of the bombs that need to be moved
    queue = []

    # Loop through each bomb and check if it is in the corner
    for i in range(B):
        pos = bombs[i]
        if pos in [(1, 1), (1, N), (N, 1), (N, N)]:
            # If the bomb is in the corner, remove it from the dictionary
            del bombs[i]
        else:
            # If the bomb is not in the corner, add it to the queue
            queue.append(pos)

    # Initialize a variable to store the number of moves
    moves = 0

    # Loop through the queue and move the bombs to the corner
    while queue:
        pos = queue.pop(0)
        x, y = pos
        if x == 1 and y == 1:
            moves += 1
        elif x == 1 and y == N:
            moves += 1
        elif x == N and y == 1:
            moves += 1
        elif x == N and y == N:
            moves += 1
        else:
            # If the bomb is not in the corner, move it to the nearest corner
            if x == 1:
                moves += 1
                x = N
            elif x == N:
                moves += 1
                x = 1
            elif y == 1:
                moves += 1
                y = N
            else:
                moves += 1
                y = 1
            queue.append((x, y))

    return moves

if __name__ == '__main__':
    N, B = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    print(f1(N, B, x, y))
    print(f2(N, B, x, y))

