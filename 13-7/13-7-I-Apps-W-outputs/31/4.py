
def solve(n, t, a):
    days = 0
    while t > 0:
        if t > a[days]:
            t -= a[days]
        else:
            t -= t
        days += 1
    return days

