
def find_min_divisible_by_2_and_n(n):
    for i in range(n, n*2):
        if i % n == 0 and i % 2 == 0:
            return i
    return -1

