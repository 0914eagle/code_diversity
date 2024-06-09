
def get_min_m(n, k):
    m = 1
    while True:
        sets = []
        for i in range(n):
            set_size = 0
            while set_size < 4:
                num = m
                for set_ in sets:
                    if num in set_:
                        break
                else:
                    sets.append([num])
                    set_size += 1
            sets[i].sort()
        gcds = []
        for set_ in sets:
            gcd = set_[0]
            for num in set_[1:]:
                gcd = gcd(gcd, num)
            gcds.append(gcd)
        if all(gcd == k for gcd in gcds):
            return m
        m += 1

