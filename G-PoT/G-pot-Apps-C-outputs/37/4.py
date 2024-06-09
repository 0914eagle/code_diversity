
def find_smallest_distance(m, x, y):
    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def mod_inv(a, m):
        g, x, y = extended_gcd(a, m)
        if g != 1:
            raise Exception('Modular inverse does not exist')
        else:
            return x % m

    def chinese_remainder_theorem(n, a):
        sum = 0
        prod = 1
        for ni in n:
            prod *= ni
        for i in range(len(n)):
            p = prod // n[i]
            sum += a[i] * mod_inv(p, n[i]) * p
        return sum % prod

    n = list(m)
    a = list(x)
    for i in range(3):
        if a[i] > y[i]:
            a[i] = y[i] + 1
        elif a[i] < y[i]:
            a[i] = y[i] - 1
    return chinese_remainder_theorem(n, a)

m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

result = find_smallest_distance(m, x, y)
print(result)
