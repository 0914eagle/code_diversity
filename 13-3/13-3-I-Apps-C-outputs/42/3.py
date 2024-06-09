
def f1(r, c, start_config, target_config):
    # Initialize a 2D array to store the current state of the board
    board = [[0] * c for _ in range(r)]

    # Initialize a queue to store the positions of the pegs that need to be checked
    queue = []

    # Initialize a set to store the positions of the pegs that have already been checked
    checked = set()

    # Initialize a variable to store the number of pegs that need to be checked
    num_pegs = 0

    # Loop through the start configuration and initialize the board and queue
    for i in range(r):
        for j in range(c):
            if start_config[i][j] == "O":
                board[i][j] = 1
                queue.append((i, j))
                num_pegs += 1

    # Loop through the queue and check if the target configuration can be reached
    while queue:
        i, j = queue.pop(0)
        if board[i][j] == 1:
            board[i][j] = 0
            num_pegs -= 1
            for x in range(max(i-1, 0), min(i+2, r)):
                for y in range(max(j-1, 0), min(j+2, c)):
                    if board[x][y] == 1 and (x, y) not in checked:
                        queue.append((x, y))
                        checked.add((x, y))

    # If all the pegs have been checked and the target configuration has been reached, return 1
    if num_pegs == 0 and target_config == "".join(["".join(map(str, row)) for row in board]):
        return 1

    # Otherwise, return 0
    return 0

def f2(...):
    ...

if __name__ == '__main__':
    r, c = map(int, input().split())
    start_config = [input() for _ in range(r)]
    target_config = [input() for _ in range(r)]
    print(f1(r, c, start_config, target_config))

