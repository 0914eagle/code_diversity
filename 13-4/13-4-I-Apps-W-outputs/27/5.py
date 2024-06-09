
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
        if all(gcd(s[0], s[1]) == k and gcd(s[1], s[2]) == k and gcd(s[2], s[3]) == k for s in sets):
            return m

