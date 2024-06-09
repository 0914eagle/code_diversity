
def solve(s, t):
    k = len(s)
    assert k == len(t)
    assert s < t
    assert k % 2 == 1

    # create a list of all strings between s and t (including s and t)
    strings = [s[i:i+k] for i in range(k)]

    # find the middle element of the list
    median = strings[k//2]

    return median

