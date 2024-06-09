
n, m, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

def check_rectangles(table):
    count_changes = 0
    for i in range(n):
        for j in range(m):
            if table[i][j] == 1:
                for h in range(1, n-i+1):
                    for w in range(1, m-j+1):
                        if i+h > n or j+w > m:
                            break
                        valid_rect = True
                        for x in range(i, i+h):
                            for y in range(j, j+w):
                                if table[x][y] != 1:
                                    valid_rect = False
                                    break
                            if not valid_rect:
                                break
                        if valid_rect:
                            count_changes = max(count_changes, h*w)
    return count_changes

min_changes = float('inf')
for i in range(n):
    for j in range(m):
        temp_table = [row[:] for row in table]
        temp_table[i][j] = 1 - temp_table[i][j]
        min_changes = min(min_changes, check_rectangles(temp_table))

if min_changes <= k:
    print(min_changes)
else:
    print(-1)
