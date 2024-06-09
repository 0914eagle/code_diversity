
def get_min_m(n, k):
    m = 1
    while True:
        sets = []
        for i in range(n):
            set_size = 0
            while set_size < 4:
                num = m + 1 + i + set_size
                if all(num % x != 0 for x in sets):
                    sets.append(num)
                    set_size += 1
            if set_size < 4:
                return -1
        if all(gcd(sets[i], sets[j]) == k for i in range(n) for j in range(i+1, n)):
            return m
        m += 1

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n, k = map(int, input().split())
m = get_min_m(n, k)
if m == -1:
    print(-1)
else:
    for i in range(n):
        print(*[m+1+i+j for j in range(4)], sep=' ')

