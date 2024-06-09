
def solve(s):
    n = len(s)
    if n == 1:
        return 0
    substrings = []
    for i in range(n):
        for j in range(i, n):
            substrings.append(s[i:j+1])
    substrings = list(set(substrings))
    if len(substrings) == n:
        return 0
    changes = 0
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                changes += 1
                s = s[:i] + "a" + s[i+1:]
                break
    return changes

