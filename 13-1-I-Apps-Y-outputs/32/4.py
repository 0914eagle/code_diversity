
def find_content_children(g, s):
    g.sort()
    s.sort()
    i, j = 0, 0
    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            i += 1
        j += 1
    return i

