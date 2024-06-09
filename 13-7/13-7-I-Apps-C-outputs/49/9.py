
def get_suffixes(s):
    suffixes = set()
    n = len(s)
    for i in range(n-2, 0, -1):
        if s[i] != s[i+1] and s[i] != s[i+2]:
            suffixes.add(s[i:i+3])
    return len(suffixes), *suffixes

