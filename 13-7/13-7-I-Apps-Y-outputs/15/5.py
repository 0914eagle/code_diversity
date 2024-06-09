
def solve(s, t):
    s_count = {}
    t_count = {}
    for c in s:
        if c not in s_count:
            s_count[c] = 1
        else:
            s_count[c] += 1
    for c in t:
        if c not in t_count:
            t_count[c] = 1
        else:
            t_count[c] += 1
    for c in s_count:
        if c not in t_count or s_count[c] > t_count[c]:
            return "No"
    for c in t_count:
        if c not in s_count or t_count[c] > s_count[c]:
            return "No"
    return "Yes"

