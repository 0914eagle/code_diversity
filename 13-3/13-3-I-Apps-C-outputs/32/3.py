
def is_standardizable(n, s):
    colors = set(s)
    if len(colors) == 1:
        return True
    for color in colors:
        if s.count(color) < 2:
            return False
    return True

