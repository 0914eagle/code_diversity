
def chicken_left_over(n, m):
    if n == m:
        return "Dr. Chaz will have 0 pieces of chicken left over!"
    elif n > m:
        return "Dr. Chaz needs {} more pieces of chicken!".format(n - m)
    else:
        return "Dr. Chaz will have {} pieces of chicken left over!".format(m - n)

