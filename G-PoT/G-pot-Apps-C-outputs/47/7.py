
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
    return ones <= k and zeros <= k

def check_valid_rectangle(i, j, h, w):
    ones = 0
    zeros = 0
    for x in range(i, i+h):
        for y in range(j, j+w):
            if table[x][y] == 1:
                ones += 1
            else:
                zeros += 1
    return ones == 0 or zeros == 0

def solve():
    min_changes = float('inf')
    for i in range(n):
        for j in range(m):
            for h in range(1, n-i+1):
                for w in range(1, m-j+1):
                    if check_valid_rectangle(i, j, h, w):
                        if check_rectangle(i, j, h, w):
                            min_changes = min(min_changes, sum(row[j:j+w]).count(1) + sum(row[j:j+w]).count(0) - h * w)
    return min_changes if min_changes != float('inf') else -1

print(solve())
