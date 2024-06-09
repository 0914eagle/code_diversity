
from sympy import mod_inverse

def chinese_remainder_theorem(n, a):
    total = 0
    prod = 1
    for ni in n:
        prod *= ni
    for ni, ai in zip(n, a):
        p = prod // ni
        total += ai * mod_inverse(p, ni) * p
    return total % prod

m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

n = []
a = []
for i in range(3):
    n.append(m[i])
    a.append(x[i])

z = chinese_remainder_theorem(n, a)

for i in range(3):
    while (z - x[i]) % m[i] > y[i]:
        z += m[i]

print(z)
