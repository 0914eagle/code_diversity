
def get_median(s, t):
    k = len(s)
    assert k == len(t)
    assert s < t
    assert k % 2 == 1

    med = ""
    for i in range(k):
        if s[i] < t[i]:
            med += "a"
        elif s[i] > t[i]:
            med += "z"
        else:
            med += "a"
    return med

