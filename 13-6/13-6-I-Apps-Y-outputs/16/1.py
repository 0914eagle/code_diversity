
def is_coffee_like(s):
    if len(s) != 6:
        return False
    if s[2] != s[3]:
        return False
    if s[4] != s[5]:
        return False
    return True

