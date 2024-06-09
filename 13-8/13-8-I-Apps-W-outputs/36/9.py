
def get_min_m(n, k):
    m = 1
    while True:
        if is_possible(n, k, m):
            return m
        m += 1

def is_possible(n, k, m):
    sets = []
    for i in range(n):
        set_size = 0
        while set_size < 4:
            num = random.randint(1, m)
            if all(num not in s for s in sets):
                sets.append(num)
                set_size += 1
        if not is_valid_set(sets[-1], k):
            return False
    return True

def is_valid_set(set, k):
    for i in range(len(set)):
        for j in range(i+1, len(set)):
            if gcd(set[i], set[j]) != k:
                return False
    return True

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

n, k = map(int, input().split())
m = get_min_m(n, k)
sets = []
for i in range(n):
    set_size = 0
    while set_size < 4:
        num = random.randint(1, m)
        if all(num not in s for s in sets):
            sets.append(num)
            set_size += 1
    print(*sets[-1])

