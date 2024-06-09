
def get_suffixes(s):
    suffixes = set()
    for i in range(len(s) - 2):
        suffix = s[i:]
        if len(suffix) == 2 or len(suffix) == 3:
            suffixes.add(suffix)
    return suffixes

