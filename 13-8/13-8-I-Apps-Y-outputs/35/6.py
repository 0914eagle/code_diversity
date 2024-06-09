
def solve(s):
    n = len(s)
    count = [s.count(i) for i in "012"]
    diff = min(count) - max(count)
    if diff == 0:
        return s
    elif diff == 1:
        return "".join(sorted(s))
    else:
        char = "012"[count.index(min(count))]
        return "".join(char if i != char else "012"[(i + 1) % 3] for i in s)

