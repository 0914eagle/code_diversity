
def is_m_cute(a, b, m):
    if a == b:
        return True, [a]
    if a > b or m < 1:
        return False, []
    x = [a]
    while x[-1] < b:
        r = x[-1]
        for i in range(m):
            x.append(x[-1] + r)
        if x[-1] > b:
            break
    return x[-1] == b, x
