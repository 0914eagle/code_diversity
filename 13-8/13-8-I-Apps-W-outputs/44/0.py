
def solve(n, p):
    badges = [0] * (n + 1)
    for i in range(1, n + 1):
        if badges[i] == 0:
            badges[i] = 1
            i = p[i - 1]
        else:
            badges[i] = 2
            break
    return badges[1:]

