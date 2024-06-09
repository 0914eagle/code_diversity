
def get_divine_digits(n, k, a):
    divine_digits = []
    for i in range(k):
        total = 0
        for j in range(n):
            total += a[j] * (i ** j)
        if str(total)[-1] == str(i):
            divine_digits.append(i)
    return len(divine_digits), sorted(divine_digits)

