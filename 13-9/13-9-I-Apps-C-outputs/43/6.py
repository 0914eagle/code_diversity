
def solve(a, b, p):
    n = len(a)
    m = len(b)
    count = 0
    for i in range(n - m + 1):
        flag = True
        for j in range(m):
            if a[i + j] != b[j]:
                flag = False
                break
        if flag:
            count += 1
    return count

