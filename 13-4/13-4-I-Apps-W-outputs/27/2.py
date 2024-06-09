
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
        if not all(gcd(s1, s2) == k for s1, s2 in combinations(sets, 2)):
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    n, k = map(int, input().split())
    m = get_min_m(n, k)
    print(m)
    for i in range(n):
        set_size = 0
        while set_size < 4:
            num = random.randint(1, m)
            if all(num not in s for s in sets):
                sets.append(num)
                set_size += 1
        print(*sets)

if __name__ == "__main__":
    main()

