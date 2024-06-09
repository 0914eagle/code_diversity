
def get_balanced_ternary_string(s):
    n = len(s)
    count = [s.count(i) for i in '012']
    diff = max(count) - min(count)
    if diff > 1:
        return -1
    if diff == 0:
        return s
    for i in range(n):
        if s[i] == '0':
            s = s[:i] + '1' + s[i+1:]
            break
    return s

