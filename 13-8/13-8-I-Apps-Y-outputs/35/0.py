
def solve(s):
    n = len(s)
    count = [s.count(i) for i in "012"]
    diff = min(count) - max(count)
    if diff == 0:
        return s
    else:
        for i in range(n):
            if s[i] == "0":
                s = s[:i] + "1" + s[i+1:]
                break
        return s

