
def solve(s):
    suffixes = set()
    for i in range(len(s)-3, len(s)):
        suffix = s[i:]
        if suffix not in suffixes:
            suffixes.add(suffix)
    return len(suffixes), *suffixes

