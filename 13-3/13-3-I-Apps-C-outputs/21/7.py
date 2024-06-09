
def solve(n, m):
    # Initialize a 2D array to store the number of chessmen placed in each cell
    chessmen = [[0] * m for _ in range(n)]

    # Initialize the maximum number of chessmen placed to 0
    max_chessmen = 0

    # Loop through each row
    for i in range(n):
        # Loop through each column
        for j in range(m):
            # Check if the current cell is empty
            if chessmen[i][j] == 0:
                # Place a chessman in the current cell
                chessmen[i][j] = 1
                # Increment the maximum number of chessmen placed
                max_chessmen += 1
                # Loop through the neighboring cells in the Manhattan distance of 3
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        # Check if the neighboring cell is within the bounds of the chessboard and empty
                        if 0 <= x < n and 0 <= y < m and chessmen[x][y] == 0:
                            # Place a chessman in the neighboring cell
                            chessmen[x][y] = 1
                            # Increment the maximum number of chessmen placed
                            max_chessmen += 1

    return max_chessmen

