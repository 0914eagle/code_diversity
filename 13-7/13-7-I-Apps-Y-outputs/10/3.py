
def solve(s, t):
    k = len(s)
    assert k == len(t)
    assert s < t
    assert k % 2 == 1

    # create a list of all strings between s and t (including s and t)
    strings = [s]
    current = s
    while current != t:
        current = next_string(current)
        strings.append(current)
    strings.append(t)

    # find the median of the list
    median = strings[k // 2]

    return median

def next_string(s):
    # find the leftmost letter that is not z
    i = 0
    while s[i] == "z":
        i += 1
    # if all letters are z, the string is the last one
    if i == len(s):
        return "aa" * len(s)
    # increment the leftmost letter
    s = s[:i] + chr(ord(s[i]) + 1) + "a" * (len(s) - i - 1)
    return s

