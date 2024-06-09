
def is_m_cute(a, b, m):
    if a == b:
        return 1
    elif b - a == 1:
        return 2
    else:
        x = (a + b) // 2
        y = b - x
        if x <= m and y <= m:
            return 2
        elif x > m and y <= m:
            return is_m_cute(a, x - 1, m) + is_m_cute(x, b, m)
        elif x <= m and y > m:
            return is_m_cute(a, x + 1, m) + is_m_cute(x + 1, b, m)
        else:
            return is_m_cute(a, x - 1, m) + is_m_cute(x + 1, b, m)

def solve(a, b, m):
    if is_m_cute(a, b, m) == 1:
        return [a]
    elif is_m_cute(a, b, m) == 2:
        return [a, b]
    else:
        return [-1]

