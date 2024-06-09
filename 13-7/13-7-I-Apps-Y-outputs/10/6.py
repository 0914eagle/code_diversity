
def solve(s, t):
    k = len(s)
    assert k == len(t)
    assert s < t
    assert k % 2 == 1

    # create a list of all strings between s and t
    strings = []
    for i in range(ord('a'), ord('a') + k):
        for j in range(ord('a'), ord('a') + k):
            if i <= ord(s[0]) and ord(s[0]) <= j and i <= ord(t[0]) and ord(t[0]) <= j:
                strings.append(chr(i) + chr(j))

    # find the median of the list
    mid = len(strings) // 2
    if len(strings) % 2 == 0:
        return strings[mid - 1]
    else:
        return strings[mid]

