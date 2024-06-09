
H, W, K = map(int, input().split())
grid = [list(input()) for _ in range(H)]

count = 0
for i in range(2 ** H):
    for j in range(2 ** W):
        black_squares = 0
        for row in range(H):
            for col in range(W):
                if (i >> row) & 1 == 0 and (j >> col) & 1 == 0 and grid[row][col] == '#':
                    black_squares += 1
        if black_squares == K:
            count += 1

print(count)
