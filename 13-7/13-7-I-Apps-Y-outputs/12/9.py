
def solve(s, t):
    sticky_keys = []
    for i in range(len(s)):
        if s[i] != t[i]:
            sticky_keys.append(s[i])
    return "".join(sticky_keys)

