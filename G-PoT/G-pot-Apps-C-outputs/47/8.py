
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

def find_min_changes():
    min_changes = float('inf')
    for i in range(n):
        for j in range(m):
            for h in range(1, n-i+1):
                for w in range(1, m-j+1):
                    if h*w > min_changes:
                        break
                    if check_rectangle(i, j, h, w):
                        min_changes = min(min_changes, h*w)
    return min_changes if min_changes != float('inf') else -1

print(find_min_changes())
