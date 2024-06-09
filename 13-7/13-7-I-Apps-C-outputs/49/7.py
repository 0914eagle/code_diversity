
def solve(s):
    suffixes = set()
    for i in range(len(s)-3, 0, -1):
        suffix = s[i:]
        if suffix not in suffixes:
            suffixes.add(suffix)
    return len(suffixes), *suffixes

