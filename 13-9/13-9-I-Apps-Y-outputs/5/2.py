
def solve(n, m):
    if m >= n:
        return "Dr. Chaz will have " + str(m - n) + " piece[s] of chicken left over!"
    else:
        return "Dr. Chaz needs " + str(n - m) + " more piece[s] of chicken!"

