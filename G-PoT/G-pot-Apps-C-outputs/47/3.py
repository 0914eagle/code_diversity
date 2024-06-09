
n, m, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

def check_rectangular(table):
    for i in range(n):
        for j in range(m):
            if table[i][j] == 1:
                for x in range(i, n):
                    for y in range(j, m):
                        if table[x][y] == 0:
                            return False
                            break
                        for a in range(i, x+1):
                            for b in range(j, y+1):
                                if table[a][b] == 0:
                                    return False
                                    break
    return True

def change_cells(table, k):
    count = 0
    for i in range(n):
        for j in range(m):
            if table[i][j] == 0:
                count += 1
    return min(count, k)

if check_rectangular(table):
    print(change_cells(table, k))
else:
    print(-1)
