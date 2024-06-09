
def get_suffixes(s):
    suffixes = set()
    n = len(s)
    for i in range(2, 4):
        for j in range(n-i+1):
            if s[j:j+i] not in suffixes:
                suffixes.add(s[j:j+i])
    return len(suffixes), *suffixes

