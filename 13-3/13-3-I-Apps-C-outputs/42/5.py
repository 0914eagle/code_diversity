
def f1(r, c, start_config, target_config):
    # Initialize a 2D array to store the current state of the board
    board = [[0] * c for _ in range(r)]

    # Initialize a queue to store the positions of the pegs that need to be checked
    queue = []

    # Initialize a set to store the positions of the pegs that have already been checked
    checked = set()

    # Initialize a variable to store the number of pegs that need to be checked
    num_pegs = 0

    # Loop through the starting configuration and set the initial state of the board
    for i in range(r):
        for j in range(c):
            if start_config[i][j] == "O":
                board[i][j] = 1
                queue.append((i, j))
                checked.add((i, j))
                num_pegs += 1

    # Loop through the queue and check if the current peg can be raised
    while queue:
        i, j = queue.pop(0)
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < r and 0 <= y < c and board[x][y] == 0 and (x, y) not in checked:
                board[x][y] = 1
                queue.append((x, y))
                checked.add((x, y))
                num_pegs += 1

    # Check if all the pegs in the target configuration are up
    for i in range(r):
        for j in range(c):
            if target_config[i][j] == "O" and board[i][j] == 0:
                return 0

    # If all the pegs in the target configuration are up, return 1
    return 1

def f2(...):
    ...

if __name__ == '__main__':
    r, c = map(int, input().split())
    start_config = [input() for _ in range(r)]
    target_config = [input() for _ in range(r)]
    print(f1(r, c, start_config, target_config))

