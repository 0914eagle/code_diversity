
def get_suffixes(s):
    suffixes = set()
    n = len(s)
    for i in range(2, n+1):
        for j in range(0, n-i+1):
            if s[j:j+i] not in suffixes:
                suffixes.add(s[j:j+i])
    return len(suffixes), *suffixes

