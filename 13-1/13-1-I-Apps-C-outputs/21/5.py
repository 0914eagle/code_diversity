
import sys
input = sys.stdin.read()
n, m = map(int, input.split())

matrix = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, input.split())
    matrix[x][y] = 1

def find_path(start, end):
    if start == end:
        return 0
    
    x, y = start
    for i in range(x + 1, n + 1):
        for j in range(y + 1, n + 1):
            if matrix[i][j] == 0:
                matrix[i][j] = matrix[x][y] + 1
                if find_path((i, j), end) == 1:
                    return 1
                matrix[i][j] = 0
    return 0

if find_path((1, 1), (n, n)) == 1:
    print(matrix[n][n])
else:
    print(-1)

