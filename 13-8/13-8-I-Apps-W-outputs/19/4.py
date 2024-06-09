
def solve(n, v, sellers):
    p = 0
    q = []
    for i in range(n):
        for j in range(sellers[i]):
            if v >= s[i][j]:
                p += 1
                q.append(i+1)
                break
    return p, q

