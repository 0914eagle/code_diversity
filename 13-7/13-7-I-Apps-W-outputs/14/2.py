
def cyclic_shift(s):
    n = len(s)
    count = 1
    for i in range(n):
        s = s[1:] + s[0]
        count += 1
    return count

