
def solve(a, b, s):
    n = len(a)
    m = len(s)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            substr1 = a[i:j+1]
            for k in range(n):
                for l in range(k+1, n):
                    substr2 = b[k:l+1]
                    if substr1 + substr2 == s:
                        count += 1
    return count

