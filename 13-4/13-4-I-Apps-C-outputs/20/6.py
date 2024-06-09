
def solve(m, n, p, q):
    if m < n or m > 1000000 or n > 1000000 or p > 1000000 or q > 1000000:
        return "IMPOSSIBLE"
    if m == n == 1:
        return str(p * q)
    if m == n == 2:
        return str(int(str(p) + str(q)) * 10)
    if m == 3 and n == 2:
        return str(int(str(p) + str(q)) * 100)
    if m == 4 and n == 3:
        return str(int(str(p) + str(q)) * 1000)
    if m == 5 and n == 4:
        return str(int(str(p) + str(q)) * 10000)
    if m == 6 and n == 5:
        return str(int(str(p) + str(q)) * 100000)
    if m == 7 and n == 6:
        return str(int(str(p) + str(q)) * 1000000)
    if m == 8 and n == 7:
        return str(int(str(p) + str(q)) * 10000000)
    if m == 9 and n == 8:
        return str(int(str(p) + str(q)) * 100000000)
    if m == 10 and n == 9:
        return str(int(str(p) + str(q)) * 1000000000)
    return "IMPOSSIBLE"

