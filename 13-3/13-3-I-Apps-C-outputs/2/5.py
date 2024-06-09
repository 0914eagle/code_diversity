
def solve(s, l, r):
    n = len(s)
    count = 0
    for i in range(l-1, r):
        if s[i] != s[i-1] and s[i] != s[i-2]:
            count += 1
    return count

