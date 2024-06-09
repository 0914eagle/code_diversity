
def solve(k, s):
    if len(s) <= k:
        return s
    else:
        return s[:k] + "..."

