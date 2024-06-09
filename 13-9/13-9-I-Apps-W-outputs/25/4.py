
def is_m_cute(a, b, m):
    if a == b:
        return 1
    elif a > b:
        return -1
    else:
        x = a
        y = b
        count = 0
        while x < y:
            count += 1
            x += a
            a += 1
        if count <= m:
            return count
        else:
            return -1

