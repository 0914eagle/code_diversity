
def solve(n, m):
    if n == m:
        return "Dr. Chaz will have 0 pieces of chicken left over!"
    elif n > m:
        return "Dr. Chaz needs " + str(n - m) + " more pieces of chicken!"
    else:
        return "Dr. Chaz will have " + str(m - n) + " pieces of chicken left over!"

