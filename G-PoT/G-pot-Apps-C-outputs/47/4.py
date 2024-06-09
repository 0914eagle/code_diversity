
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

def check_valid():
    for i in range(n):
        for j in range(m):
            for h in range(1, n-i+1):
                for w in range(1, m-j+1):
                    if check_rectangle(i, j, h, w):
                        return True
    return False

if check_valid():
    print(0)
else:
    print(-1)
