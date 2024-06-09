
# Read input
H, W, K = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

# Initialize count variable
count = 0

# Iterate through all possible combinations of rows and columns
for row_mask in range(1 << H):
    for col_mask in range(1 << W):
        black_count = 0
        for i in range(H):
            for j in range(W):
                if (row_mask >> i) & 1 == 0 and (col_mask >> j) & 1 == 0 and grid[i][j] == '#':
                    black_count += 1
        if black_count == K:
            count += 1

print(count)