
def get_median(s, t):
    k = len(s)
    assert k == len(t)
    assert s < t
    assert k % 2 == 1

    # generate all strings between s and t
    strings = []
    for i in range(k):
        for c in range(ord('a'), ord('z') + 1):
            if chr(c) >= s[i] and chr(c) <= t[i]:
                strings.append(s[:i] + chr(c) + s[i+1:])

    # sort the strings and return the middle element
    strings.sort()
    return strings[k // 2]

