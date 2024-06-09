
def solve(s):
    n = len(s)
    count = 0
    for i in range(n):
        if s[i] == 'w':
            count += n - i
        elif s[i] == 'm':
            count += n - i
        else:
            count += 1
    return count % (10**9 + 7)

