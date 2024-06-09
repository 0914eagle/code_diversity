
def get_min_m(n, k):
    m = 1
    while True:
        sets = []
        for i in range(n):
            set_size = 0
            while set_size < 4:
                num = m * (i + 1) + set_size + 1
                if num > m:
                    break
                sets.append(num)
                set_size += 1
            if len(sets) == n:
                break
        m += 1
    return m, sets

