
def count_choices(H, W, K, grid):
    total_black = sum(row.count('#') for row in grid)
    ans = 0
    for row_mask in range(1 << H):
        for col_mask in range(1 << W):
            black_count = 0
            for i in range(H):
                for j in range(W):
                    if (row_mask >> i) & 1 or (col_mask >> j) & 1:
                        if grid[i][j] == '#':
                            black_count += 1
            if total_black - black_count == K:
                ans += 1
    return ans

H, W, K = map(int, input().split())
grid = [input() for _ in range(H)]

print(count_choices(H, W, K, grid))
