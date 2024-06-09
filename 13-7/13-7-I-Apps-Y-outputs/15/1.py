
def solve(s, t):
    s_count = [0] * 26
    t_count = [0] * 26
    for c in s:
        s_count[ord(c) - ord('a')] += 1
    for c in t:
        t_count[ord(c) - ord('a')] += 1
    if s_count < t_count:
        return "Yes"
    for i in range(26):
        if s_count[i] < t_count[i]:
            return "Yes"
        elif s_count[i] > t_count[i]:
            return "No"
    return "Yes"

