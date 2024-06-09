
def get_balanced_ternary_string(s):
    n = len(s)
    count = [s.count(i) for i in "012"]
    diff = max(count) - min(count)
    if diff > 1:
        return -1
    if diff == 0:
        return s
    char = "012"[count.index(min(count))]
    return s.replace(char, "012"[(count.index(min(count)) + 1) % 3])

