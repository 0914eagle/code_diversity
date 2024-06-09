
def get_suffixes(s):
    suffixes = set()
    for i in range(len(s) - 2, 0, -1):
        if s[i] != s[i - 1] and s[i] != s[i - 2]:
            suffixes.add(s[i:])
    return len(suffixes), *suffixes

