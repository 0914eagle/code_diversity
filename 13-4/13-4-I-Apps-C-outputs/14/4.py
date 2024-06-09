
def solve(a, s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if int(s[i] + s[j] + s[k] + s[l]) == a:
                        count += 1
    return count

