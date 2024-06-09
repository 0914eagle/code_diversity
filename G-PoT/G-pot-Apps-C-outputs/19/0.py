
def max_buildings_disarmed(R, C, grid):
    def can_disarm(row, col):
        for i in range(R):
            if i != row and grid[i][col] == 'x':
                return True
        for j in range(C):
            if j != col and grid[row][j] == 'x':
                return True
        return False

    count = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'x' and can_disarm(i, j):
                count += 1

    return count

# Read input
R, C = map(int, input().split())
grid = [input() for _ in range(R)]

# Call the function and print the output
print(max_buildings_disarmed(R, C, grid))
