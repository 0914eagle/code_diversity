
def get_ans(s, p):
    n = len(s)
    occ = [0] * (n + 1)
    for i in range(n):
        if s[i] == p[0]:
            if i + 1 < n and s[i + 1] == p[1]:
                occ[i + 2] = max(occ[i + 2], occ[i] + 1)
            else:
                occ[i + 1] = max(occ[i + 1], occ[i] + 1)
    return occ

