
n, m, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

def check_rectangle(i, j, h, w):
    ones = 0
    zeros = 0
    for x in range(i, i+h):
        for y in range(j, j+w):
            if table[x][y] == 1:
                ones += 1
            else:
                zeros += 1
    return ones == h*w or zeros == h*w

def count_changes(i, j, h, w):
    ones = 0
    zeros = 0
    for x in range(i, i+h):
        for y in range(j, j+w):
            if table[x][y] == 1:
                ones += 1
            else:
                zeros += 1
    return min(ones, zeros)

min_changes = float('inf')
for i in range(n):
    for j in range(m):
        for h in range(1, n-i+1):
            for w in range(1, m-j+1):
                if h*w <= k and check_rectangle(i, j, h, w):
                    min_changes = min(min_changes, count_changes(i, j, h, w))

if min_changes == float('inf'):
    print(-1)
else:
    print(min_changes)
