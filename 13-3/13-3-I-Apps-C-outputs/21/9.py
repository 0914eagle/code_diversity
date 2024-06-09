
def solve(n, m):
    # Initialize a 2D array to store the number of chessmen placed in each cell
    chessmen = [[0] * m for _ in range(n)]

    # Initialize the maximum number of chessmen placed
    max_chessmen = 0

    # Loop through each cell in the chessboard
    for i in range(n):
        for j in range(m):
            # If the current cell is not already occupied
            if chessmen[i][j] == 0:
                # Place a chessman in the current cell and update the maximum number of chessmen placed
                chessmen[i][j] = 1
                max_chessmen += 1

                # Loop through the neighboring cells in all four directions (up, down, left, and right)
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        # If the neighboring cell is within the bounds of the chessboard and is not already occupied
                        if 0 <= i + di < n and 0 <= j + dj < m and chessmen[i + di][j + dj] == 0:
                            # Place a chessman in the neighboring cell and update the maximum number of chessmen placed
                            chessmen[i + di][j + dj] = 1
                            max_chessmen += 1

    return max_chessmen

