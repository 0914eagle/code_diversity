
def get_min_m(n, k):
    m = 1
    while True:
        sets = []
        for i in range(n):
            set_size = 0
            while set_size < 4:
                num = m
                for j in range(set_size):
                    if num % sets[i][j] != 0:
                        break
                else:
                    sets.append(num)
                    set_size += 1
                m += 1
        if all(gcd(sets[i][0], sets[i][1]) == k and gcd(sets[i][1], sets[i][2]) == k and gcd(sets[i][2], sets[i][3]) == k for i in range(n)):
            return m

