
def chicken_leftovers(n, m):
    if n > m:
        return "Dr. Chaz needs " + str(n - m) + " more piece[s] of chicken!"
    else:
        return "Dr. Chaz will have " + str(m - n) + " piece[s] of chicken left over!"

