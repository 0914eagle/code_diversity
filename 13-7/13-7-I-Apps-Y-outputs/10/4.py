
def get_median(s, t):
    k = len(s)
    assert k == len(t)
    assert s < t
    assert k % 2 == 1

    # create a list of all strings between s and t, inclusive
    strings = [s[i] + t[i] for i in range(k)]

    # sort the list
    strings.sort()

    # return the middle element
    return strings[k//2]

