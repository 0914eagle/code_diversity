
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

    # Loop through the target configuration and check if it is possible to reach it from the start configuration
    while queue:
        i, j = queue.pop(0)
        checked.add((i, j))
        num_pegs -= 1

        # Check if the current peg is in the target configuration
        if target_config[i][j] == "O":
            continue

        # Check if the current peg is in the target configuration
        if target_config[i][j] == "X":
            return 0

        # Check the neighbors of the current peg
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < r and 0 <= y < c and (x, y) not in checked:
                queue.append((x, y))
                num_pegs += 1

    # If all the pegs have been checked and the target configuration has not been reached, return 0
    if num_pegs == 0:
        return 0

    # If the target configuration has been reached, return 1
    return 1

def f2(...):
    ...

if __name__ == '__main__':
    r, c = map(int, input().split())
    start_config = [input() for _ in range(r)]
    target_config = [input() for _ in range(r)]
    print(f1(r, c, start_config, target_config))

