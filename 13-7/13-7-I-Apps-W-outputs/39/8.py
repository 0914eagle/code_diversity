
def solve(s):
    n = len(s)
    substrings = set()
    for i in range(n):
        for j in range(i, n):
            substrings.add(s[i:j+1])
    if len(substrings) == n:
        return 0
    else:
        changes = 0
        for i in range(n-1):
            if s[i] == s[i+1]:
                changes += 1
                s = s[:i+1] + 'a' + s[i+2:]
        return changes

