
def get_happy_seconds(n, x, y, c):
    # Initialize a 2D array to store the state of the table
    table = [[0] * n for _ in range(n)]
    table[x - 1][y - 1] = 1
    seconds = 0
    while True:
        # Iterate over the table and check if the condition is met
        if sum(map(sum, table)) >= c:
            break
        # Switch on the cells that are off but have side-adjacent cells that are on
        for i in range(n):
            for j in range(n):
                if table[i][j] == 0 and sum(table[i - 1][j], table[i + 1][j], table[i][j - 1], table[i][j + 1]) >= 3:
                    table[i][j] = 1
        seconds += 1
    return seconds

