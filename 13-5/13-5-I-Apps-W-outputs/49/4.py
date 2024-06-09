
def is_beautiful(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True


def solve(s):
    if "?" not in s:
        return s
    for i in range(s.count("?")):
        for c in "abc":
            if is_beautiful(s.replace("?", c, 1)):
                s = s.replace("?", c, 1)
                break
    if "?" in s:
        return "-1"
    return s

