
def max_disarmed_buildings(R, C, grid):
    rows = [0] * R
    cols = [0] * C

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'x':
                rows[i] += 1
                cols[j] += 1

    max_disarmed = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '.' and (rows[i] > 0 or cols[j] > 0):
                max_disarmed += 1

    return max_disarmed

# Read input
R, C = map(int, input().split())
grid = [input() for _ in range(R)]

# Call the function and print the result
print(max_disarmed_buildings(R, C, grid))
