
def get_min_nubs(mark):
    n, m = map(int, input().split())
    mark = [input() for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if mark[i][j] == '#':
                count += 1
    return count

