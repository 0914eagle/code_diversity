
def find_n(factorial):
    n = 1
    while factorial > 1:
        factorial //= n
        n += 1
    return n - 1

