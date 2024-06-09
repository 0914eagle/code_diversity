
def solve(s, p):
    n = len(s)
    count = [0] * 26
    for c in s:
        count[ord(c) - ord('a')] += 1
    max_cost = 0
    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                max_cost = max(max_cost, j - i + 1)
    for i in range(26):
        if count[i] > 0:
            max_cost = max(max_cost, count[i])
    return max_cost

