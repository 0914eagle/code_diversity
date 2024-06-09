
def is_standardizable(n, s):
    colors = set(s)
    if len(colors) == 1:
        return True
    for c in colors:
        if s.count(c) < 2:
            return False
    return True

