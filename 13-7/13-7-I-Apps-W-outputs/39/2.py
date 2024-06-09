
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
        # find the longest common prefix of all substrings
        lcp = ""
        for i in range(len(substrings[0])):
            for j in range(1, len(substrings)):
                if substrings[0][i] != substrings[j][i]:
                    return -1
            lcp += substrings[0][i]
        # find the number of changes needed to make all substrings distinct
        changes = 0
        for substring in substrings:
            changes += len(substring) - len(lcp)
        return changes

