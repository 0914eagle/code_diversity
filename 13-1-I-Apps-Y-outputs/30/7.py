
def find_min_divisible_by_2_and_n(n):
    for i in range(1, n+1):
        if i % 2 == 0 and i % n == 0:
            return i
    return -1

