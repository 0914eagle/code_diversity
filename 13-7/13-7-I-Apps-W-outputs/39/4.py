
def solve(s):
    n = len(s)
    substrings = []
    for i in range(n):
        for j in range(i, n):
            substrings.append(s[i:j+1])
    substrings = list(set(substrings))
    if len(substrings) == len(s):
        return 0
    else:
        changes = 0
        for i in range(n):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    changes += 1
                    s = s[:i] + "a" + s[i+1:]
                    break
        return changes

