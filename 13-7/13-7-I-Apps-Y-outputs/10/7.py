
def solve(s, t):
    k = len(s)
    assert k == len(t)
    assert s < t

    # generate all strings between s and t in lexicographical order
    strings = []
    for i in range(k):
        for c in range(ord('a'), ord('z') + 1):
            if s[i] < chr(c) <= t[i]:
                strings.append(s[:i] + chr(c) + s[i+1:])

    # find the median
    return strings[len(strings) // 2]

