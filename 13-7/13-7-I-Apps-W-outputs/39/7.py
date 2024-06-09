
def solve(s):
    n = len(s)
    substrings = []
    for i in range(n):
        for j in range(i, n):
            substrings.append(s[i:j+1])
    substrings = list(set(substrings))
    if len(substrings) == len(s) + 1:
        return 0
    else:
        return 1

