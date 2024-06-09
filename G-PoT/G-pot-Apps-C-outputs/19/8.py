
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
            disarmed = rows[i] + cols[j]
            if grid[i][j] == 'x':
                disarmed -= 1
            max_disarmed = max(max_disarmed, disarmed)

    return max_disarmed

# Input
R, C = map(int, input().split())
grid = [input() for _ in range(R)]

# Output
print(max_disarmed_buildings(R, C, grid))
