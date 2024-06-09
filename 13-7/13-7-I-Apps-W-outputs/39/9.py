
def solve(s):
    n = len(s)
    substrings = set()
    for i in range(n):
        for j in range(i, n):
            substrings.add(s[i:j+1])
    if len(substrings) == len(s):
        return 0
    else:
        # Find the longest common prefix of all substrings
        lcp = ""
        for i in range(n):
            for substring in substrings:
                if substring[i] != s[i]:
                    break
            else:
                lcp += s[i]
        # Find the number of changes needed to make all substrings distinct
        changes = 0
        for substring in substrings:
            if substring.startswith(lcp):
                changes += 1
        return changes

