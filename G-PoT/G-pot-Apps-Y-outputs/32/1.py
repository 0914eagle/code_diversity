
# Read input
H, W, K = map(int, input().split())
grid = [input() for _ in range(H)]

# Count the number of black squares
total_black = sum(row.count("#") for row in grid)

# Initialize the count of valid choices
count = 0

# Loop through all possible combinations of rows and columns
for row_mask in range(1 << H):
    for col_mask in range(1 << W):
        black_count = 0
        for i in range(H):
            for j in range(W):
                if (row_mask >> i) & 1 == 0 and (col_mask >> j) & 1 == 0 and grid[i][j] == "#":
                    black_count += 1
        if black_count == total_black - K:
            count += 1

print(count)
