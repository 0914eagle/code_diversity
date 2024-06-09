
H, W, K = map(int, input().split())
grid = [input() for _ in range(H)]

ans = 0
for row_mask in range(1 << H):
    for col_mask in range(1 << W):
        black_count = 0
        for i in range(H):
            for j in range(W):
                if (row_mask >> i) & 1 == 0 and (col_mask >> j) & 1 == 0 and grid[i][j] == '#':
                    black_count += 1
        if black_count == K:
            ans += 1

print(ans)
