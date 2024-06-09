
def find_nearest_fraction(x, y, n):
    min_denom = 10**5 + 1
    min_num = 10**5 + 1
    for a in range(n+1):
        b = x*a // y
        if b <= n and abs(x*a//y - x//y) < min_denom:
            min_denom = abs(x*a//y - x//y)
            min_num = a
    return str(min_num) + "/" + str(min_denom)

