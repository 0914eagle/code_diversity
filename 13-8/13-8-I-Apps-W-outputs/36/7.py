
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
            num = m - set_size
            if gcd(num, m) == k:
                sets.append(num)
                set_size += 1
            m -= 1
        if len(sets) != len(set(sets)):
            return False
    return True

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def main():
    n, k = map(int, input().split())
    m = get_min_m(n, k)
    print(m)
    for i in range(n):
        print(*[m - i for i in range(4)])

if __name__ == "__main__":
    main()

