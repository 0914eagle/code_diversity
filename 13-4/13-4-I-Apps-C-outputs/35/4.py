
def solve(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if s[i] == s[j] == s[k]:
                    count += 1
    return count
