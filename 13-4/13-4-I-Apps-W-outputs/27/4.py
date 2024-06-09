
def get_min_m(n, k):
    m = 1
    while True:
        sets = []
        for i in range(n):
            set_size = 0
            while set_size < 4:
                num = m
                for j in range(i):
                    if num % sets[j][set_size] != 0:
                        break
                else:
                    sets.append([num])
                    set_size += 1
            m += 1
        if all(gcd(s[i], s[j]) == k for i in range(4) for j in range(i+1, 4) for s in sets):
            return m

