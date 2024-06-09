
def is_beautiful(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True


def solve(s):
    if "?" not in s:
        return s
    for i in range(len(s)):
        if s[i] == "?":
            for c in "abc":
                if is_beautiful(s[:i] + c + s[i + 1:]):
                    return solve(s[:i] + c + s[i + 1:])
    return -1

