
def solve(s, t):
    s_concat = s * 10**100
    for i in range(len(s_concat)):
        if t in s_concat[:i+1]:
            return i
    return -1

