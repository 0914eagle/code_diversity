
n, m, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

def check_rectangles(table):
    rectangles = 0
    for i in range(n):
        for j in range(m):
            if table[i][j] == 1:
                rectangles += 1
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    if 0 <= x < n and 0 <= y < m and table[x][y] == 1:
                        table[x][y] = 0
                        stack.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])
    return rectangles

min_changes = float('inf')
for i in range(2**n):
    temp_table = [row.copy() for row in table]
    changes = 0
    for j in range(n):
        if (i >> j) & 1:
            changes += 1
            for l in range(m):
                temp_table[j][l] = 1 - temp_table[j][l]
    if check_rectangles(temp_table) <= k:
        min_changes = min(min_changes, changes)

if min_changes == float('inf'):
    print(-1)
else:
    print(min_changes)
