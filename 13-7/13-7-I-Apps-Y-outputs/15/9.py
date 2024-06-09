
def is_lexicographically_smaller(s, t):
    if len(s) < len(t):
        return True
    if len(s) > len(t):
        return False
    for i in range(len(s)):
        if s[i] < t[i]:
            return True
        if s[i] > t[i]:
            return False
    return False

