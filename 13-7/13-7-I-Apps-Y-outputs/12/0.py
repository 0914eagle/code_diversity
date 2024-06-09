
def sticky_keys(s, t):
    sticky_chars = []
    for i in range(len(s)):
        if s[i] != t[i]:
            sticky_chars.append(s[i])
    return "".join(sticky_chars)

