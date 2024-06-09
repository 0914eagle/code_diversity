
def is_hq9_plus(string):
    return any(string.count(c) > 1 for c in "HQ9+")

