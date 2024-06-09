
def is_m_cute(a, b, m):
    if a == b:
        return 1
    if a > b:
        return -1
    x = [a]
    while x[-1] < b:
        x.append(x[-1] + x[-2] + 1)
        if x[-1] > b:
            return -1
        if x[-1] == b:
            return len(x)
    return -1

