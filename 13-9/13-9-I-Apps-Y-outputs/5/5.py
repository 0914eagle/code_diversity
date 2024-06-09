
def solve(n, m):
    if n == m:
        return "Dr. Chaz will have 0 pieces of chicken left over!"
    elif n > m:
        return "Dr. Chaz needs {} more piece{} of chicken!".format(n - m, "s" if n - m > 1 else "")
    else:
        return "Dr. Chaz will have {} piece{} of chicken left over!".format(m - n, "s" if m - n > 1 else "")

