
def is_m_cute(a, b, m):
    if a == b:
        return True, [a]
    if a > b or m < 1:
        return False, []
    x = [a]
    while x[-1] < b:
        r = x[-1]
        for i in range(1, m+1):
            x.append(r + i)
            if x[-1] > b:
                break
        if x[-1] == b:
            return True, x
    return False, []

