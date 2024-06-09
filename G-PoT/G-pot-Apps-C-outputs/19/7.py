
def max_disarmed_buildings(R, C, grid):
    def can_disarm(i, j):
        for k in range(R):
            if grid[k][j] == 'x' and (k != i or j != j):
                return True
        for k in range(C):
            if grid[i][k] == 'x' and (i != i or k != j):
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

# Calculate and print the maximum number of disarmed buildings
print(max_disarmed_buildings(R, C, grid))
