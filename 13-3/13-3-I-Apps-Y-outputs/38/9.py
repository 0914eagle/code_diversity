
def find_min_value(n, k):
    while n != 0:
        n = abs(n - k)
    return n

